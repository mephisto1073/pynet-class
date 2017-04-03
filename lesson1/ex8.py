#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse('cisco_ipsec.txt')
CRYPTO = cisco_cfg.find_objects(r'^crypto map CRYPTO')
for i,v in enumerate(CRYPTO):
    print v.text
    for child in CRYPTO[i].children:
        print child.text
