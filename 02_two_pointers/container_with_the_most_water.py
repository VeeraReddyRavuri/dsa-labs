"""
You are given an integer array called height. Each number represents the height of a vertical wall at that specific index.
You need to choose exactly two walls that, together with the flat ground (the x-axis), form a container that can hold the absolute maximum amount of water.
Return the maximum area of water it can store.

Example:

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    Output: 49
"""


def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        current_area = (right - left) * min(height[left], height[right])

        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1

        if current_area > max_water:
            max_water = current_area

    return max_water
        

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))

