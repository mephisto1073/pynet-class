#!/usr/bin/env python
import re
from ciscoconfparse import CiscoConfParse

get_conf = CiscoConfParse('cisco_ipsec.txt')
transform= get_conf.find_objects_wo_child(parentspec=r'crypto map', childspec=r'AES')
for line in transform:
    print line.text
    for child in line.children:
        if 'transform-set' in child.text:
            ts = re.search(r'transform-set (.*)', child.text).group(1)
            print ts    

