import curses
import random
import string


def init_colors():
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)


def init(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(10)

    init_colors()

    max_y, max_x = stdscr.getmaxyx()

    return max_y, max_x, [], [0] * (max_x - 1), [False] * (max_x - 1)


def main(stdscr):

    max_y, max_x, lines, snakes_lines, snake_first = init(stdscr)
    blue_color = curses.color_pair(1)
    white_color = curses.color_pair(2)

    while True:
        stdscr.clear()

        new_line = []

        for i in range(max_x - 1):
            if snakes_lines[i] == 0:
                random_spawn = random.random() * 100
                new_line.append((' ', blue_color))

                if random_spawn < 2:
                    snakes_lines[i] = random.randint(6, 12)
                    snake_first[i] = True
            else:
                char = random.choice(string.ascii_letters + string.digits + string.punctuation)
                if snake_first[i]:
                    snake_first[i] = False
                    new_line.append((char, white_color))
                else:
                    new_line.append((char, blue_color))
                snakes_lines[i] -= 1

        lines.insert(0, new_line)
        lines = lines[:max_y]

        for i, line in enumerate(lines):
            for j, (char, color) in enumerate(line):
                stdscr.addstr(i, j, char, color)

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break


if __name__ == "__main__":
    curses.wrapper(main)
