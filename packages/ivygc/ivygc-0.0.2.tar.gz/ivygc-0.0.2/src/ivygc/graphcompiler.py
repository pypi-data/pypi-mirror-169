import sys, json
import os, os.path
from io import open
import glob, time

from .dotlang import dotlang


from lark import Lark
from lark.indenter import Indenter

import lark
pohon = lark.tree.Tree
token = lark.lexer.Token
ispohon = lambda i: isinstance(i, pohon)
istoken = lambda i: isinstance(i, token)



class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


kwargs = dict(postlex=PythonIndenter(), start='file_input')

chosen_parser = Lark.open('py.grammar', rel_to=__file__, parser='lalr', **kwargs)

# counter = 1
current_class = None

function_calls = []

dependency_graph = {}

def func_name(item):
    retval = ''
    # for item in suite.children:
    if item.data == 'var':
        retval = str(item.children[0].children[0])
    elif item.data == 'getattr':
        class_name = str(item.children[0].children[0].children[0])
        method_name = str(item.children[1].children[0])
        retval = f"{class_name}.{method_name}"
    return retval

def arguments_list(suite):
    retval = []
    for item in suite.children:
        if item.data == 'var':
            item = str(item.children[0].children[0])
            retval.append(item)
    return retval

def arguments_factor(suite):
    retval = ''
    for item in suite.children:
        if istoken(item):
            retval += str(item)
        elif item.data == 'number':
            retval += str(item.children[0])
    return int(retval)

def arguments(suite):
    retval = []
    for item in suite.children:
        if item.data == 'var':
            arg = str(item.children[0].children[0])
            retval.append(arg)
        elif item.data == 'list':
            arg_list = arguments_list(item)
            retval += arg_list
        elif item.data == 'factor':
            arg_factor = arguments_factor(item)
            retval.append(arg_factor)
    return retval

def function_call(suite, add_to_dependency_graph=None, dependency_graph_parent=''):
    """
    """
    function_name, function_args = '', []
    for item in suite.children:
        if isinstance(item, pohon):
            if item.data in ['getattr', 'var']:
                function_name = func_name(item)
            # elif item.data == 'getattr':
            #     function_name = func_name(item)
            elif item.data == 'arguments':
                function_args = arguments(item)
    return function_name, function_args

def arith_expr(suite):
    retval = []
    value = ''
    for item in suite.children:
        if istoken(item):
            arg = str(item)
            # retval.append(arg)
            if arg == '+':
                value += (',' if value else '') + 'torch.add'
            elif arg == '-':
                value += (',' if value else '') + 'torch.sub'
            elif arg == '*':
                value += (',' if value else '') + 'torch.matmul'
            elif arg == '/':
                value += (',' if value else '') + 'torch.div'
        elif item.data == 'var':
            arg = str(item.children[0].children[0])
            retval.append(arg)
        elif item.data == 'term':
            args, val = assign_term(item)  # val = mul
            if value:
                value += ',' + val
            else:
                value = val
            retval += args
            # arg = str(item.children[0].children[0])
            # retval.append(arg)
            # elif item.data == 'term':
            #     args, val = assign_term(item)
            #     dependency_graph[function_name][left_hand_side_name]['value'] = val
            #     dependency_graph[function_name][left_hand_side_name]['depends'] = args
    return retval, value

def assign_term(suite):
    retval = []
    value = ''
    for item in suite.children:
        if istoken(item):
            arg = str(item)
            # retval.append(arg)
            if arg == '+':
                value = 'torch.add'
            elif arg == '-':
                value = 'torch.sub'
            elif arg == '*':
                value = 'torch.matmul'
            elif arg == '/':
                value = 'torch.div'
        elif item.data == 'var':
            arg = str(item.children[0].children[0])
            retval.append(arg)
    return retval, value

def assign(suite, function_name, function_parameters):
    left_hand_side_name = ''
    for item in suite.children:
        if isinstance(item, pohon):
            if item.data == 'var':
                left_hand_side_name = str(item.children[0].children[0])
                dg_item = {
                    'type': 'assign',
                    'name': left_hand_side_name,
                    'value': '',
                    'depends': [],
                }
                # dependency_graph.append(dg_item)
                # dependency_graph[left_hand_side_name] = dg_item
                dependency_graph[function_name][left_hand_side_name] = dg_item
            elif item.data == 'arith_expr':
                args, val = arith_expr(item)
                dependency_graph[function_name][left_hand_side_name]['value'] = val
                dependency_graph[function_name][left_hand_side_name]['depends'] = args
            elif item.data == 'term':
                args, val = assign_term(item)
                dependency_graph[function_name][left_hand_side_name]['value'] = val
                dependency_graph[function_name][left_hand_side_name]['depends'] = args
            elif item.data == 'funccall':
                name, args = function_call(item, add_to_dependency_graph=True, dependency_graph_parent=left_hand_side_name)
                dependency_graph[function_name][left_hand_side_name]['value'] = name
                dependency_graph[function_name][left_hand_side_name]['depends'] = args

def assign_stmt(suite, function_name, function_parameters):
    for item in suite.children:
        if isinstance(item, pohon):
            if item.data == 'assign':
                assign(item, function_name, function_parameters)

def expr_stmt(suite, function_name, function_parameters):
    for item in suite.children:
        if isinstance(item, pohon):
            if item.data == 'funccall':
                function_call(item)

def return_arith_expr(suite, function_name, function_parameters=[]):
    """    
    dependency_graph[function_name][dependency_name]['value'] = val
    dependency_graph[function_name][dependency_name]['depends'] = args
    """

    items = []
    current_operator = ''
    current_term_operator = ''

    retval = []
    value = ''
    for item in suite.children:
        if istoken(item):
            arg = str(item)
            # retval.append(arg)
            if arg == '+':
                current_operator = 'torch.add'
            elif arg == '-':
                # value += (',' if value else '') + 'torch.sub'
                current_operator = 'torch.sub'
            elif arg == '*':
                # value += (',' if value else '') + 'torch.matmul'
                current_operator = 'torch.matmul'
            elif arg == '/':
                # value += (',' if value else '') + 'torch.div'
                current_operator = 'torch.div'


            if current_operator not in dependency_graph[function_name]:
                dependency_graph[function_name][current_operator] = {
                    'value': current_operator,
                    'depends': [],
                }
            else:
                i = 1
                current_operator = f"{current_operator}_{i}"
                while current_operator in dependency_graph[function_name]:
                    i += 1
                    current_operator = f"{current_operator}_{i}"
                dependency_graph[function_name][current_operator] = {
                    'value': current_operator,
                    'depends': [],
                }
            if current_term_operator:
                dependency_graph[function_name][current_operator]['depends'].append(current_term_operator)
            dependency_graph[function_name]['__output__']['depends'].append(current_operator)
        elif item.data == 'var':
            arg = str(item.children[0].children[0])
            # retval.append(arg)
            if current_operator:
                dependency_graph[function_name][current_operator]['depends'].append(arg)
            else:
                print(f"""var dalam arithmetic
                arg = {arg}
                function_name = {function_name}
                """)
        elif item.data == 'term':
            args, val = assign_term(item)  # val = mul
            # if value:
            #     value += ',' + val
            # else:
            #     value = val
            # retval += args

            term_operator = 'torch.matmul'
            if term_operator not in dependency_graph[function_name]:
                dependency_graph[function_name][term_operator] = {
                    'value': term_operator,
                    'depends': args,
                }
            else:
                i = 1
                term_operator = f"torch.matmul_{i}"
                while term_operator in dependency_graph[function_name]:
                    i += 1
                    term_operator = f"torch.matmul_{i}"
                dependency_graph[function_name][term_operator] = {
                    'value': term_operator,
                    'depends': args,
                }
            if current_operator:
                dependency_graph[function_name][current_operator]['depends'].append(term_operator)
            else:
                current_term_operator = term_operator

    return retval, value

def return_stmt(suite, function_name, function_parameters):
    dependency_name = '__output__'
    dependency_graph[function_name][dependency_name] = {}

    for item in suite.children:
        if isinstance(item, pohon):
            if item.data == 'var':
                depends = str(item.children[0].children[0])                
                dg_item = {
                    'type': 'return',
                    'name': dependency_name,
                    'depends': [depends],
                }
                # dependency_graph.append(dg_item)
                # dependency_graph[name] = dg_item
                dependency_graph[function_name][dependency_name] = dg_item
            elif item.data == 'funccall':
                # function_call(item, add_to_dependency_graph=True)
                # function_call(item)
                name, args = function_call(item)
                # if dependency_name not in dependency_graph[function_name]:
                #     dependency_graph[function_name][dependency_name] = {}
                dependency_graph[function_name][dependency_name]['value'] = name
                dependency_graph[function_name][dependency_name]['depends'] = args
            elif item.data == 'arith_expr':
                # args, val = arith_expr(item)
                # dependency_graph[function_name][dependency_name]['value'] = val
                # dependency_graph[function_name][dependency_name]['depends'] = args
                dependency_graph[function_name]['__output__']['depends'] = []
                return_arith_expr(item, function_name)

def process_suite(suite, level=0, function_name='', function_parameters=[]):
    for item in suite.children:
        if isinstance(item, pohon):
            if item.data == 'assign_stmt':
                assign_stmt(item, function_name, function_parameters)
            elif item.data == 'expr_stmt':
                expr_stmt(item, function_name, function_parameters)
            elif item.data == 'return_stmt':
                return_stmt(item, function_name, function_parameters)

        if hasattr(item, 'children'):
            process_suite(item, level+1)

def parameters(suite):
    """
    parameters
        name        x
        name        w
        name        b
        None
        None
        None
    """
    params = []
    for param in suite.children:
        if param is None:
            continue
        if isinstance(param, token):
            # print(f'\n\n*** ketemu token "{str(param)}"\n\n')
            params.append(param)
        elif param.data == 'name':
            arg = param.children[0]
            params.append(str(arg))
        elif param.data == 'paramvalue':
            # ada name dan value
            paramname = str(param.children[0].children[0])
            paramtype = param.children[1].data
            if param.children[0].data == 'typedparam':
                itemnametree = param.children[0].children[0]
                itemname = itemnametree.children[0]
                itemtype = 'getattr'
                if param.children[0].children[1].data == 'getitem':
                    itemtype = 'getitem'
                params.append(f"{itemname}:{itemtype}")
            elif paramtype in ['string', 'number']:
                paramvalue = str(param.children[1].children[0])
                # params.append(f"paramvalue {paramname}|type {paramtype}|value {paramvalue}")
                params.append(f"{paramname}: {paramtype} = {paramvalue}")
            elif paramtype in ['list', 'tuple']:
                values = []
                for paramitem in param.children[1].children:
                    values.append(str(paramitem.children[0]))
                # params.append(f"paramvalue {paramname}|type {paramtype}|value {', '.join(values)}")
                params.append(f"{paramname}: {paramtype} = [{', '.join(values)}]")
                # print(param)
            elif paramtype in ['dict']:
                values = []
                for paramitem in param.children[1].children:
                    # values.append(str(paramitem.children[0]))
                    itemname = str(paramitem.children[0].children[0])
                    itemvalue = str(paramitem.children[1].children[0])
                    values.append(f"{itemname}: {itemvalue}")
                params.append(f"{paramname}: {paramtype} = {{ {', '.join(values)} }}")
        elif param.data == 'starparams':
            for starparam_or_postparam in param.children:
                if starparam_or_postparam.children[0] is None:  # Tree(Token('RULE', 'poststarparams'), [None])])]),
                    continue
                # print('starparam', starparam_or_postparam)
                paramname = str(starparam_or_postparam.children[0].children[0])
                params.append(f"args*: {paramname}")
            # ada_args = True
        elif param.data == 'kwparams':
            for kwname in param.children:
                paramname = str(kwname.children[0])
                params.append(f"kw**: {paramname}")
            # ada_kwargs = True
        elif param.data == 'typedparam':
            itemname = str(param.children[0].children[0])
            itemtype = 'getattr'
            if param.children[1].data == 'getitem':
                itemtype = 'getitem'
            params.append(f"{itemname}: {itemtype}")
    return params

def function_definition(item, current_class=None):
    function_name, function_parameters, function_type, function_suite = '', [], {}, None

    for _item in item.children:
        if _item is None:
            continue
        if _item.data == 'name':
            function_name = str(_item.children[0])
            if current_class is not None:
                function_name = f"{current_class}.{function_name}"
            dependency_graph[function_name] = {}
        elif _item.data == 'parameters':
            function_parameters = parameters(_item)
            dependency_graph[function_name]['__input__'] = function_parameters
        elif _item.data == 'test':
            pass
        elif _item.data == 'suite':
            process_suite(_item, 0, function_name, function_parameters)

def print_item(item, level):
    # print(counter, level*'\t', item.data)
    if item.data in ['name', 'number']:
        namastr = item.children[0]
        print(level*'\t' + item.data, f'({namastr})')
    else:
        print(level*'\t' + item.data)

def process_tree(tree, level=0, function_name=''):
    
    global current_class

    if level==0:
        function_name = '__global__'

    for item in tree.children:
        if isinstance(item, pohon):

            # print_item(item, level)

            if item.data == 'funcdef':
                function_definition(item, current_class)
            elif item.data == 'funccall':
                function_call(item)
            elif item.data == 'assign_stmt':                
                if function_name and function_name not in dependency_graph:
                    dependency_graph[function_name] = {}
                if level == 0:
                    # only global assignment, local assignments were handled within funcdef
                    # print('assignment:', function_name, 'level:', level)
                    assign_stmt(item, function_name=function_name, function_parameters=[])
            # else:
            #     print('⚡', item.data)
        # else:
        #     print(item)

            # counter += 1

        if hasattr(item, 'children'):
            process_tree(item, level+1)

def graph_compile(thefile = 'gc.txt'):
    # path = _get_lib_path()
    start = time.time()

    with open(thefile, 'r', encoding='utf8') as fd:
        r = fd.read()
        result = chosen_parser.parse(r + '\n')


        print('*'*20)
        print(result.pretty())
        print('*'*20)

        process_tree(result)

    end = time.time()
    print( "graph_compile. time: %.2f secs" % (end-start) )

def fill_nodes_later(nodes, dependency_graph, initial_func, initial_node):
    source_value = dependency_graph[initial_func][initial_node]['value']
    if source_value.count('.') and not source_value.startswith('"'):
        source_value = '"' + source_value + '"'
    for depend in dependency_graph[initial_func][initial_node]['depends']:
        if depend in dependency_graph[initial_func]:
            value = dependency_graph[initial_func][depend]['value']
            if value.count('.') and not value.startswith('"'):
                value = '"' + value + '"'
            nodes.append(f'{source_value}[style=filled,color=mistyrose]=>{value}')
            if dependency_graph[initial_func][depend]['depends']:
                fill_nodes_later(nodes, dependency_graph, initial_func=initial_func, initial_node=depend)
        elif depend in dependency_graph[initial_func]['__input__']:
            if depend.count('.') and not depend.startswith('"'):
                depend = '"' + depend + '"'
            nodes.append(f'{source_value}[style=filled,color=mistyrose]=>{depend}')

def fill_nodes(nodes, dependency_graph, initial_func, initial_node='ret'):
    if initial_node.count('.') and not initial_node.startswith('"'):
        initial_node = '"' + initial_node + '"'
    for depend in dependency_graph[initial_func]['__output__']['depends']:
        if depend in dependency_graph[initial_func]:
            value = dependency_graph[initial_func][depend]['value']
            if value.count('.') and not value.startswith('"'):
                value = '"' + value + '"'
            config = '[style=filled,color=mistyrose]' if initial_node!='ret' else ''
            nodes.append(f'{initial_node}{config}=>{value}')
            if dependency_graph[initial_func][depend]['depends']:
                fill_nodes_later(nodes, dependency_graph, initial_func=initial_func, initial_node=depend)
        elif depend in dependency_graph[initial_func]['__input__']:
            if depend.count('.') and not depend.startswith('"'):
                depend = '"' + depend + '"'
            nodes.append(f'{initial_node}[style=filled,color=mistyrose]=>{depend}')

def process_dependency_graph(dependency_graph):
    func = None
    key_global = list(filter(lambda k: k=='__global__', dependency_graph.keys()))
    if key_global:
        # print('key_global:', key_global)
        key_graph = list(filter(lambda v: v['value']=='ivy.compile_graph', dependency_graph['__global__'].values()))
        if key_graph:
            # print('key_graph:', key_graph)
            key_graph = key_graph[0]
            main_function = None if not key_graph else key_graph['depends'][0]
            # return main_function
            func = main_function
    # return None
    # print(f"terima func:", func)
    nodes = []
    if func in dependency_graph and '__output__' in dependency_graph[func]:
        # start = dependency_graph[func]['__output__']
        nodes.append('ret')
        initial_node = 'ret'
        if 'value' in dependency_graph[func]['__output__']:
            value = dependency_graph[func]['__output__']['value']
            if value.count('.') and not value.startswith('"'):
                value = '"' + value + '"'
            # nodes.append(f'ret[style=filled,color=darkslategray1]=>{value}')
            nodes.append(f'ret=>{value}')
            initial_node = value
        fill_nodes(nodes, dependency_graph, initial_func=func, initial_node=initial_node)
    # ppr(nodes)

    # dotlang
    if 'ret' in nodes:
        nodes.remove('ret')
        # dotcode = '|'.join(['"'+item+'"' if item.count('.') else item for item in nodes])
        dotcode = '|'.join(nodes)
        dotconfig = '[style=rounded,style=filled,shape=box,color=darkslategray1]'
        dotcode = dotconfig + dotcode #+ '|ret[style=filled,color=darkslategray1]'
        dotlang(dotcode)

def graph_compile_code(code):
    result = chosen_parser.parse(code + '\n')
    process_tree(result)
    process_dependency_graph(dependency_graph)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        graph_compile(sys.argv[1])
    else:
        graph_compile()

    # ppr(dependency_graph)
    process_dependency_graph(dependency_graph)
    

