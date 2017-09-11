#!/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'


from PySide import QtGui
from .check_dialog import CheckerDialog
from .singleton_decoration import  singleton
import sys

@singleton
class MainWindow(object):
    def __init__(self, config=''):
        self.app = QtGui.QApplication.instance()
        if not self.app:
            print("Starting new QApplication.....")
            self._app = QtGui.QApplication(sys.argv)
        self.window = CheckerDialog(parent=QtGui.QApplication.activeWindow(), config=config)

    def show(self):
        self.window.show()
        if not self.app:
            self._app.exec_()

    def register_next_cmd(self, cmd):
        self.window.register_next_cmd(cmd)


class WinShotgun(object):
    def __init__(self, sgtk):
        self._sgtk = sgtk

    def show(self):
        config = self._sgtk.get_setting("checker_config")
        self.window = CheckerDialog(parent=QtGui.QApplication.activeWindow(), config=config)
        self.window.register_next_cmd(self._cmd)
        self.window.show()

    def register_next_cmd(self, cmd):
        self._cmd = cmd


