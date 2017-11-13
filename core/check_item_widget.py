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
        self._parent.output_info(u'>>> 开始检查： %s' % self._ui.check_name.text(), color=self._parent._run_color)
        self._parent.current_uuid = self.uuid
        select_state = self._parent.get_select_state()
        result_data = self.checker.scan(select_state)
        self._parent.clear_error_info()
        if result_data:
            # 1.错误，中断
            if result_data[0]:
                data = result_data[1]
                self.set_state('error')
                self._parent.output_info(u'发现错误！',  color=self._parent._error_color)
                if data:
                    # a.发现错误，显示错误数据（有数据）
                    self._parent.error_node_collection(self, data)
                    if len(result_data)==3:
                        info_str = result_data[-1]
                        self._parent.output_info(info_str, color=self._parent._info_color, status=1)
                    if not self._data.get('auto'):
                        self._parent.output_info(u'该项不能自动修复呃，请手动修复吧！', color=self._parent._hint_color)
                    else:
                        self._parent.output_info(u'该项可以自动修复哦！', color=self._parent._hint_color)
                else:
                    # b.发现错误，不显示错误数据（无数据）
                    self._parent.clear_error_info()
                    info_str = result_data[-1]
                    if info_str:
                        self._parent.output_info(info_str, color=self._parent._info_color, status=1)
                    self._parent.output_info(u'请手动修复吧！',  color=self._parent._hint_color)
                return True
            # 2.忽略，继续（主要针对同一环节，不同类型资产，不如模型环节的set类型资产）
            else:
                self.set_state('skip')
                info_str = result_data[-1]
                if info_str:
                    self._parent.output_info(info_str, color=self._parent._info_color)
                self._parent.output_info(u'跳过检查！',  color=self._parent._hint_color)

                if not self._parent._batch:
                    if self.uuid not in self._parent.pass_list:
                        self._parent.pass_list.append(self.uuid)
                return False

            # self.set_state('error')
            # self._parent.output_info(u'Error（发现错误）！')
            # self._parent.error_node_collection(self, result_data)
            # if not self._data.get('auto'):
            #     self._parent.output_info(u'Can not be repaired automatically！Please manually solve！（该项不能自动修复呃，请手动修复吧！）')
            # else:
            #     self._parent.output_info(u'This can be repaired automatically！（该项可以自动修复哦！）')
            # return True
        else:
            self.set_state('pass')
            self._parent.output_info(u'检查通过！', color=self._parent._pass_color)
            if not self._parent._batch:
                if self.uuid not in self._parent.pass_list:
                    self._parent.pass_list.append(self.uuid)
            return False

    def on_solve_btn_clicked(self):
        """
        自动修复
        Returns:
        """
        self._parent.output_info(u'>>> 开始修复： %s' % self._ui.check_name.text(),  color=self._parent._run_color)
        self.checker.solve()
        self._parent.output_info(u'修复完成！开始修复后自检！',  color=self._parent._hint_color)
        data = self.on_scan_btn_clicked()
        if data:
            self._parent.output_info(u'修复失败，请联系TD ！',  color=self._parent._error_color)
            return True
        self._parent.output_info(u'修复成功！',  color=self._parent._pass_color)

    def on_skip_btn_clicked(self):
        """
        取消检查
        Returns:
        """
        self.close()
        self._parent.checker_uuid_list.remove(self.uuid)
        self._parent.output_info(u"取消检查： %s" % self._ui.check_name.text(),  color=self._parent._hint_color)

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
        elif state == 'skip':
            self._ui.state_icon.setPixmap(':/icons/warning.png')
            # self._ui.scan_btn.setVisible(0)
            # self._ui.solve_btn.setVisible(0)
            # self._ui.skip_btn.setVisible(0)

            self._ui.scan_btn.setVisible(1)
            self._ui.solve_btn.setVisible(self._data.get('auto'))
            self._ui.skip_btn.setVisible(self._data.get('skip'))

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