#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
get_conf = CiscoConfParse('cisco_ipsec.txt')
transform= get_conf.find_objects(r'^crypto ipsec')
for line in transform:
    if 'AES' not in line.text:
        print line.text


