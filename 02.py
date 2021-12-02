def step1():
    with open('02.txt') as file:
        movements = file.readlines()
        hor = 0
        depth = 0
        for i in range(0, len(movements)):
            splitMoves = movements[i].strip().split()
            direction = splitMoves[0]
            amount = splitMoves[1]
            if direction == 'forward':
                hor = hor + int(amount)

            if direction == 'down':
                depth = depth + int(amount)

            if direction == 'up':
                depth = depth - int(amount)


        print('Horizontal: ', hor)
        print('Depth: ', depth)
        print('Solution: ', (hor * depth))

def step2():
    with open('02.txt') as file:
        movements = file.readlines()
        hor = 0
        depth = 0
        aim = 0
        for i in range(0, len(movements)):
            splitMoves = movements[i].strip().split()
            direction = splitMoves[0]
            amount = splitMoves[1]
            if direction == 'forward':
                hor = hor + int(amount)
                depth = depth + (aim * int(amount))

            if direction == 'down':
                aim = aim + int(amount)

            if direction == 'up':
                aim = aim - int(amount)


        print('Horizontal: ', hor)
        print('Depth: ', depth)
        print('Solution: ', (hor * depth))

# step1()
step2()