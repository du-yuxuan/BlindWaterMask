from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QAction, QFileDialog

from qfluentwidgets import RoundMenu, FluentIcon, MessageBox, MessageDialog

from blind_watermark import bw_notes
from blind_watermark import WaterMark

import cv2
import numpy as np

from view.imgresize_ui import Ui_Ui_Resize_UI


class Imgresize(Ui_Ui_Resize_UI, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)

        self.inimg = None
        self.outimg = None

        self.resizein.clicked.connect(self.loadimg)
        self.resizeout.clicked.connect(self.saveimg)
        self.resizebutton.clicked.connect(self.iresize)

    def loadimg(self):
        f = QFileDialog()
        f.setFileMode(QFileDialog.ExistingFile)
        f.setNameFilter('图片文件(*.jpg *.png *.bmp *.jpeg)')
        if f.exec():
            self.inimg = f.selectedFiles()[0]

    def saveimg(self):
        d = QFileDialog.getExistingDirectory(None, "选择文件夹路径")
        self.outimg = d + "/output.png"

    def iresize(self):
        img = cv2.imdecode(np.fromfile(self.inimg, dtype=np.uint8), -1)
        f = 100/((np.shape(img)[0]+np.shape(img)[1])/2)

        img = cv2.resize(img, (0, 0), fx=f, fy=f)  # 按比例缩放

        cv2.imencode('.png', img)[1].tofile(self.outimg)

