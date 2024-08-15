#!/usr/bin/python3
""" Lock Boxes Module"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    n = len(boxes)
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
