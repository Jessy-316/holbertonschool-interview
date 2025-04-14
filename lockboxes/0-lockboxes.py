#!/usr/bin/python3
"""
Module that contains the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list of keys
                              Each key corresponds to a box number
           
    Returns:
        bool: True if all boxes can be opened, else False
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # First box is unlocked

    # Keep track of keys we need to process
    keys_to_check = [0]  # Start with box 0

    while keys_to_check:
        current_box = keys_to_check.pop()

        for key in boxes[current_box]:
            #If the key corresponds to a valid box and that box is still locked
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys_to_check.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
