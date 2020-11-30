import os
import re
from shutil import get_terminal_size
import sys
import time

from colors import Colors
from config import DEFAULT_TIMER_LENGTH, DEFAULT_COMPLETE_MESSAGE


TERMINAL_HEIGHT = get_terminal_size()[1]


def main():
    if len(sys.argv) > 1 and re.match(r'^[0-5]?\d$', sys.argv[1]):
        timer_length = f"0:{sys.argv[1].zfill(2)}"
    else:
        clear_screen()
        print(Colors.WHITE + 'Default timer length is: ' +
              Colors.RED + DEFAULT_TIMER_LENGTH + Colors.NORMAL + '\n')
        timer_length = task_time_input(DEFAULT_TIMER_LENGTH)
    timer(timer_length)


def clear_screen():
    print('\n' * TERMINAL_HEIGHT)


def task_time_input(default_time: str = None):
    """Validate task time input"""
    while True:
        length = input('Task Time: ')
        if re.match(r'\d:[0-5]\d', length):
            return length
        elif re.match(r'^[0-5]?\d$', length):
            return f"0:{length.zfill(2)}"
        elif length == '' and default_time:
            return default_time
        print('Please ensure your input matches `H:MM` or `MM`.')


def timer(timer_length: str):
    timer_length_seconds = convert_length_to_seconds(timer_length)
    elapsed_seconds = 0
    while elapsed_seconds <= timer_length_seconds:
        try:
            clear_screen()
            print_timer_details(timer_length, elapsed_seconds)
            time.sleep(1)
            elapsed_seconds += 1
        except KeyboardInterrupt:
            break
    if elapsed_seconds >= timer_length_seconds:
        say(DEFAULT_COMPLETE_MESSAGE)
        # alarm(5)
    clear_screen()


def convert_length_to_seconds(length: str):
    hours, minutes = length.split(':')
    return (int(hours) * 60 + int(minutes)) * 60


def print_timer_details(timer_length, elapsed_seconds):
    print(f'Timer Length: {Colors.GREEN}{timer_length}:00{Colors.NORMAL}')
    print(f'Elapsed Time: {format_hms_from_seconds(elapsed_seconds)} \n')
    print(Colors.WHITE + 'Press `Ctrl + C` to stop the timer' +
          Colors.NORMAL + '\n')


def format_hms_from_seconds(seconds):
    return (f'{seconds // 3600}:' +
            f'{((seconds // 60) % 60):02}:' +
            f'{(seconds % 60):02}')


def alarm(repetitions: int):
    try:
        for repetition in range(repetitions):
            for i in range(5):
                print('\a', end='', flush=True)
                time.sleep(.1)
            time.sleep(1.5)
    except KeyboardInterrupt:
        pass


def say(msg: str):
    os.system(f'say {msg} &')


if __name__ == "__main__":
    main()
