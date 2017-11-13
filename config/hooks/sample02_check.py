#/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'



class Checker():
    def scan(self, select=0):
        """
        扫描场景并返回结果数据，数据为空则检查通过
        data数据结果为字典，且字典的键值对的键为节点名字，值一般为节点的出错属性等信息数据，即{nodeName1:nodeAttrInfo, ...}
        Returns:
            [True data, info]     错误！中断检查，如果给定info将会显示info信,并在界面的错误列表中列出错误结果数据data. (有数据)
            [True, False, info]   错误！中断检查，如果给定info将会显示info信息。 （无错误数据，如：空场景，没有检查的数据）
            [False, info]         跳过！不会中断继续检查其他项，等检查完由用户决定是否修改，如果给定info将会显示info信息
            False                 检查通过

        """
        self.data_dict = {}

        return [1, {'aaa':111111}, u'啊啊啊']
        # return [1, 0, u'场景中还没有任何物体！']


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
