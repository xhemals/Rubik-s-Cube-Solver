import numpy as np
import viewCube, moves
import random
import kociemba
import pyfiglet
import subprocess
import os


def newCube():
    colours = ["Y", "O", "W", "R", "B", "G"]
    faces = ["bottom", "left", "top", "right", "behind", "front"]
    cube = {}
    for face, color in zip(faces, colours):
        cube[face] = np.array([[color] * 3] * 3)
    np.savez("cube.npz", **cube)


def loadCube():
    loadedCube = np.load("cube.npz")
    bottom = loadedCube["bottom"]
    left = loadedCube["left"]
    top = loadedCube["top"]
    right = loadedCube["right"]
    behind = loadedCube["behind"]
    front = loadedCube["front"]
    return front, left, right, top, bottom, behind


def scramble(visual):
    randomNumber = random.randint(20, 25)
    randomMoves = random.choices(moves.moves(), k=randomNumber)
    randomMoves = " ".join(randomMoves)
    moves.makeMoves(randomMoves, visual)
    return randomMoves


def solve(visual):
    front, left, right, top, bottom, behind = loadCube()
    faces = ""
    arrays = [top, right, front, bottom, left, behind]
    for array in arrays:
        for sub_array in array:
            for element in sub_array:
                faces += element
    faces = (
        faces.replace("W", "U").replace("O", "L").replace("Y", "D").replace("G", "F")
    )
    solveMoves = kociemba.solve(faces)
    moves.makeMoves(solveMoves, visual)
    return solveMoves


def start(page):
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print(pyfiglet.figlet_format("PYCUBE", justify="center"))
    print(f"Your Cube: \n \n{viewCube.visualise()}")
    if page == "home":
        print(
            """
        [1] New Cube
        [2] Scramble
        [3] Solve
        [4] Move Mode
        [X] Exit
            """
        )
        option = input("Select Option: ")
        if option == "1":
            newCube()
            start("home")
        elif option == "2":
            start("scramble")
        elif option == "3":
            start("solve")
        elif option == "4":
            start("move")
        elif option == "X" or option == "x":
            exit()
    elif page == "scramble":
        print(
            """
        [1] Scramble With Steps
        [2] Scramble Without Steps
        [3] Give Scramble Algorithm
        [X] Back
            """
        )
        option = input("Select Option: ")
        if option == "1":
            scramble(True)
            start("home")
        elif option == "2":
            scramble(False)
            start("scramble")
        elif option == "3":
            algorithm = scramble(False)
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print(pyfiglet.figlet_format("PYCUBE", justify="center"))
            print(f"Your Cube: \n \n{viewCube.visualise()}")
            print(f"Scramble Algorithm:\n{algorithm}\n")
            wait = input("Press enter to continue...")
            start("home")
        elif option == "X" or option == "x":
            start("home")
    elif page == "solve":
        print(
            """
        [1] Solve With Steps
        [2] Give Solve Algorithm
        [X] Back
            """
        )
        option = input("Select Option: ")
        if option == "1":
            solve(True)
            start("home")
        elif option == "2":
            algorithm = solve(False)
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print(pyfiglet.figlet_format("PYCUBE", justify="center"))
            print(f"Your Cube: \n \n{viewCube.visualise()}")
            print(f"Solve Algorithm:\n{algorithm}\n")
            wait = input("Press enter to continue...")
            start("home")
        elif option == "X" or option == "x":
            start("home")
    elif page == "move":
        print(
            "Available Moves: \n"
            "U   D   R   L   F   B \n"
            "U'  D'  R'  L'  F'  B'\n"
            "U2  D2  R2  L2  F2  B2\n"
            "[X] Back\n"
        )
        move = input("What is your move: ").upper()
        if move == "X" or move == "X":
            start("home")
        moves.makeMoves(move, False)
        start("move")


if __name__ == "__main__":
    start("home")
