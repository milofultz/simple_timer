import os
import re
from shutil import get_terminal_size
import time

from colors import Colors
from config import DEFAULT_TIMER_LENGTH


TERMINAL_HEIGHT = get_terminal_size()[1]


def main():
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
        time_spent = input('Task Time: ')
        if re.match(r'\d:[0-6]\d', time_spent):
            return time_spent
        elif re.match(r'[0-6]?\d', time_spent):
            return f"0:{time_spent.zfill(2)}"
        elif time_spent == '' and default_time:
            return default_time
        print('Please ensure your input matches `H:MM`.')


def timer(timer_length: str):
    timer_length_seconds = convert_time_spent_to_seconds(timer_length)
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
        say("Timer complete")
        alarm(5)
    clear_screen()


def convert_time_spent_to_seconds(length: str):
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
