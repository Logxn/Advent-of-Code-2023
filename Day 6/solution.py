with open('input.txt', 'r') as f:
    lines = f.readlines()

times = lines[0].split()
distances = lines[1].split()

possibilities = {1: 0, 2: 0, 3: 0, 4: 0}

for i in range(1, len(times)):
    time = int(times[i])
    distance = int(distances[i])

    for j in range(1, time + 1):
        speed = j
        time_left = time - j
        distance_traveled = speed * time_left

        if(distance_traveled > distance):
            possibilities[i] += 1

solution = 1
for value in possibilities.values():
    solution *= value

print(solution)
assert(solution == 2756160)

# The values for time and distance below are different for you!
# Probably a smarter and faster calculation method.
# Frankly I dont care :^)
solution_two = 0
time = 48938595
distance = 296192812361391

for i in range(1, time + 1):
    speed = i
    time_left = time - i
    distance_traveled = speed * time_left

    if(distance_traveled > distance):
        solution_two += 1

print(solution_two)
assert(solution_two == 34788142)