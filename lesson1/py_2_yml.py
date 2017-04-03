#!/usr/bin/env python

import yaml
import pprint
a = range(10)
a.append('primul_string')
a.append('al_doile_string')
a.append({})
a.append({})
a[-2]['ip_address'] = '1.1.1.1'
a[-2]['device_type'] = 'juniper'
a[-1]['username'] = 'Juniper'
a[-1]['password'] = 'Junos123'
with open('py_2_yml.yml', 'w') as f:
    f.write(yaml.dump(a, default_flow_style=False))

