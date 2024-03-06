import random

def display(room):
    for row in room:
        print(row)

# 1 means dirty location
# 0 means clean location
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

print("All the locations in the room are dirty")
display(room)

# Randomly assign dirt to locations
x = 0  # rows
y = 0  # cols
while x < 4:
    while y < 4:
        room[x][y] = random.choice([0, 1])
        y += 1
    x += 1
    y = 0

print("Before cleaning the room, the vacuum cleaner detects all the random dirt in the following locations")
display(room)

# Agent code
x = 0
y = 0
z = 0  # number of rooms cleaned

while x < 4:
    y = 0  # Reset y before starting the inner loop
    while y < 4:
        if room[x][y] == 1:
            print("Vacuum cleaner is in this location now:", x, y)
            room[x][y] = 0
            print("Location cleaned:", x, y)
            z += 1
        y += 1
    x += 1

print("Number of locations cleaned:", z)
performance = (100 - ((z / 16) * 100))
print("Room is clean now")
display(room)
print("Cleaning performance:", performance, "%")
