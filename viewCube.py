import numpy as np


def colourise(char):
    colours = {
        "W": "\u001b[37m",
        "R": "\u001b[31m",
        "Y": "\u001b[93m",
        "O": "\033[38;2;255;165;0m",
        "B": "\u001b[34m",
        "G": "\u001b[32m",
    }
    highlights = {
        "W": "\u001b[47m",
        "R": "\u001b[41m",
        "Y": "\u001b[103m",
        "O": "\033[48;2;255;165;0m",
        "B": "\u001b[44m",
        "G": "\u001b[42m",
    }
    return f"{colours.get(char)}{highlights.get(char)}{char}{char}\u001b[0m"


def visualise():
    try:
        front, left, right, top, bottom, behind = loadCube()
        text = ""
        for i in range(3):
            text += f"        {''.join(map(colourise, top[i]))}\n"
        text += "\n"
        for i in range(3):
            text += f"{''.join(map(colourise, left[i]))}  {''.join(map(colourise, front[i]))}  {''.join(map(colourise, right[i]))}  {''.join(map(colourise, behind[i]))}\n"
        text += "\n"
        for i in range(3):
            text += f"        {''.join(map(colourise, bottom[i]))}\n"
        return text
    except FileNotFoundError:
        pass


def loadCube():
    loadedCube = np.load("cube.npz")
    bottom = loadedCube["bottom"]
    left = loadedCube["left"]
    top = loadedCube["top"]
    right = loadedCube["right"]
    behind = loadedCube["behind"]
    front = loadedCube["front"]
    return front, left, right, top, bottom, behind
