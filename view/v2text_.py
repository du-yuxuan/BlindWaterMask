from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QAction

from view.v2text_ui import Ui_V2text_UI

from qfluentwidgets import RoundMenu, FluentIcon, MessageBox, MessageDialog

from text_blind_watermark import TextBlindWatermark


class V2text(Ui_V2text_UI,QWidget):
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
        self.v2button.setMenu(self.menu)

    def Embed(self):
        try:

            text_blind_wm = TextBlindWatermark(password=self.v2pwd.text())
            text_blind_wm.read_wm(watermark=self.v2wm.text())
            text_blind_wm.read_text(text=self.v2text.toPlainText())
            self.v2text.setPlainText(text_blind_wm.embed())
        except:
            MessageBox("OH NO 加密出了点问题~", "也许是你没输入密文或者明文？\n也可能是明文的字数不足密文长度的16倍呢~", self).exec()

    def Extract(self):
        try:
            text_blind_wm = TextBlindWatermark(password=self.v2pwd.text())
            wm_extract = text_blind_wm.extract(text_embed=self.v2text.toPlainText())
            self.v2wm.setText(wm_extract)
        except:
            MessageBox("OH NO 解密出了点问题~", "也许是你的密码出错了~\n也可能是字太多了,电脑忙不过来了~", self).exec()

