#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    # r = np.sqrt(x**2 + y**2)
    # angle = np.arctan2(y, x)
   # for c in cartesian_coordinates:
       # r = np.sqrt(c[0]**2 + c[1]**2)
        # angle = np.arctan2(c[1], c[0])
    return np.array([(np.sqrt(c[0]**2 + c[1]**2), np.arctan2(c[1], c[0])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    
    return np.abs(values - number).argmin()



def vreate_plot():
    x = np.linspace(-1, 1, num= 250)
    y = x**2 * np.sin(1 / x**2) + x
       
    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(0, 0), (1, 1), (5, 8)])))
    print(find_closest_index(np.array([0, 5, 10, 12, 8]), 10.5))
    create_plot()
    pass
