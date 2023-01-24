import numpy as np
import viewCube
import subprocess
import os


def loadCube():
    loadedCube = np.load("cube.npz")
    bottom = loadedCube["bottom"]
    left = loadedCube["left"]
    top = loadedCube["top"]
    right = loadedCube["right"]
    behind = loadedCube["behind"]
    front = loadedCube["front"]
    return front, left, right, top, bottom, behind


def save(front, left, right, top, bottom, behind):
    np.savez(
        "cube.npz",
        bottom=bottom,
        left=left,
        top=top,
        right=right,
        behind=behind,
        front=front,
    )


def F():
    front, left, right, top, bottom, behind = loadCube()
    front = front[::-1]
    front = front.transpose()

    t = [top[2][0], top[2][1], top[2][2]]
    r = [right[0][0], right[1][0], right[2][0]]
    l = [left[2][2], left[1][2], left[0][2]]
    bo = [bottom[0][0], bottom[0][1], bottom[0][2]]

    t, r, l, bo = l, t, bo, r

    top[2][0], top[2][1], top[2][2] = t[0], t[1], t[2]
    right[0][0], right[1][0], right[2][0] = r[0], r[1], r[2]
    left[0][2], left[1][2], left[2][2] = l[0], l[1], l[2]
    bottom[0][2], bottom[0][1], bottom[0][0] = bo[0], bo[1], bo[2]

    save(front, left, right, top, bottom, behind)


def R():
    front, left, right, top, bottom, behind = loadCube()
    right = right[::-1]
    right = right.transpose()

    f = [front[0][2], front[1][2], front[2][2]]
    bo = [bottom[0][2], bottom[1][2], bottom[2][2]]
    be = [behind[2][0], behind[1][0], behind[0][0]]
    t = [top[0][2], top[1][2], top[2][2]]

    t, be, bo, f = f, t, be, bo

    front[0][2], front[1][2], front[2][2] = f[0], f[1], f[2]
    bottom[0][2], bottom[1][2], bottom[2][2] = bo[0], bo[1], bo[2]
    behind[2][0], behind[1][0], behind[0][0] = be[0], be[1], be[2]
    top[0][2], top[1][2], top[2][2] = t[0], t[1], t[2]

    save(front, left, right, top, bottom, behind)


def U():
    front, left, right, top, bottom, behind = loadCube()
    top = top[::-1]
    top = top.transpose()

    f = [front[0][0], front[0][1], front[0][2]]
    l = [left[0][0], left[0][1], left[0][2]]
    be = [behind[0][0], behind[0][1], behind[0][2]]
    r = [right[0][0], right[0][1], right[0][2]]

    f, l, be, r = r, f, l, be
    front[0][0], front[0][1], front[0][2] = f[0], f[1], f[2]
    left[0][0], left[0][1], left[0][2] = l[0], l[1], l[2]
    behind[0][0], behind[0][1], behind[0][2] = be[0], be[1], be[2]
    right[0][0], right[0][1], right[0][2] = r[0], r[1], r[2]
    save(front, left, right, top, bottom, behind)


def L():
    front, left, right, top, bottom, behind = loadCube()
    left = left[::-1]
    left = left.transpose()

    f = [front[0][0], front[1][0], front[2][0]]
    bo = [bottom[0][0], bottom[1][0], bottom[2][0]]
    be = [behind[2][2], behind[1][2], behind[0][2]]
    t = [top[0][0], top[1][0], top[2][0]]

    t, be, bo, f = be, bo, f, t

    front[0][0], front[1][0], front[2][0] = f[0], f[1], f[2]
    bottom[0][0], bottom[1][0], bottom[2][0] = bo[0], bo[1], bo[2]
    behind[2][2], behind[1][2], behind[0][2] = be[0], be[1], be[2]
    top[0][0], top[1][0], top[2][0] = t[0], t[1], t[2]

    save(front, left, right, top, bottom, behind)


def B():
    front, left, right, top, bottom, behind = loadCube()
    behind = behind[::-1]
    behind = behind.transpose()

    t = [top[0][0], top[0][1], top[0][2]]
    r = [right[0][2], right[1][2], right[2][2]]
    l = [left[0][0], left[1][0], left[2][0]]
    bo = [bottom[2][2], bottom[2][1], bottom[2][0]]

    t, r, l, bo = r, bo, t, l

    top[0][0], top[0][1], top[0][2] = t[0], t[1], t[2]
    right[0][2], right[1][2], right[2][2] = r[0], r[1], r[2]
    left[2][0], left[1][0], left[0][0] = l[0], l[1], l[2]
    bottom[2][0], bottom[2][1], bottom[2][2] = bo[0], bo[1], bo[2]

    save(front, left, right, top, bottom, behind)


def D():
    front, left, right, top, bottom, behind = loadCube()
    bottom = bottom[::-1]
    bottom = bottom.transpose()

    f = [front[2][0], front[2][1], front[2][2]]
    l = [left[2][0], left[2][1], left[2][2]]
    be = [behind[2][0], behind[2][1], behind[2][2]]
    r = [right[2][0], right[2][1], right[2][2]]

    f, l, be, r = l, be, r, f
    front[2][0], front[2][1], front[2][2] = f[0], f[1], f[2]
    left[2][0], left[2][1], left[2][2] = l[0], l[1], l[2]
    behind[2][0], behind[2][1], behind[2][2] = be[0], be[1], be[2]
    right[2][0], right[2][1], right[2][2] = r[0], r[1], r[2]
    save(front, left, right, top, bottom, behind)


def Y():
    front, left, right, top, bottom, behind = loadCube()
    bottom = bottom[::-1]
    bottom = bottom.transpose()
    top = top[::-1]
    top = top.transpose()

    f = [
        front[0][0],
        front[0][1],
        front[0][2],
        front[1][0],
        front[1][1],
        front[1][2],
        front[2][0],
        front[2][1],
        front[2][2],
    ]
    l = [
        left[0][0],
        left[0][1],
        left[0][2],
        left[1][0],
        left[1][1],
        left[1][2],
        left[2][0],
        left[2][1],
        left[2][2],
    ]
    be = [
        behind[0][0],
        behind[0][1],
        behind[0][2],
        behind[1][0],
        behind[1][1],
        behind[1][2],
        behind[2][0],
        behind[2][1],
        behind[2][2],
    ]
    r = [
        right[0][0],
        right[0][1],
        right[0][2],
        right[1][0],
        right[1][1],
        right[1][2],
        right[2][0],
        right[2][1],
        right[2][2],
    ]

    f, l, be, r = r, f, l, be

    (
        front[0][0],
        front[0][1],
        front[0][2],
        front[1][0],
        front[1][1],
        front[1][2],
        front[2][0],
        front[2][1],
        front[2][2],
    ) = (
        f[0],
        f[1],
        f[2],
        f[3],
        f[4],
        f[5],
        f[6],
        f[7],
        f[8],
    )
    (
        left[0][0],
        left[0][1],
        left[0][2],
        left[1][0],
        left[1][1],
        left[1][2],
        left[2][0],
        left[2][1],
        left[2][2],
    ) = (
        l[0],
        l[1],
        l[2],
        l[3],
        l[4],
        l[5],
        l[6],
        l[7],
        l[8],
    )
    (
        behind[0][0],
        behind[0][1],
        behind[0][2],
        behind[1][0],
        behind[1][1],
        behind[1][2],
        behind[2][0],
        behind[2][1],
        behind[2][2],
    ) = (
        be[0],
        be[1],
        be[2],
        be[3],
        be[4],
        be[5],
        be[6],
        be[7],
        be[8],
    )
    (
        right[0][0],
        right[0][1],
        right[0][2],
        right[1][0],
        right[1][1],
        right[1][2],
        right[2][0],
        right[2][1],
        right[2][2],
    ) = (
        r[0],
        r[1],
        r[2],
        r[3],
        r[4],
        r[5],
        r[6],
        r[7],
        r[8],
    )

    save(front, left, right, top, bottom, behind)


def f():
    for i in range(3):
        F()


def r():
    for i in range(3):
        R()


def u():
    for i in range(3):
        U()


def l():
    for i in range(3):
        L()


def b():
    for i in range(3):
        B()


def d():
    for i in range(3):
        D()


def F2():
    for i in range(2):
        F()


def R2():
    for i in range(2):
        R()


def U2():
    for i in range(2):
        U()


def L2():
    for i in range(2):
        L()


def B2():
    for i in range(2):
        B()


def D2():
    for i in range(2):
        D()


def makeMoves(moves, visual):
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    cube = f"Starting Cube\n{viewCube.visualise()}"
    moves.upper()
    moves = moves.split()
    numMoves = len(moves)
    movesCompleted = 0
    for move in moves:
        movesCompleted += 1
        if move == "F":
            F()
        elif move == "R":
            R()
        elif move == "U":
            U()
        elif move == "L":
            L()
        elif move == "B":
            B()
        elif move == "D":
            D()
        elif move == "Y":
            Y()
        elif move == "F'":
            f()
        elif move == "R'":
            r()
        elif move == "U'":
            u()
        elif move == "L'":
            l()
        elif move == "B'":
            b()
        elif move == "D'":
            d()
        elif move == "F2":
            F2()
        elif move == "R2":
            R2()
        elif move == "U2":
            U2()
        elif move == "L2":
            L2()
        elif move == "B2":
            B2()
        elif move == "D2":
            D2()
        if visual:
            cube += f"--------------------------\n{move}\n{viewCube.visualise()}\n"
            print(cube)
            if movesCompleted == numMoves:
                print("\u001b[32mAll Moves Completed\u001b[0m")
            else:
                print(f"Moves Completed: {movesCompleted}/{numMoves}")
            wait = input("Press enter to continue...")
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def moves():
    moves = [
        "F",
        "R",
        "U",
        "L",
        "B",
        "D",
        "F'",
        "R'",
        "U'",
        "L'",
        "B'",
        "D'",
        "F2",
        "R2",
        "U2",
        "L2",
        "B2",
        "D2",
    ]
    return moves
