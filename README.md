Simple Timer
---

I wanted a simple timer for my work that I can use in the terminal. I implemented more or less the same timer in [Tod](https://github.com/milofultz/tod), but wanted a standalone that was really easy to use, so here it is.

## Usage

Times should be entered using the format `H:MM`, using hours and minute respectively. If you enter nothing, it will use the default time. A time in minutes can also be entered in as a command line argument (e.g. `python3 main.py 25` will set the timer for 25 minutes).

When the timer completes, it will use TTS to speak the default message (tested only in OSX).


## Defaults

Defaults for time and end message can be set in the `config.py` file.