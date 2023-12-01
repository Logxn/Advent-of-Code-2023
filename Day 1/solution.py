import re

PATTERN_ONE = r'\d'
PATTERN_TWO = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
NUMB_DICT = {"one": "1", "two": "2", "three": "3", "four": "4", "five":"5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def get_match(line, reverse=False, solution=1):
    if solution == 1:
        PATTERN = PATTERN_ONE
    else:
        PATTERN = PATTERN_TWO

    if reverse:
        for i in range(len(line), -1, -1):
            sub_str = line[i:]
            matches = re.findall(PATTERN, sub_str)

            if len(matches) == 0:
                continue

            if not matches[0].isnumeric():
                return [NUMB_DICT[matches[0]], i]
            
            return [matches[0], i]
    else:
        for i in range(len(line)):
            sub_str = line[:i]
            matches = re.findall(PATTERN, sub_str)

            if len(matches) == 0:
                continue
            
            if not matches[0].isnumeric():
                return [NUMB_DICT[matches[0]], i]
            
            return [matches[0], i]

with open('input.txt', 'r') as f:
    lines = f.readlines()

solution = 0

for line in lines:
    first_match = get_match(line)
    last_match = get_match(line, reverse=True)

    if first_match[1] == last_match[1]:
        solution += int(first_match[0] + last_match[0])
        continue
    
    solution += int(first_match[0] + last_match[0])

assert(solution == 55621)

solution_two = 0

for line in lines:
    first_match = get_match(line, solution=2)
    last_match = get_match(line, reverse=True, solution=2)
    
    if first_match[1] == last_match[1]:
        solution_two += int(first_match[0] + last_match[0])
        continue

    solution_two += int(first_match[0] + last_match[0])

assert(solution_two == 53592)    