from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, random, string, sys

def get_icon():
    pixmap = QPixmap(16, 16)
    pixmap.fill(Qt.transparent)
    painter = QPainter()
    painter.begin(pixmap)
    painter.setFont(QFont('Webdings', 11))
    painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
    painter.drawText(0, 0, 16, 16, Qt.AlignCenter, random.choice(string.ascii_letters))
    painter.end()
    return QIcon(pixmap)


def about_qt():
    QApplication.instance().aboutQt()


context_menu_stylesheet = """
QMenu {
    /* Translucent effect */
    background-color: rgba(255, 255, 255, 230);
    border: none;
    border-radius: 4px;
}

QMenu::item {
    border-radius: 4px;
    /* This distance is cumbersome and needs to be fine-tuned based on factors such as menu length and icons */
    padding: 8px 48px 8px 36px; /* 36px is the distance from the text to the left*/
    background-color: transparent;
}

/* Mouseover and press effects */
QMenu::item:selected {
    border-radius: 0px;
    color: blue;
    background-color: rgba(32, 32, 32, 32);
    /* background-color: transparent; */
}

/*
QMenu::item:hovered {
    border-radius: 0px;
    background-color: transparent;
}
*/

/* disable effect */
QMenu::item:disabled {
    background-color: transparent;
}

/* icon distance to the left */
QMenu::icon {
    left: 15px;
}

/* split line effect */
QMenu::separator {
    height: 1px;
    background-color: rgb(232, 236, 243);
}
"""



class AcdseeWidget(QGraphicsView):

    def doShow(self):
        try:
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def init_menu(self):
        self.context_menu.setAttribute(Qt.WA_TranslucentBackground)
        self.context_menu.setWindowFlags(self.context_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        for i in range(10):
            if i % 2 == 0:
                action = self.context_menu.addAction('menu %d' % i, about_qt)
                action.setEnabled(i % 4)
            elif i % 3 == 0:
                self.context_menu.addAction(get_icon(), 'menu %d' % i, about_qt)
            if i % 4 == 0:
                self.context_menu.addSeparator()
            if i % 5 == 0:
                menu = QMenu('Secondary menu %d' % i, self.context_menu)
                menu.setAttribute(Qt.WA_TranslucentBackground)
                menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
                for j in range(3):
                    menu.addAction(get_icon(), 'Submenu %d' % j)
                self.context_menu.addMenu(menu)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QPixmap(file_path))
            event.accept()
        else:
            event.ignore()

    def __init__(self, *args, **kwargs):
        background = kwargs.pop('background', Qt.black)
        super(AcdseeWidget, self).__init__(*args, **kwargs)

        self.setAcceptDrops(True)

        self.setStyleSheet(context_menu_stylesheet)
        self.setCursor(Qt.OpenHandCursor)
        self.setBackground(background)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.SmoothPixmapTransform)
        self.setCacheMode(self.CacheBackground)
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        self._item = QGraphicsPixmapItem()
        self._item.setFlags(QGraphicsPixmapItem.ItemIsFocusable | QGraphicsPixmapItem.ItemIsMovable)
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self._scene.addItem(self._item)
        rect = QApplication.instance().desktop().availableGeometry(self)
        self.resize(int(rect.width() * 2 / 3), int(rect.height() * 2 / 3))

        self.pixmap = None
        self._delta = 0.1
        self.context_menu = QMenu(self)
        self.init_menu()

        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(1000)

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def setBackground(self, color):
        if isinstance(color, QColor):
            self.setBackgroundBrush(color)
        elif isinstance(color, (str, Qt.GlobalColor)):
            color = QColor(color)
            if color.isValid():
                self.setBackgroundBrush(color)

    def setPixmap(self, pixmap, fitIn=True):
        if isinstance(pixmap, QPixmap):
            self.pixmap = pixmap
        elif isinstance(pixmap, QImage):
            self.pixmap = QPixmap.fromImage(pixmap)
        elif isinstance(pixmap, str) and os.path.isfile(pixmap):
            self.pixmap = QPixmap(pixmap)
        else:
            return
        self._item.setPixmap(self.pixmap)
        self._item.update()
        self.setSceneDims()
        if fitIn:
            self.fitInView(QRectF(self._item.pos(), QSizeF(self.pixmap.size())), Qt.KeepAspectRatio)
        self.update()

    def setSceneDims(self):
        if not self.pixmap:
            return
        self.setSceneRect(QRectF(QPointF(0, 0), QPointF(self.pixmap.width(), self.pixmap.height())))

    def fitInView(self, rect, flags=Qt.IgnoreAspectRatio):
        if not self.scene() or rect.isNull():
            return
        unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        viewRect = self.viewport().rect()
        sceneRect = self.transform().mapRect(rect)
        x_ratio = viewRect.width() / sceneRect.width()
        y_ratio = viewRect.height() / sceneRect.height()
        if flags == Qt.KeepAspectRatio:
            x_ratio = y_ratio = min(x_ratio, y_ratio)
        elif flags == Qt.KeepAspectRatioByExpanding:
            x_ratio = y_ratio = max(x_ratio, y_ratio)
        self.scale(x_ratio, y_ratio)
        self.centerOn(rect.center())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def zoomIn(self):
        self.zoom(1 + self._delta)

    def zoomOut(self):
        self.zoom(1 - self._delta)

    def zoom(self, factor):
        _factor = self.transform().scale(factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            return
        self.scale(factor, factor)
