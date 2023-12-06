import regex as re

SPECIAL_CHARS = ['*', '#', '+', '$', "%", "@", "=", "/", "&", "-"]

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
                solution += int(match)
                continue

        if line[end] in SPECIAL_CHARS:
            solution += int(match)
            continue

        if i - 1 > 0:
            new_line = lines[i - 1]
            sub_start = start - 1
            sub_end = sub_start + len(match) + 2

            sub_str = new_line[sub_start:sub_end]

            if len([x for x in sub_str if x in SPECIAL_CHARS]) > 0:
                solution += int(match)
                continue
        
        if i + 1 < len(lines) - 1:
            new_line = lines[i + 1]
            sub_start = start - 1 if start > 0 else 0
            sub_end = sub_start + len(match) + 2

            sub_str = new_line[sub_start:sub_end]

            print(f'Match: {match} - {sub_str}')
            if len([x for x in sub_str if x in SPECIAL_CHARS]) > 0:
                solution += int(match)
                continue

print(solution)
assert(solution == 528819)