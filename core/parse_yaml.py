#!/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'

import yaml

def parse_yaml_file(file_path):
    data = None
    with open(str(file_path)) as f:
        data = yaml.load(f)
    return data
