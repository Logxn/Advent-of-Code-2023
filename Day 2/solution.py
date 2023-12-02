max_countings = {'red': 12, 'green': 13, 'blue': 14}

def is_possible(game_info):
    rounds = game_info[1].split('; ')
    for round in rounds:
        draws = round.split(', ')
        
        for draw in draws:
            draw_info = draw.split(' ')
            color = draw_info[1]
            amount = draw_info[0]
            
            if int(amount) > max_countings[color.replace('\n', '')]:
                return False
    return True
            
def get_power(game_info):
    rounds = game_info[1].split('; ')
    countings = {'red': 0, 'green': 0, 'blue': 0}

    for round in rounds:
        draws = round.split(', ')
        
        for draw in draws:
            draw_info = draw.split(' ')
            color = draw_info[1].replace('\n', '')
            amount = int(draw_info[0])

            if amount > countings[color]:
                countings[color] = amount
    
    power = 1
    for color in countings:
        power *= countings[color]

    return power

with open('input.txt', 'r') as f:
    games = f.readlines()

solution = 0
solution_two = 0

for game in games:
    game_info = game.split(': ')
    game_id = game_info[0].split(' ')[1]
    
    solution_two += get_power(game_info)

    if not is_possible(game_info):
        continue

    solution += int(game_id)

print(solution)
assert(solution == 2447)

print(solution_two)