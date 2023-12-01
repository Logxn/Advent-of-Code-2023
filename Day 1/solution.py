import re

# I am to stupid for regex - don't hate me
PATTERN_ONE = r'\d'
PATTERN_TWO = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
NUMB_DICT = {"one": "1", "two": "2", "three": "3", "four": "4", "five":"5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# We want to get the first and last number
# For solution two we also have to consider number words like 'one'
# Because we can have overlapping numbers 'eightwothree'
# we scan the line from the beginning until we hit the first number and
# scan the line from the end backwards until we hit the first number

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
                return NUMB_DICT[matches[0]]
            
            return matches[0]
    else:
        for i in range(len(line)):
            sub_str = line[:i]
            matches = re.findall(PATTERN, sub_str)

            if len(matches) == 0:
                continue
            
            if not matches[0].isnumeric():
                return NUMB_DICT[matches[0]]
            
            return matches[0]

with open('input.txt', 'r') as f:
    lines = f.readlines()

solution = 0

for line in lines:
    first_match = get_match(line)
    last_match = get_match(line, reverse=True)

    solution += int(first_match + last_match)

assert(solution == 55621)

solution_two = 0

for line in lines:
    first_match = get_match(line, solution=2)
    last_match = get_match(line, reverse=True, solution=2)
    
    solution_two += int(first_match + last_match)

assert(solution_two == 53592)    