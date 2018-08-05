from random import randrange as rnd, choice, shuffle
from tkinter import *
import itertools, time, copy
import time
   
root = Tk()
root.geometry('800x600')
   
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
 
nr = 10
nc = 12
m = 24
y0 = x0 = m
 
 
class cell():
    def __init__(self):
        self.n = 0
        self.bomb = 0
        self.mode = 'closed'
         
def new_game():
    global a
    a = [[cell() for c in range(nc)] for r in range(nr)]
    bomb_count = 18
    while bomb_count > 0:
        r = rnd(nr)
        c = rnd(nc)
        if not a[r].bomb:
            a[r].bomb = 1
            bomb_count -= 1
     
    for r in range(nr):
        for c in range(nc):
            k = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    rr = r + dr
                    cc = c + dc
                    if rr in range(nr) and cc in range(nc):
                        if a[rr][cc].bomb:
                            k += 1
            a[r].n = k
     
    paint()
 
 
 
 
def paint():
    canv.delete(ALL)
    for r in range(nr):
        for c in range(nc):
            x = x0 + c*m
            y = y0 + r*m
            if a[r].mode == 'opened':
                if not a[r].bomb:
                    canv.create_rectangle(x,y,x+m,y+m, fill = 'white')
                    if a[r].n > 0:
                        canv.create_text(x+m//2,y+m//2, text = a[r].n)
                else:
                    canv.create_rectangle(x,y,x+m,y+m, fill = 'red')
            elif a[r].mode == 'closed':
                canv.create_rectangle(x,y,x+m,y+m, fill = 'gray')
            elif a[r].mode == 'flag':
                canv.create_rectangle(x,y,x+m,y+m, fill = 'orange')
 
def cell_change(r,c,button):
    if a[r].mode == 'closed':
        if button == 1:
            time.sleep(0.001)
            a[r].mode = 'opened'
            if a[r].n == 0:
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        rr = r + dr
                        cc = c + dc
                        if rr in range(nr) and cc in range(nc):
                            paint()
                            canv.update()
                            cell_change(rr,cc,1)
                 
                 
            if a[r].bomb:
                print('boom!!!')
        elif button == 3:
            a[r].mode = 'flag'
    elif a[r].mode == 'flag' and button == 3:
         a[r].mode = 'closed'
 
     
 
def click(event):
    r = (event.y - y0)//m
    c = (event.x - x0)//m
    if r in range(nr) and c in range(nc):
        cell_change(r,c,event.num)
    paint()
     
new_game()       
     
     
canv.bind('<1>',click)   
canv.bind('<3>',click)   
mainloop()