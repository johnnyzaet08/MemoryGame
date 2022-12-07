from tkinter import *
from tkinter.ttk import *
import random
import time
move = 0
move1 = 0
move2 = 0

window = Tk()
window.title("Memory Game")
window.geometry('910x610')
window.resizable(width=False, height=False)
imagebackground=PhotoImage(file="fondo.gif")
background = Label(window, image=imagebackground).place(x=0, y=0)

lista_imagenes=[PhotoImage(file="carta.png"),
                PhotoImage(file="corazon.png"),
                PhotoImage(file="diamante.png"),
                PhotoImage(file="trebol.png")]
lista_cartas=['carta1',
              'carta2',
              'carta3',
              'carta4',
              'carta5',
              'carta6']
lista_carima=[1,
              2,
              3,
              1,
              2,
              3]
lista_posiciones=[(50,50),
                  (350,50),
                  (650,50),
                  (50,350),
                  (350,350),
                  (650,350)]
random.shuffle(lista_posiciones)

class carta:
    def __init__(self):
        self.btn = Button(window, command=self.vuelta)


    carta_num = ""
    def carta_num(self,carta_num):
        self.carta_num = carta_num
        print(carta_num)


    image_num=""
    def back (self, state, image_num):
        self.image_num = image_num
        print(image_num)
        if state == True:
            self.btn.config(image=lista_imagenes[0])
            self.btn.config(state = "enable")
        elif state == False:
            self.btn.config(image=lista_imagenes[self.image_num])
            self.btn.config(state = "disabled")

             
    def dibujar(self,place):
        print(place)
        self.btn.place(x=place[0],y=place[1])


    def vuelta(self):
        lista_cartas[self.carta_num].back(False, self.image_num)
        global move
        move += 1
        if move == 1:
            global move1
            move1 = self.image_num
        elif move == 2:
            global move2
            move2 = self.image_num
            move = 0
            return check()

def check():
    if move1 == move2:
        print("Ganaste")
    else:
        for num in [0,1,2,3,4,5]:
            lista_cartas[num].back(True, lista_carima[num])
            

        
for num in [0,1,2,3,4,5]:
    print(lista_cartas[num])
    print(num)
    lista_cartas[num] = carta()
    lista_cartas[num].carta_num(num)
    lista_cartas[num].back(True, lista_carima[num])
    lista_cartas[num].dibujar (lista_posiciones[num])

print(carta_num)



window.mainloop()
