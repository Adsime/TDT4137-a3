import shapes
import numpy as np
import matplotlib.pyplot as plt


def triangle_val(xPos, coordinates, cut):
    return shapes.triangle(xPos, coordinates[0], coordinates[1], coordinates[2], cut)


def integrate(arr):
    over = 0
    under = 0
    index = -10
    for x in arr:
        over += x * index
        under += x
        index += 1
    return over/under


def aggregate_rules(defArr, coords, cuts):
    items = []
    i = 0
    for x in defArr:
        t1 = triangle_val(x, coords[0], cuts[0])
        t2 = triangle_val(x, coords[1], cuts[1])
        t3 = triangle_val(x, coords[2], cuts[2])

        items.insert(i, max(t1, t2, t3))
        i += 1
    return items


def plot(defArr, items, position):
    plt.plot(defArr, items)
    plt.plot([position, position], [0, 1], '-')
    plt.axis([-10, 10, 0, 1])
    plt.xticks(defArr)
    plt.show()








