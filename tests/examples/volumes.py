import math

def get_cylinder_volume(radius, height):
    return math.pi * height * radius ** 2

def get_sphere_volume(radius):
    return 4 / 3 * math.pi * radius ** 3

def get_cube_volume(side):
    return side ** 3

def get_tank_volume(length, width, height):
    return length * width * height