
import os, pathlib, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

from .acdsee import AcdseeWidget
from .common import FILEOUTPUT_EXT
from .graphcompiler import graph_compile_code

__CURDIR__ = pathlib.Path(__file__).parents[0]


status_filepath = str(__CURDIR__ / 'status.jpg').replace('\\', '/')
bgfilepath = str(__CURDIR__/'bg.jpg').replace('\\', '/')

# print(f"""
# status_filepath = {status_filepath}
# bgfilepath = {bgfilepath}
# """)

def resize_screen_ratio(object, posx_ratio=1/2, ratio=1/6, wratio=0, delta = 60):
    """
    posx_ratio = 1/2 = center of the screen
    """
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()

    if not wratio:
        wratio = ratio
    #print('wratio:', wratio)
    lebar, tinggi = int(screenw*wratio),int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)


def file_content(filepath):
	"""
	retval berupa segelondongan text/string
	https://stackoverflow.com/questions/45529507/unicodedecodeerror-utf-8-codec-cant-decode-byte-0x96-in-position-35-invalid
	update utk:
	'utf-8' codec can't decode byte 0x93 in position 68384: invalid start byte
	errors='ignore'
	"""
	return pathlib.Path(filepath).read_text(encoding='utf8', errors='ignore')



class EditorStandard(QsciScintilla):

    def __init__(self, parent=None, *args, **kwargs):
        super(EditorStandard, self).__init__(parent, *args, **kwargs)
        self.margin = 24
        self.init()
        self.linesChanged.connect(self.onLinesChanged)

        self.init_content()

    def init_content(self):
        content = file_content(str (__CURDIR__ / 'gc.txt') )
        self.setText(content)

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + self.margin)

    def init(self):
        self.setUtf8(True)

        # lexer = QsciLexerMarkdown(self)
        lexer = QsciLexerPython(self)
        self.setLexer(lexer)

        self.setAutoCompletionCaseSensitivity(False)  # ignore case
        self.setAutoCompletionSource(self.AcsAll)
        self.setAutoCompletionThreshold(1)  # One character pops up completion
        self.setAutoIndent(True)  # auto indent
        self.setBackspaceUnindents(True)
        self.setBraceMatching(self.StrictBraceMatch)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setTabWidth(4)
        self.setWhitespaceSize(1)
        self.setWhitespaceVisibility(self.WsVisible)
        self.setWhitespaceForegroundColor(Qt.gray)
        self.setWrapIndentMode(self.WrapIndentFixed)
        self.setWrapMode(self.WrapWord)

        # fold
        # https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
        self.setFolding(self.BoxedTreeFoldStyle, 2)
        self.setFoldMarginColors(QColor("#676A6C"), QColor("#676A6D"))
        font = self.font() or QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(13)
        self.setFont(font)
        self.setMarginsFont(font)
        self.fontmetrics = QFontMetrics(font)
        lexer.setFont(font)

        self.setMarginWidth(0, self.fontmetrics.width(str(self.lines())) + self.margin)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("gainsboro"))
        self.setMarginWidth(1, 0)
        self.setMarginWidth(2, 14)

        completeKey = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Slash), self)
        completeKey.setContext(Qt.WidgetShortcut)
        completeKey.activated.connect(self.autoCompleteFromAll)

        QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())


class MainWindow(QMainWindow):



    def __init__(self):
        super().__init__()

        self.initUI()


    def run_code(self):
        content = self.editor.text()
        if content:
            # print('running code:', content)
            graph_compile_code(content)
            self.image_viewer.setPixmap(FILEOUTPUT_EXT)

    def openFile(self, path=None):
        if not path:
            path, _ = QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "Python Files (*.py);; all Files (*)")
        if path:
            self.openFileOnStart(path)

    def openFileOnStart(self, path=None):
        try:
            content = file_content(path)
            self.editor.setText(content)
            # self.filepath = path
            # self.filepath_label.setText(self.filepath)
        except Exception as err:
            print(err)

    def initUI(self):

        self.main_layout = QHBoxLayout()
        split0 = QSplitter(Qt.Horizontal)
        split0_page_0 = QWidget(self)
        split0_pagelayout_0 = QVBoxLayout(split0_page_0)


        mylayout = QVBoxLayout()
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_code)
        # mylayout.addWidget(self.run_button)
        buttonbar = QHBoxLayout()
        buttonbar.addWidget(self.run_button)
        buttonbar.addStretch(1)
        # mylayout.addStretch(1)
        mylayout.addLayout(buttonbar)

        self.editor = EditorStandard(self)
        self.editor.setStyleSheet('min-width: 400px;')
        mylayout.addWidget(self.editor)
        split0_pagelayout_0.addLayout(mylayout)
        
        split0.addWidget(split0_page_0)

        split0_page_1 = QWidget(self)
        split0_pagelayout_1 = QVBoxLayout(split0_page_1)
                

        self.image_viewer = AcdseeWidget(parent=self)
        self.image_viewer.setStyleSheet('min-width: 400px;')
        split0_pagelayout_1.addWidget(self.image_viewer)
        split0.addWidget(split0_page_1)

        self.image_viewer.setPixmap('dotlang.png')

        split0.handle(1).setStyleSheet('background: 3px blue;')
        self.main_layout.addWidget(split0)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.statusBar().showMessage("Write the code in the editor, click the run button, then see the result on the image view pane on the right (Scoll to zoom in/out).")        
        self.statusBar().setStyleSheet(f"background-image : url({status_filepath}); background-position: center; color: orange;")

        openAct = QAction("&Open", self)
        openAct.setShortcut("Ctrl+O")
        openAct.setStatusTip("Open file")
        openAct.triggered.connect(self.openFile)
        openAct.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogStart))


        editAct = QAction("&Edit", self)
        editAct.setShortcut("Ctrl+E")
        editAct.setStatusTip("Edit file")
        # editAct.triggered.connect(lambda: os.system(f"code {__file__}"))
        editAct.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogDetailedView))

        exitAct = QAction("E&xit", self)
        exitAct.setShortcut("Ctrl+X")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(qApp.quit)
        exitAct.setIcon(QApplication.style().standardIcon(QStyle.SP_BrowserStop))

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")

        file_menu.addAction(openAct)
        file_menu.addAction(editAct)

        file_menu.addAction(exitAct)
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(openAct)
        toolbar.addAction(editAct)
        toolbar.addAction(exitAct)


def set_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)


background_image_stylesheet = f"""
MainWindow {{
    border-image: url("{bgfilepath}");
    background-repeat: no-repeat; 
    background-position: center;
}}
"""


def main():
    app = QApplication([])
    # set_theme(app)
    wnd = MainWindow()
    wnd.setStyleSheet(background_image_stylesheet)
    wnd.show()
    # wnd.resize(1200, 800)
    resize_screen_ratio(wnd, ratio=0.8, wratio=0, delta = 60)
    wnd.setWindowTitle("Ivy's Graph Compiler")
    QShortcut(QKeySequence("Ctrl+Q"), wnd, activated=lambda: qApp.quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
