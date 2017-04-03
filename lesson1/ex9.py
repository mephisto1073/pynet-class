#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
get_conf = CiscoConfParse('cisco_ipsec.txt')
group2 = get_conf.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'set pfs group2')
for entry in group2:
    print entry.text


