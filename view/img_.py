from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QAction, QFileDialog

from qfluentwidgets import RoundMenu, FluentIcon, MessageBox, MessageDialog

from blind_watermark import bw_notes
from blind_watermark import WaterMark

from view.img_ui import Ui_Img_UI


class Img(Ui_Img_UI, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        bw_notes.close()

        self.inimg = None
        self.outimg = None
        self.setupUi(self)

        self.menu = RoundMenu(parent=self)
        embed_action = QAction(FluentIcon.RIGHT_ARROW.icon(), '添加水印')
        embed_action.triggered.connect(self.Embed)
        extract_action = QAction(FluentIcon.LEFT_ARROW.icon(), '提取水印')
        extract_action.triggered.connect(self.Extract)
        self.menu.addAction(embed_action)
        self.menu.addAction(extract_action)
        self.imgbutton.setMenu(self.menu)

        self.imginput1.clicked.connect(self.loadimg)
        self.imginput2.clicked.connect(self.saveimg)

    def loadimg(self):
        f = QFileDialog()
        f.setFileMode(QFileDialog.ExistingFile)
        f.setNameFilter('图片文件(*.jpg *.png *.bmp *.jpeg)')
        if f.exec():
            self.inimg = f.selectedFiles()[0]

    def saveimg(self):
        d = QFileDialog.getExistingDirectory(None, "选择文件夹路径")
        self.outimg = d + "/output.png"

    def Embed(self):
        try:
            if self.imgpwd.text() != ""  and self.inimg != None and self.outimg != None:
                bwm = WaterMark(password_img=int(self.imgpwd.text()), password_wm=int(self.imgpwd.text()))
                bwm.read_img(self.inimg)
                bwm.read_wm(self.imgwm.text(), mode='str')
                bwm.embed(self.outimg)
                self.imgshape.setText(str(len(bwm.wm_bit)))
            else:
                MessageBox("OH NO 添加水印出了点问题~", "也许是你没输入图片或者保存的路径？没输入密码？", self).exec()
        except Exception as e:
            MessageBox("OH NO 添加水印出了点问题~", "也许是你没输入图片或者保存的路径？没输入密码？"+str(e), self).exec()

    def Extract(self):
        try:
            if self.imgpwd.text() != "" and self.imgshape != "" and self.inimg != None:
                bwm = WaterMark(password_img=int(self.imgpwd.text()), password_wm=int(self.imgpwd.text()))
                wm_extract = bwm.extract(self.inimg, wm_shape=int(self.imgshape.text()), mode='str')
                self.imgwm.setText(wm_extract)
            else:
                MessageBox("OH NO 解密出了点问题~", "也许是你没输入图片?没输入密码和shape？", self).exec()
        except Exception as e:
            MessageBox("OH NO 解密出了点问题~", "也许是你没输入图片?没输入密码和shape？"+e, self).exec()
