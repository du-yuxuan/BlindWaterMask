from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QAction

from view.v1text_ui import Ui_V1text_UI

from qfluentwidgets import RoundMenu, FluentIcon, MessageBox, MessageDialog

from text_blind_watermark import TextBlindWatermarkThin

class V1text(Ui_V1text_UI,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.menu = RoundMenu(parent=self)
        embed_action = QAction(FluentIcon.RIGHT_ARROW.icon(), '加密')
        embed_action.triggered.connect(self.Embed)
        extract_action = QAction(FluentIcon.LEFT_ARROW.icon(), '解密')
        extract_action.triggered.connect(self.Extract)
        self.menu.addAction(embed_action)
        self.menu.addAction(extract_action)
        self.v1button.setMenu(self.menu)

    def Embed(self):
        text_blind_wm = TextBlindWatermarkThin(password=self.v1pwd.text())
        wm = text_blind_wm.embed(watermark=self.v1wm.text())
        text_embed = self.v1front.text() + wm + self.v1back.text()
        self.v1embed.setPlainText(text_embed)

    def Extract(self):
        try:
            text_blind_wm = TextBlindWatermarkThin(password=self.v1pwd.text())
            wm_extract = text_blind_wm.extract(text_embed=self.v1embed.toPlainText())
            wm = text_blind_wm.embed(watermark=wm_extract)
            s = self.v1embed.toPlainText().split(wm)
            self.v1front.setText(s[0])
            self.v1back.setText(s[1])
            self.v1wm.setText(wm_extract)
        except:
            MessageBox("OH NO 解密出了点问题~", "也许是你的密码出错了~\n也可能是字太多了,电脑忙不过来了~", self).exec()




