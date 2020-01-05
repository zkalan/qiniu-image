from sys import path
path.append('../')

from utils.math import add
from demo import sub

if __name__ == "__main__":
    a = int(input())
    print(sub(a, 1))
    print(add(a, 1))
