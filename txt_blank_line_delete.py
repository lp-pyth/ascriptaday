# -*- coding: utf-8 -*-
"""
Get white lines out of .txt
@author: lux
"""

recipe = r'PATHTOFILE'

with open(recipe) as f:
    print ("".join(line for line in f if not line.isspace()))