#/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'



class Checker():
    def scan(self, select=0):
        """
        扫描场景并返回结果数据，数据为空则检查通过
        数据结果为字典，且字典的键值对的键为节点名字，值为列表，即{nodeName1:[...], ...}
        """
        self.data_dict = {}
        
        pass

        return self.data_dict


    def solve(self):
        """
        根据扫描数据自动修复，如果配置文件auto属性为True则次方法要实现
        """
        pass

    def select(self, obj):
        """
        选择：返回UI错误列表中的选择项名字，即self.data_dict的键。
        单选返回字符串（名字），多选返回列表（名字列表）
        请根据实际检查项实现次方法
        """
        pass
