value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))

names = ["Mack","Villa","David"]
for x in names:
    print(x)

for x in "Venice":
    print(x)

for x in names:
    if x == "Villa":
        break
    print(x)

for x in names:
    if x == "Villa":
        continue
    print(x)

for x in range(2,4):
    print(x)

for x in range(0,100,5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Mack","Villa","David"]
actions = ["codes","eats","sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")

