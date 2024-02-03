def apply_rule(rule, x, y):
    if rule == 1:
        return 4, y
    elif rule == 2:
        return x, 3
    elif rule == 3:
        d = min(x, 3 - y)
        return x - d, y + d
    elif rule == 4:
        d = min(y, 4 - x)
        return x + d, y - d
    elif rule == 5:
        return 0, y
    elif rule == 6:
        return x, 0
    elif rule == 7 or rule == 9:
        if x + y <= 4:
            return x + y, 0
        else:
            return 4, y - (4 - x)
    elif rule == 8 or rule == 10:
        if x + y <= 3:
            return 0, x + y
        else:
            return x - (3 - y), 3
    elif rule == 11:
        return 2, 0
    elif rule == 12:
        return 0, y
    else:
        return x, y

x, y = 0, 0

while True:
    print(f"Current state: ({x}, {y})")
    if x == 2:
        print("Goal state reached!")
        break

    rule_input = input("Enter rule number (1-12) or 'exit' to exit: ")
    if rule_input.lower() == 'exit':
        break

    rule = int(rule_input)
    if 1 <= rule <= 12:
        x, y = apply_rule(rule, x, y)
    else:
        print("Invalid rule. Please enter a number between 1 and 12.")