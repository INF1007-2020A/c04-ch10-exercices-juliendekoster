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

    
def monte_carlo( iteration: int=5000) -> float:
    x_inside_dots = []
    x_outside_dots = []
    y_inside_dots = []
    y_outside_dots = []
    for i in range(iteration):
        x = np.random()
        y = np.random()
        if np.sqrt(x**2 * y**2) < 1:
            x_inside_dots.append(x)
            y_inside_dots.append(y)
        else:
            x_outside_dots.append(x)
            y_outside_dots.append(y)
    plt.scatter(x_inside_dots, y_inside_dots, label="inside dot")
    plt.scatter(x_outside_dots, y_outside_dots, label="outside dot")
    plt.title("calcul de monte-Carlo")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return float(len(inside_dots)) / iteration * 4
        
        
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(0, 0), (1, 1), (5, 8)])))
    print(find_closest_index(np.array([0, 5, 10, 12, 8]), 10.5))
    create_plot()
    pass
