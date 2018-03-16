import numpy as np

class Dp:
    def __init__(self, dataset0, length=32, thick=2):
        self.length = length
        self.thick = thick
        self.o_length = length - thick
        self.__BLACK = self.__get_black()
        self.__WHITE = self.__get_white()
        row,col = dataset0.shape
        self.__dataset = np.zeros((row*length, col*length))
        for i in range(row):
            for j in range(col):
                bi = length*i
                bj = length*j
                if dataset0[i][j] == 1:
                    self.__dataset[bi:bi+length, bj:bj+length] = self.__BLACK
                else:
                    self.__dataset[bi:bi+length, bj:bj+length] = self.__WHITE
        self.__img = np.reshape(self.__dataset,(row*length, col*length, 1))

    def __get_black(self):
        length = self.length
        o_length = self.o_length
        thick = self.thick
        black = 255*np.ones((length, length), dtype = np.int)
        black[thick:o_length,thick:o_length] = black[thick:o_length,thick:o_length] -255
        return black

    def __get_white(self):
        length = self.length
        o_length = self.o_length
        thick = self.thick
        white = np.zeros((length, length), dtype=np.int)
        white[thick:o_length, thick:o_length] = white[thick:o_length, thick:o_length] + 255
        return white

    def get_img(self):
        return self.__img

if __name__ == '__main__':
    import cv2
    a = np.array([[0,1],[0,0]])
    dp = Dp(a, length = 32)
    print dp.get_img()
    cv2.imshow('av', dp.get_img())
    cv2.waitKey()
