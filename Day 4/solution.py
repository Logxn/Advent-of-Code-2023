with open('input.txt', 'r') as f:
    lines = f.readlines()

def get_winning_numbers(decks):
    winning_numbers =  decks[0].split()
    my_numbers =  decks[1].split()

    matching_numbers = [i for i in winning_numbers if i in my_numbers]

    if len(matching_numbers) == 0:
        return 0
    
    return len(matching_numbers)



solution = 0
solution_two = len(lines)

for i, line in enumerate(lines):
    decks = line.split(': ')[1].split(' | ')
   
    winnings = get_winning_numbers(decks)

    if winnings == 0:
        continue

    solution += 1 * pow(2, winnings - 1)
    

print(solution)
assert(solution == 24733)