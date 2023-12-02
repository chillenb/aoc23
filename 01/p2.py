#!/usr/bin/env python3
from aocd import get_data, submit
from num2words import num2words
import re
fwd = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
back = re.compile(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin')
dmap = {num2words(i) : i for i in range(1, 10)}
dmap.update({str(i) : i for i in range(1, 10)})
def process(line):
    return dmap[fwd.search(line).group()]*10 + dmap[back.search(line[::-1]).group()[::-1]]
submit(sum([process(l) for l in get_data(day=1, year=2023).splitlines()]), day=1, year=2023, part='b')
