import sys
import cv2
import numpy as np
from actor import Actor, ACTORS 
from background import Bg
import random
import time

def show(img_name, img_data, x=0, y=0):
    cv2.namedWindow(img_name)
    cv2.moveWindow(img_name, x, y)
    cv2.imshow(img_name, img_data)

def get_actor(col):
    mmax = len(ACTORS) - 1 
    p = random.randint(0, mmax)
    dataset = ACTORS[p]
    _, acol = dataset.shape 
    y = (col - acol) / 2
    return Actor(dataset, 0, y)  

if __name__ == '__main__':
    _quit = False 
    col = 10 
    dataset = np.zeros((20, col), dtype=int)
    bg = Bg(dataset)
    tmp_bg = bg
    curr_actor = None
    reserve_actor = get_actor(col)
    begin_time = time.time() 
    score = 0
    while not _quit:
        if not curr_actor:
            curr_actor = reserve_actor
            reserve_actor = get_actor(col)
            show('next actor', reserve_actor.get_img(), 200, 0)
            tmp_bg = bg.add(curr_actor)
        show('tetris', tmp_bg.get_img(), 500, 0)
        print('****************')
        print('score:', score)
        print('time: ', time.time() - begin_time)
        print('****************')
        print('')

        c = cv2.waitKey(1000)
        if c == 27:
            _quit = True 
        elif c == 65361:
            curr_actor.left(bg)
            tmp_bg = bg.add(curr_actor)
            continue
        elif c == 65363:
            curr_actor.right(bg)
            tmp_bg = bg.add(curr_actor)
            continue
        elif c == 65362:
            curr_actor.rotate(bg)
            tmp_bg = bg.add(curr_actor)

        elif c == 65364:
            curr_actor.Down(bg)
        else:
            pass
        ret = curr_actor.Down(bg)
        if curr_actor.x == 0:
            sys.exit('game over')
        tmp_bg = bg.add(curr_actor)
        if ret == -1:
            bg = tmp_bg
            bg.refresh()
            tmp_bg = bg
            curr_actor = None
            score = score + 1
    cv2.destroyAllWindows()
