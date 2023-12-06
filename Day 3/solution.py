import regex as re
import math
from collections import defaultdict

SPECIAL_CHARS = ['*', '#', '+', '$', "%", "@", "=", "/", "&", "-"]
dic = defaultdict(list)


with open('input.txt', 'r') as f:
    lines = f.readlines()

solution = 0

for i, line in enumerate(lines):
    possible_matches = re.finditer(r'\d+', line)
    
    for possible_match in possible_matches:
        match = possible_match.group()
        start = possible_match.start()
        end = possible_match.end()

        if possible_match.start() > 0:
            if line[start - 1] in SPECIAL_CHARS:
                if line[start - 1] == '*':
                    dic[(i, start - 1)].append(int(match))
                solution += int(match)
                continue

        if line[end] in SPECIAL_CHARS:
            if line[end] == '*':
                dic[(i, end)].append(int(match))
            solution += int(match)
            continue

        if i - 1 > 0:
            new_line = lines[i - 1]
            sub_start = start - 1 if start - 1 > 0 else 0
            sub_end = sub_start + len(match) + 2

            sub_str = new_line[sub_start:sub_end]

            if len([x for x in sub_str if x in SPECIAL_CHARS]) > 0:
                if '*' in sub_str:
                    gear_pos = sub_start + sub_str.rfind('*')
                    dic[(i - 1, gear_pos)].append(int(match))

                solution += int(match)
                continue
        
        if i + 1 < len(lines) - 1:
            new_line = lines[i + 1]
            sub_start = start - 1 if start > 0 else 0
            sub_end = sub_start + len(match) + 2

            sub_str = new_line[sub_start:sub_end]

            if len([x for x in sub_str if x in SPECIAL_CHARS]) > 0:
                if '*' in sub_str:
                    gear_pos = sub_start + sub_str.rfind('*')
                    dic[(i + 1, gear_pos)].append(int(match))

                solution += int(match)
                continue

print(solution)
assert(solution == 528819)

solution_two = 0

for val in dic.values():
    if len(val) > 1:
        solution_two += math.prod(val)

print(solution_two)
assert(solution_two == 80403602)