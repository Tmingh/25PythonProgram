#!/usr/bin/env python
# coding=utf-8
import hashlib

def create_md5_string(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'));
    return md5.hexdigest()

i = 0
codes = []
while(i < 200):
    str = 'activation code no: %d' %(i)
    codes.append(create_md5_string(str))
    i += 1

for code in codes:
    print(code)

