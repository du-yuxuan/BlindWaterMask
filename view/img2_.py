from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QAction, QFileDialog

from qfluentwidgets import RoundMenu, FluentIcon, MessageBox, MessageDialog

from blind_watermark import bw_notes
from blind_watermark import WaterMark
import cv2

from view.img2_ui import Ui_Img2_UI


class Img2(Ui_Img2_UI, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        bw_notes.close()

        self.setupUi(self)

        self.inimg = None
        self.inimg2 = None
        self.outimg = None

        self.menu = RoundMenu(parent=self)
        embed_action = QAction(FluentIcon.RIGHT_ARROW.icon(), '添加水印')
        embed_action.triggered.connect(self.Embed)
        extract_action = QAction(FluentIcon.LEFT_ARROW.icon(), '提取水印')
        extract_action.triggered.connect(self.Extract)
        self.menu.addAction(embed_action)
        self.menu.addAction(extract_action)
        self.img2buuton.setMenu(self.menu)

        self.img2input1.clicked.connect(self.loadimg)
        self.img2input2_2.clicked.connect(self.loadimg2)
        self.img2input3.clicked.connect(self.saveimg)

    def loadimg(self):
        f = QFileDialog()
        f.setFileMode(QFileDialog.ExistingFile)
        f.setNameFilter('图片文件(*.jpg *.png *.bmp *.jpeg)')
        if f.exec():
            self.inimg = f.selectedFiles()[0]

    def loadimg2(self):
        f = QFileDialog()
        f.setFileMode(QFileDialog.ExistingFile)
        f.setNameFilter('图片文件(*.jpg *.png *.bmp *.jpeg)')
        if f.exec():
            self.inimg2 = f.selectedFiles()[0]

    def saveimg(self):
        d = QFileDialog.getExistingDirectory(None, "选择文件夹路径")
        self.outimg = d + "/output.png"

    def Embed(self):
        try:
            if self.img2pwd.text() != "" and self.inimg != None and self.inimg2 != None and self.outimg != None:
                bwm = WaterMark(password_img=int(self.img2pwd.text()), password_wm=int(self.img2pwd.text()))
                bwm.read_img(self.inimg)
                bwm.read_wm(self.inimg2)
                bwm.embed(self.outimg)
                wm_shape = cv2.imread(self.inimg2, flags=cv2.IMREAD_GRAYSCALE).shape
                self.img2shape.setText(str(wm_shape[0])+"|"+str(wm_shape[1]))
            else:
                MessageBox("OH NO 添加水印出了点问题~", "也许是你没输入图片或者保存的路径？没输入密码？", self).exec()
        except Exception as e:
            MessageBox("OH NO 添加水印出了点问题~", "也许是你没输入图片或者保存的路径？没输入密码？" + str(e),
                       self).exec()

    def Extract(self):
        try:
            if self.img2pwd.text() != "" and self.img2shape.text() != "" and self.inimg != None and self.outimg != None:
                bwm = WaterMark(password_img=int(self.img2pwd.text()), password_wm=int(self.img2pwd.text()))
                bwm.extract(self.inimg, wm_shape=[int(self.img2shape.text().split("|")[0]),
                                                  int(self.img2shape.text().split("|")[1])], out_wm_name=self.outimg,
                            mode='img')
            else:
                MessageBox("OH NO 解密出了点问题~", "也许是你没输入图片?没输入密码和shape？", self).exec()
        except Exception as e:
            MessageBox("OH NO 解密出了点问题~", "也许是你没输入图片?没输入密码和shape？" + e, self).exec()
