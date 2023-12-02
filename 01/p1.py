#!/usr/bin/env python3
from aocd import get_data, submit
al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(sum([(lambda s: 10*int(s[0]) + int(s[-1]))(l.strip(al)) for l in get_data(day=1, year=2023).splitlines()]))



