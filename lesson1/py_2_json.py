#!/usr/bin/env python

import json
import pprint
a = range(10)
a.append('first_string')
a.append('second_string')
a.append({})
a.append({})
a[-2]['ip_address'] = '10.10.10.10'
a[-2]['device_type'] = 'cisco_ios'
a[-1]['username'] = 'cisco_admin'
a[-1]['password'] = 'cisco123'
with open('py_2_json.json', 'w') as f:
    json.dump(a, f)






