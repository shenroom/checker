#/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'



class Checker():
    def scan(self, select=0):
        """
        扫描场景并返回结果数据，数据为空则检查通过
        data数据结果为字典，且字典的键值对的键为节点名字，值为列表，即{nodeName1:[...], ...}
        Returns:
            [True data]           错误！中断检查，并列出错误结果数据data. (有数据)
            [True, False, info]   错误！中断检查，如果给定info将会显示info信息。 （无错误数据，如：空场景，没有检查的数据）
            [False, info]         跳过！继续检查其他项，如果给定info将会显示info信息
            False                 检查通过！
        """
        self.data_dict = {}
        
        pass

        return #[0, u'不是set类型，跳过该项检查!']


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
