import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from qfluentwidgets import SplitFluentWindow, FluentIcon, FluentTranslator, setTheme, Theme

from view.home_ import Home
from view.v1text_ import V1text
from view.v2text_ import V2text
from view.img_ import Img
from view.img2_ import Img2
from view.imgresize_ import Imgresize


class BlindWaterMask(SplitFluentWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BlindWaterMask")
        self.resize(800, 500)
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.home = Home(self)
        self.v1text = V1text(self)
        self.v2text = V2text(self)
        self.img = Img(self)
        self.img2 = Img2(self)
        self.imgresize = Imgresize(self)

        self.addSubInterface(self.home, FluentIcon.HOME, "主页")
        self.addSubInterface(self.v1text, FluentIcon.PENCIL_INK, "文字盲水印v1")
        self.addSubInterface(self.v2text, FluentIcon.PENCIL_INK, "文字盲水印v2")
        self.addSubInterface(self.img, FluentIcon.PHOTO, "图片盲水印 文本")
        self.addSubInterface(self.img2, FluentIcon.PHOTO, "图片盲水印 图片")
        self.addSubInterface(self.imgresize, FluentIcon.PHOTO, "图片压缩")


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)

    setTheme(Theme.DARK)

    translator = FluentTranslator()
    app.installTranslator(translator)

    w = BlindWaterMask()
    w.show()
    app.exec_()
