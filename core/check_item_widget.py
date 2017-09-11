#!/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'

from PySide import QtGui, QtCore
from .ui.check_item_widget import Ui_check_item_widget
import uuid
import sys

class CheckItemWidget(QtGui.QFrame):
    def __init__(self, parent=None, data=None):
        super(CheckItemWidget, self).__init__()
        self._ui = Ui_check_item_widget()
        self._ui.setupUi(self)
        self._parent = parent
        self._data = data
        self.uuid = str(uuid.uuid4().hex)
        self.setObjectName(self.uuid)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet("*{background:rgba(0,0,0,0);}QFrame::hover#%s{background:rgb(0,120,210);}" % self.uuid)

        # initialize connect
        self._ui.scan_btn.clicked.connect(self.on_scan_btn_clicked)
        self._ui.solve_btn.clicked.connect(self.on_solve_btn_clicked)
        self._ui.skip_btn.clicked.connect(self.on_skip_btn_clicked)

        self.data_init()

    def data_init(self):
        """
        初始化检查项数据
        Returns:
        """
        self._ui.check_name.setText(self._data.get('name'))
        checker_handler = self._data.get('handler')
        self._ui.solve_btn.setVisible(0)
        self._ui.skip_btn.setVisible(self._data.get('skip'))
        module = __import__(checker_handler)
        del sys.modules[checker_handler]
        module = __import__(checker_handler)
        self.checker = module.Checker()
        # self.width() > self._parent._ui.left_area_frame.width()
        # print self.width()
        # print self._parent._ui.left_area_frame.width()
        # self._parent._ui.left_area_frame.setMinimumWidth(self.width())

    def on_scan_btn_clicked(self):
        """
        开始检查
        Returns: True则检查失败 False则检查通过
        """
        self._parent.output_info(u'>>> Checking（开始检查）： %s' % self._ui.check_name.text())
        self._parent.current_uuid = self.uuid
        select_state = self._parent.get_select_state()
        result_data = self.checker.scan(select_state)
        self._parent.clear_error_info()
        if result_data:
            self.set_state('error')
            self._parent.output_info(u'Error（发现错误）！')
            self._parent.error_node_collection(self, result_data)
            if not self._data.get('auto'):
                self._parent.output_info(u'Can not be repaired automatically！Please manually solve！（该项不能自动修复呃，请手动修复吧！）')
            else:
                self._parent.output_info(u'This can be repaired automatically！（该项可以自动修复哦！）')
            return True
        else:
            self.set_state('pass')
            self._parent.output_info(u'Check through！（检查通过！）')
            return False

    def on_solve_btn_clicked(self):
        """
        自动修复
        Returns:
        """
        self._parent.output_info(u'>>> Start repairing（开始修复）： %s' % self._ui.check_name.text())
        self.checker.solve()
        self._parent.output_info(u'Repair completed！self checking！（修复完成！开始修复后自检！）')
        data = self.on_scan_btn_clicked()
        if data:
            self._parent.output_info(u'Repair failed ！Please contact TD！（修复失败，请联系TD ！）')
            return True
        self._parent.output_info(u'Successful repair！（修复成功！）')

    def on_skip_btn_clicked(self):
        """
        取消检查
        Returns:
        """
        self.close()
        self._parent.checker_uuid_list.remove(self.uuid)
        self._parent.output_info(u">>> Cancle check（取消检查）： %s" % self._ui.check_name.text())

    def set_state(self, state='error'):
        """
        设置检查的结果状态
        Args:
            state: 结果状态
        Returns:
        """
        if state == 'wating':
            self._ui.state_icon.setPixmap(':/icons/clock.png')
        elif state == 'error':
            self._ui.state_icon.setPixmap(':/icons/failure.png')
            self._ui.scan_btn.setVisible(1)
            self._ui.solve_btn.setVisible(self._data.get('auto'))
            self._ui.skip_btn.setVisible(self._data.get('skip'))
        elif state == 'pass':
            self._ui.state_icon.setPixmap(':/icons/success.png')
            self._ui.scan_btn.setVisible(0)
            self._ui.solve_btn.setVisible(0)
            self._ui.skip_btn.setVisible(0)

    def mouseReleaseEvent(self, *event):
        """
        鼠标单击事件，点击会输出检查项的描述信息（配置文件实现），如果没有会输出该项的名字
        Args:
            *event:
        Returns:
        """
        description = self._data.get('description', None)
        if description:
            self._parent.output_info(description)
        else:
            self._parent.output_info(self._ui.check_name.text())


if __name__ == '__main__':
    app = QtGui.QApplication([])
    ciw = CheckItemWidget()
    ciw.show()
    app.exec_()