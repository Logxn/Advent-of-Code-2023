max_countings = {'red': 12, 'green': 13, 'blue': 14}

with open('input.txt', 'r') as f:
    games = f.readlines()

solution = 0

for game in games:
    game_info = game.split(': ')
    game_id = game_info[0].split(' ')[1]
    
    is_possible = True

    rounds = game_info[1].split('; ')
    for round in rounds:
        draws = round.split(', ')
        
        for draw in draws:
            draw_info = draw.split(' ')
            color = draw_info[1]
            amount = draw_info[0]
            
            if int(amount) > max_countings[color.replace('\n', '')]:
                is_possible = False
                break
        
        if not is_possible:
            break

    if not is_possible:
        continue

    solution += int(game_id)

print(solution)