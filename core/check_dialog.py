#!/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'

from PySide import QtGui, QtCore
from .ui.check_dialog import Ui_check_dialog
from .ui import resources_rc
from .check_item_widget import CheckItemWidget
from .ui_style import STANDARD_STYLE
from .parse_yaml import parse_yaml_file
import sys
import os

class CheckerDialog(QtGui.QDialog):
    def __init__(self, parent=None, config=''):
        super(CheckerDialog, self).__init__(parent)
        self._ui = Ui_check_dialog()
        self._ui.setupUi(self)
        self.setWindowTitle('Checker')

        self._ui.error_node_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self._ui.error_node_list.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self.config = config
        self.next_cmd = None
        self.checker_item = {}
        self.checker_uuid_list = []
        self.current_uuid = None
        self._batch = False
        self.pass_list = []
        self.hooks_path = ''
        self.updata_cmd = QtGui.QApplication.instance().processEvents

        # connect
        self._ui.error_node_list.itemSelectionChanged.connect(self.on_error_node_list_selection_changed)
        self._ui.refresh_btn.clicked.connect(self.on_refresh_btn_clicked)
        self._ui.batch_run_btn.clicked.connect(self.on_batch_run_btn_clicked)
        self._ui.continue_btn.clicked.connect(self.on_continue_btn_clicked)
        self._ui.auto_check.stateChanged.connect(self.on_auto_check_state_changed)
        self._ui.check_seleted.stateChanged.connect(self.on_check_selected_state_changed)
        self._ui.cancle_btn.clicked.connect(self.close)
        self._ui.next_btn.clicked.connect(self.on_next_btn_clicked)


    def on_next_btn_clicked(self):
        """
        下一步按钮点击事件
        Returns:
        """
        if self.next_cmd:
            self.next_cmd()
            self.close()

    def register_next_cmd(self, cmd):
        """
        注册下一步按钮点击功能
        Args:
            cmd: 执行函数
        Returns:
        """
        self.next_cmd = cmd

    def on_auto_check_state_changed(self, state):
        """
        修复开关状态变更提示信息
        Args:
            state:
        Returns:
        """
        if state:
            self.output_info(u'Turn on（开启批量检查时自动修复功能）')
        else:
            self.output_info(u'Turn off（关闭批量检查时自动修复功能）')

    def on_check_selected_state_changed(self, state):
        """
        选择开关状态变更提示信息
        Args:
            state:
        Returns:
        """
        if state:
            self.output_info(u'Turn on（选择开启：检查选择的物体）')
        else:
            self.output_info(u'Turn off（选择关闭：检查整个场景）')

    def get_select_state(self):
        """
        获取选择开关状态
        Returns:
        """
        return self._ui.check_seleted.isChecked()

    def _init_checker_item(self, data):
        """
        实例化检查项
        Args:
            data: 单个检查项所需的字典数据，解析配置文件获得
        Returns: QtGui.QFrame
        """
        item = CheckItemWidget(self, data=data)
        self._ui.check_item_layout.addWidget(item)
        return item

    def _set_style(self):
        """
        设置风格
        Returns:
        """
        self.setStyleSheet(STANDARD_STYLE)
        self._ui.left_area_frame.setStyleSheet('QFrame#left_area_frame{border-right:1px solid rgb(20,20,20);}')
        self._ui.left_area_top_frame.setStyleSheet("""*{background:rgb(80,80,80)}
                                                QFrame#left_area_top_frame{border-bottom:1px solid rgb(20,20,20);}""")
        self._ui.right_area_top_frame.setStyleSheet("""*{background:rgb(80,80,80)}
                                                QFrame#right_area_top_frame{border-bottom:1px solid rgb(20,20,20);}""")
        self._ui.bottom_frame.setStyleSheet('QFrame#bottom_frame{border-top:1px solid rgb(20,20,20);}')
        self._ui.output_screen.setStyleSheet('background:rgb(40,40,40);')
        self._ui.splitter.setStyleSheet("QSplitter::handle{background:rgb(20,20,20);}")

    def on_batch_run_btn_clicked(self):
        """
        批量检查，如果有勾选“检查”复选框则会自动修复，直到遇到检查不通过且需手动修复的项中断
        Returns:
        """
        self._batch = True
        if not self.checker_uuid_list:
            self.output_info(u'No check item（没有检查项）！')
            return
        self.output_info(u'Batch checking （开始批量检查）......')
        self.pass_list = []

        for checker_uuid in self.checker_uuid_list:
            self.clear_error_info()
            item = self.checker_run(checker_uuid)
            if item:
                if self._ui.auto_check.isChecked() and item._data.get('auto'):
                    if item.on_solve_btn_clicked():
                        return
                else:
                    return
            self.pass_list.append(checker_uuid)
        self.current_uuid = None
        self._batch = False

    def on_continue_btn_clicked(self):
        """
        继续检查，接着上次中断的项开始，如果有勾选“检查”复选框则会自动修复，直到遇到检查不通过且需手动修复的项中断
        Returns:
        """
        if not self._batch:
            self.output_info(u'Must be batch check first! （仅用于批量检查中断时）！')
            return
        self.output_info(u'Continue checking （继续上次检查）......')
        for checker_uuid in self.checker_uuid_list:
            if checker_uuid in self.pass_list:
                continue
            self.clear_error_info()
            item = self.checker_run(checker_uuid)
            if item:
                if self._ui.auto_check.isChecked() and item._data.get('auto'):
                    if item.on_solve_btn_clicked():
                        return
                else:
                    return
            self.pass_list.append(checker_uuid)
        self.current_uuid = None
        self._batch = False

    def checker_run(self, checker_uuid):
        """
        获取检查项，并对该项进行检查
        Args:
            checker_uuid: 检查项uuid
        Returns: QtGui.QFrame
        """
        self.updata_cmd()
        item = self.checker_item.get(checker_uuid)
        # self.current_uuid = checker_uuid
        if item.on_scan_btn_clicked():
            return item

    def get_config_file(self):
        """
        解析配置文件地址
        Returns:
        """
        if os.path.isfile(self.config):
            return self.config
        else:
            config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', self.config)
            if os.path.isfile(config_path):
                return config_path.replace('\\', '/')

    def on_refresh_btn_clicked(self):
        """
        界面刷新重置，重载配置文件数据
        Returns:
        """
        config_file = self.get_config_file()
        if not config_file:
            self.output_info(u'Can not find config file！Please contact TD！（配置文件不存在，请联系TD解决！）')
            self.setEnabled(0)
            return
        self._refresh_ui()
        config_data = parse_yaml_file(config_file)
        if not config_data:
            self.output_info(u'Config error！Please contact TD！（配置文件错误！请联系TD解决！）')
            return
        self.hooks_path = self.get_hooks_path(config_data.get('hooks_path'))
        if not self.hooks_path:
            self.output_info(u'Config error！Please contact TD！（hooks_path 配置错误！请联系TD解决！）')
            self.setEnabled(0)
            return
        checker_actions = config_data.get('checker_actions')
        sys.path.append(self.hooks_path)
        for checker_data in checker_actions:
            item = self._init_checker_item(checker_data)
            self.checker_item[item.uuid] = item
            self.checker_uuid_list.append(item.uuid)

    def get_hooks_path(self, file_path):
        """
        解析hooks路径
        Args:
            file_path: 配置文件获得
        Returns:
        """
        if not file_path:
            hooks_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'hooks')
            return hooks_path.replace('\\', '/')
        if os.path.isdir(file_path):
            return file_path
        else:
            hooks_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'hooks', self.config)
            if os.path.isdir(hooks_path):
                return hooks_path.replace('\\', '/')
            else:
                return


    def _refresh_ui(self):
        """
        重置界面界面数据，界面刷新重载时调用
        Returns:
        """
        if self.hooks_path in sys.path:
            sys.path.remove(self.hooks_path)
        self._clear_checker_list()
        self.pass_list = []
        self.checker_item = {}
        self.checker_uuid_list = []
        self.current_uuid = None
        self._batch = False
        self.hooks_path = ''
        self._ui.error_node_list.clear()
        self._ui.output_screen.clear()
        self.set_counter(0)
        self._ui.next_btn.setVisible(0)

    def _clear_checker_list(self):
        """
        清空检查项列表，界面刷新重载时调用
        Returns:
        """
        if not self.checker_uuid_list:
            return
        for checker_uuid in self.checker_uuid_list:
            item = self.checker_item.get(checker_uuid)
            try:
                item.close()
                self._ui.check_item_layout.removeWidget(item)
            except:pass

    def on_error_node_list_selection_changed(self):
        """
        节点列表的选择事件，选择列表中的项，会在场景中选择对应的节点，可多选
        Returns:
        """
        item_list = self._ui.error_node_list.selectedItems()
        if not item_list:
            return
        checker_item = self.checker_item[self.current_uuid]
        checker = checker_item.checker
        if len(item_list) == 1:
            node_name = item_list[0].text()
            attr_list = self.error_dict.get(node_name)
            self.output_info(str(attr_list))
            checker.select([node_name])
        else:
            node_list = []
            for item in item_list:
                node_list.append(item.text())
            checker.select(node_list)

    def set_counter(self, num):
        """
        设置计数器，用于统计单项检查的错误节点个数，界面重置及单项检查时调用
        Args:
            num: 错误节点数量
        Returns:
        """
        self._ui.counter_label.setText('Error  (%s)' % str(num))

    def clear_error_info(self):
        """
        清空错误列表数据，复原计数器, 单项检查开始前调用，清理数据
        Returns:
        """
        self._ui.error_node_list.clear()
        self.set_counter(0)

    def error_node_collection(self,item, error_data):
        """
        单项检查的错误节点处理呈现
        Args:
            item: 检查项
            error_data: 错误数据
        Returns:
        """
        self.clear_error_info()
        self.error_dict = error_data
        counter = 0
        for error_node in self.error_dict:
            counter += 1
            self._ui.error_node_list.addItem(error_node)
            self.set_counter(counter)
            self.updata_cmd()

    def output_info(self, text):
        """
        信息反馈输出，便于制作人员对检查状态的了解
        Args:
            text: 反馈输出的信息
        Returns:
        """
        self._ui.output_screen.appendPlainText(text)
        self._ui.output_screen.moveCursor(QtGui.QTextCursor.End)

    def showEvent(self, event):
        """
        界面显示的时候根据设置重置界面
        Args:
            event:
        Returns:
        """
        self._set_style()
        self._ui.splitter.handle(1).moveSplitter(150)
        self.setEnabled(1)
        self.on_refresh_btn_clicked()
        # if not self.next_cmd:
        #     try:
        #         import tank
        #         self.next_cmd = tank.platform.current_engine().commands['Publish...']['callback']
        #     except:
        #         self.next_cmd = None
        super(CheckerDialog, self).showEvent(event)

    def closeEvent(self, event):
        """
        关闭界面的时候讲hooks路径从系统路径里面移除掉
        Args:
            event:
        Returns:
        """
        if self.hooks_path in sys.path:
            sys.path.remove(self.hooks_path)
        # sys.modules.clear()
        super(CheckerDialog, self).closeEvent(event)

    def event(self, event):
        """
        监测是否显示publish按钮
        Args:
            event:
        Returns:
        """
        if hasattr(self, 'checker_uuid_list'):
            if self.checker_uuid_list and self.pass_list and self.next_cmd:
                self._ui.next_btn.setVisible(set(self.checker_uuid_list).issubset(self.pass_list))
            super(CheckerDialog, self).event(event)
        return False



if __name__ == '__main__':
    app = QtGui.QApplication([])
    PD = CheckerDialog()
    PD.show()
    app.exec_()

