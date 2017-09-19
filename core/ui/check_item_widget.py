# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core\resources\check_item_widget.ui'
#
# Created: Tue Sep 19 11:26:48 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_check_item_widget(object):
    def setupUi(self, check_item_widget):
        check_item_widget.setObjectName("check_item_widget")
        check_item_widget.resize(495, 34)
        self.verticalLayout = QtGui.QVBoxLayout(check_item_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(check_item_widget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.state_icon = QtGui.QLabel(self.frame)
        self.state_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.state_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.state_icon.setText("")
        self.state_icon.setPixmap(QtGui.QPixmap(":/icons/clock.png"))
        self.state_icon.setScaledContents(True)
        self.state_icon.setObjectName("state_icon")
        self.horizontalLayout.addWidget(self.state_icon)
        self.check_name = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.check_name.setFont(font)
        self.check_name.setObjectName("check_name")
        self.horizontalLayout.addWidget(self.check_name)
        spacerItem = QtGui.QSpacerItem(560, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.scan_btn = QtGui.QToolButton(self.frame)
        self.scan_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/play_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.scan_btn.setIcon(icon)
        self.scan_btn.setAutoRaise(True)
        self.scan_btn.setObjectName("scan_btn")
        self.horizontalLayout.addWidget(self.scan_btn)
        self.solve_btn = QtGui.QToolButton(self.frame)
        self.solve_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/correct.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.solve_btn.setIcon(icon1)
        self.solve_btn.setAutoRaise(True)
        self.solve_btn.setObjectName("solve_btn")
        self.horizontalLayout.addWidget(self.solve_btn)
        self.skip_btn = QtGui.QToolButton(self.frame)
        self.skip_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/clear_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.skip_btn.setIcon(icon2)
        self.skip_btn.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.skip_btn.setAutoRaise(True)
        self.skip_btn.setArrowType(QtCore.Qt.NoArrow)
        self.skip_btn.setObjectName("skip_btn")
        self.horizontalLayout.addWidget(self.skip_btn)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(check_item_widget)
        QtCore.QMetaObject.connectSlotsByName(check_item_widget)

    def retranslateUi(self, check_item_widget):
        check_item_widget.setWindowTitle(QtGui.QApplication.translate("check_item_widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.check_name.setText(QtGui.QApplication.translate("check_item_widget", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.scan_btn.setToolTip(QtGui.QApplication.translate("check_item_widget", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">开始检查</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.solve_btn.setToolTip(QtGui.QApplication.translate("check_item_widget", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">自动修改</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.skip_btn.setToolTip(QtGui.QApplication.translate("check_item_widget", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">取消检查</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
