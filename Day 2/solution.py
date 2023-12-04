# By definition a game is impossible, if a bag contains more than
# 12 reds, 13 greens and 14 blues
def is_possible(game_info):
    max_countings = {'red': 12, 'green': 13, 'blue': 14}

    bags = game_info[1].split('; ')
    for bag in bags:
        draws = bag.split(', ')
        
        for draw in draws:
            draw_info = draw.split(' ')
            color = draw_info[1].replace('\n', '')
            amount = draw_info[0]
            
            if int(amount) > max_countings[color]:
                return False
    return True

# This is for part II of the challenge
# We have to find the max occurence of a each color in a round
# 
# Example: Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Answer: Green: 13, Red: 20, Blue: 6
# 
# The power is the multiplication of the color values (e.g. 13 * 20 * 6)           
def get_power(game_info):
    bags = game_info[1].split('; ')
    countings = {'red': 0, 'green': 0, 'blue': 0}

    for bag in bags:
        draws = bag.split(', ')
        
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
    
    # Solution for part II is the sum of the power of each game
    solution_two += get_power(game_info)

    if not is_possible(game_info):
        continue

    # Solution for part I ist the sum of each possible game_id
    solution += int(game_id)

assert(solution == 2447)
assert(solution_two == 56322)

print(solution)
print(solution_two)