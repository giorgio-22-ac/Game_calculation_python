from GamePy import Calculate


def main():
    points = 0
    play(points)


def play(points):
    difficulty = int(input('Choose the level of difficulty [1, 2, 3 or 4]:'))
    calc = Calculate(difficulty)

    print('Show the result for the following operation:')
    calc._show_operation()

    result = int(input())

    if calc._check_result(result):
        points += 1
        print(f'You have {points} point(s).')

    go_on = int(input('Do you want to go on? [1 - yes, 2 - no]'))

    if go_on == 1:
        play(points)
    else:
        print(f'You ended with {points} point(s).')
        print('See you!')


if __name__ == '__main__':
    main()
