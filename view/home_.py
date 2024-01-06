from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QPixmap,QPainter,QColor
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import setTheme, Theme

from view.home_ui import Ui_Home_UI

class Home(Ui_Home_UI,QWidget):
    def __init__ (self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)