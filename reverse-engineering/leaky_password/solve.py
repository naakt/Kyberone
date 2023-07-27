#!/usr/bin/env python3

import sys
import marshal
import dis
import time
from pwn import *

print(sys.version)
context.log_level='error'

winning_str = ["a"]*8

def explore_dis():
    with open( "chall.pyc","rb") as ff:
         ff.seek(16)
         print(dis.dis(marshal.load(ff)))
explore_dis()

for j in range(8):
    local_max = -1
    index = -1
    for i in range(48,58):
        tmp = winning_str[j]
        winning_str[j] = chr(i)
        intit = time.time()
        p = process(['python3.10',"source.py","-i",''.join(winning_str),"-m 1"])
        resp=p.recvline(4096)
        elapse = time.time()
        delta = elapse-intit
        print(delta, chr(i), resp)
        if delta > local_max:
            local_max = delta
        else:
            winning_str[j] = tmp
        p.close()
    print(local_max,index, winning_str)   
print(''.join(winning_str))

