"""
compute required indicies.

date: 10/1
author: arabian9ts
"""

def smooth_L1(x):
    """
    smooth L1
    """
    y = 0
    if abs(x) < 1:
        y = 0.5 * x**2
    else:
        y = abs(x) - 0.5

    return y


def intersection(rect1, rect2):
    """
    intersecton of units
    rect is defined as [ top_left_x, top_left_y, height, width ]
    """
    top = max(rect1[1], rect2[1])
    left = max(rect1[0], rect2[0])
    right = min(rect1[0] + rect1[3], rect2[0] + rect2[3])
    bottom = min(rect1[1] + rect1[2], rect2[1] + rect2[2])

    if bottom > top and right > left:
        return (bottom-top)*(right-left)

    return 0


def jaccard(rect1, rect2):
    """
    Jaccard index.
    Jaccard index is defined as #(A∧B) / #(A∨B)
    """
    rect1_ = [x if x >= 0 else 0 for x in rect1]
    rect2_ = [x if x >= 0 else 0 for x in rect2]
    s = rect1_[2]*rect1_[3] + rect2_[2]*rect2_[3]

    # rect1 and rect2 => A∧B
    intersect = intersection(rect1_, rect2_)

    # rect1 or rect2 => A∨B
    union = s - intersect

    # A∧B / A∨B
    return intersect / union


print(smooth_L1(1))
print(smooth_L1(0.1))

rect1 = [0, 0, 10, 10]
rect2 = [5, 0, 5, 10]
print(intersection(rect1, rect2))