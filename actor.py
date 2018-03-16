import numpy as np
from display import Dp

ACTOR0 = np.array([[1], [1], [1], [1]])
ACTOR1 = np.array([[1, 1], [0, 1], [0, 1]])
ACTOR2 = np.array([[1, 1], [1, 0], [1, 0]])
ACTOR3 = np.array([[0, 1], [1, 1], [0, 1]])
ACTOR4 = np.array([[1, 0], [1, 1], [1, 0]])
ACTOR5 = np.array([[1, 1], [1, 1]])
ACTOR6 = np.array([[0, 1], [1, 1], [1, 0]])
ACTOR7 = np.array([[1, 0], [1, 1], [0, 1]])
ACTORS = [ACTOR0, ACTOR1, ACTOR2, ACTOR3, ACTOR4, ACTOR5, ACTOR6, ACTOR7]

class Actor:
    def __init__(self, dataset, x=0, y=0):
        self.__dataset = dataset 
        self.x = x 
        self.y = y

    def value(self):
        return self.__dataset

    def shape(self):
        return self.__dataset.shape

    def rotate(self, bg):
        dataset = np.rot90(self.__dataset)
        x = self.x
        y = self.y
        
        brow, bcol = bg.shape()
        row, col = dataset.shape 
        if x + row > brow - 1 or y + col > bcol - 1:
            return -1 
        if self.overlap(bg, x, y):
            return -1 
        self.__dataset = dataset

        return 0 

    def left(self, bg):
        x = self.x
        y = self.y - 1 
        if y < 0:
            return -1 
        if self.overlap(bg, x, y):
            return -1 
        self.y = y
        return 0 

    def right(self, bg):
        x = self.x
        y = self.y + 1
        col = self.__dataset.shape[1]
        if y + col > bg.shape()[1]:
            return -1 
        if self.overlap(bg, x, y):
            return -1
        self.y = y
        return 0 

    def Down(self, bg):
        x = self.x + 1
        y = self.y
        row = self.__dataset.shape[0]
        if x + row > bg.shape()[0]:
            return -1  
        if self.overlap(bg, x, y):
            return -1
        self.x = x
        return 0 

    def overlap(self, bg, x, y):
        array = np.array(self.__dataset, copy=True)
        row, col = self.__dataset.shape
        for i  in range(row):
            for j in range(col):
                array[i][j] = array[i][j] + bg.value()[x + i][y + j]
                if array[i][j] == 2:
                    return True
        return False
    
    def get_img(self):
        dp = Dp(self.__dataset)
        return dp.get_img()

if __name__ == '__main__':
    actor = Actor(ACTORS[7])
    print actor.value()
    print actor.shape()
