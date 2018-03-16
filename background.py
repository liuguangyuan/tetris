import numpy as np
from display import Dp
class Bg:
    def __init__(self, dataset):
        self.__dataset = dataset

    def add(self, actor):
        tmp = np.array(self.__dataset, copy=True)
        row, col = actor.shape()
        x = actor.x
        y = actor.y
        for i in range(row):
            for j in range(col):
                tmp[x+i][y+j] = tmp[x+i][y+j] + actor.value()[i][j]

        return Bg(tmp) 

    def refresh(self):
        ds = []
        row, col = self.__dataset.shape
        for i in range(row):
            sum = 0
            for j in range(col):
                sum = sum + self.__dataset[i][j]
            if sum == col:
                 ds.append(i)
        tmp = np.delete(self.__dataset, ds, 0)
        for i in range(len(ds)):
            tmp = np.insert(tmp, 0, np.array(col*[0]), 0)
        self.__dataset = tmp

    def value(self):
        return self.__dataset

    def shape(self):
        return self.__dataset.shape

    def clear(self):
        row, col = self.__dataset.shape
        for i in range(row):
            for j in range(col):
                self.__dataset[i][j] = 0

    def get_img(self):
        dp = Dp(self.__dataset)
        return dp.get_img()

if __name__ == '__main__':
    from actor import Actor, ACTORS
    dataset = np.zeros((10, 8), dtype=int)
    print dataset
    bg = Bg(dataset)
    ac = Actor(ACTORS[0], 1,1)
    tmp = bg.add(ac)
    print tmp.value()
