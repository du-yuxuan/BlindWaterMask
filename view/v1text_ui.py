# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1text_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_V1text_UI(object):
    def setupUi(self, V1text_UI):
        V1text_UI.setObjectName("V1text_UI")
        V1text_UI.resize(469, 406)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(V1text_UI)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.TitleLabel = TitleLabel(V1text_UI)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)
        self.BodyLabel = BodyLabel(V1text_UI)
        self.BodyLabel.setObjectName("BodyLabel")
        self.verticalLayout.addWidget(self.BodyLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.v1button = DropDownPushButton(V1text_UI)
        self.v1button.setObjectName("v1button")
        self.verticalLayout_2.addWidget(self.v1button)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CaptionLabel_2 = CaptionLabel(V1text_UI)
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.horizontalLayout_5.addWidget(self.CaptionLabel_2)
        self.v1pwd = LineEdit(V1text_UI)
        self.v1pwd.setObjectName("v1pwd")
        self.horizontalLayout_5.addWidget(self.v1pwd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CaptionLabel = CaptionLabel(V1text_UI)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.horizontalLayout.addWidget(self.CaptionLabel)
        self.v1wm = LineEdit(V1text_UI)
        self.v1wm.setObjectName("v1wm")
        self.horizontalLayout.addWidget(self.v1wm)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.v1front = LineEdit(V1text_UI)
        self.v1front.setObjectName("v1front")
        self.horizontalLayout_3.addWidget(self.v1front)
        self.CaptionLabel_3 = CaptionLabel(V1text_UI)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.horizontalLayout_3.addWidget(self.CaptionLabel_3)
        self.v1back = LineEdit(V1text_UI)
        self.v1back.setObjectName("v1back")
        self.horizontalLayout_3.addWidget(self.v1back)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CaptionLabel_4 = CaptionLabel(V1text_UI)
        self.CaptionLabel_4.setObjectName("CaptionLabel_4")
        self.verticalLayout_3.addWidget(self.CaptionLabel_4)
        self.v1embed = TextEdit(V1text_UI)
        self.v1embed.setObjectName("v1embed")
        self.verticalLayout_3.addWidget(self.v1embed)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.retranslateUi(V1text_UI)
        QtCore.QMetaObject.connectSlotsByName(V1text_UI)

    def retranslateUi(self, V1text_UI):
        _translate = QtCore.QCoreApplication.translate
        V1text_UI.setWindowTitle(_translate("V1text_UI", "Form"))
        self.TitleLabel.setText(_translate("V1text_UI", "文字盲水印 V1"))
        self.BodyLabel.setText(_translate("V1text_UI", "<html><head/><body><p><span style=\" font-size:8pt;\">密文变得不可见为暗文并嵌入到文本之间后的文本中就是明文</span></p></body></html>"))
        self.v1button.setText(_translate("V1text_UI", "加密/解密"))
        self.CaptionLabel_2.setText(_translate("V1text_UI", "密码"))
        self.CaptionLabel.setText(_translate("V1text_UI", "密文"))
        self.CaptionLabel_3.setText(_translate("V1text_UI", "+暗文+"))
        self.CaptionLabel_4.setText(_translate("V1text_UI", "=明文"))
from qfluentwidgets import BodyLabel, CaptionLabel, DropDownPushButton, LineEdit, TextEdit, TitleLabel
