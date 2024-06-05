#!/usr/bin/python3
"""Solution to lockboxes problem"""

def canUnlockAll(boxes):
    """Solution to the lockboxes problem"""
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for a in range(1, len(boxes) - 1):
        boxes_checked = False
        for b in range(len(boxes)):
            boxes_checked = a in boxes[b] and a != b
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
