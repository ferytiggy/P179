# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:33:39 2024

@author: Aidan
"""

from tkinter import *
import random

root = Tk()
root.title("P178")
root.geometry("800x1200")
root.config(bg="cyan")

label_name = Label(root, bg="white")
label_name.place(relx=0.5, rely=0.5, anchor=CENTER)
label_score = Label(root, text="Puntos = 0", bg="white")
label_score.place(relx=0.5, rely=0.7, anhor=CENTER)
input_value = Entry(root)

class game:
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["ROSA", "VERDE", "ROJO", "AZUL", "AMARILLO", "NARANJA"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black", "green", "red", "blue", "yellow", "orange"]
        self.random_number_for_color = random.randint(0,5)
        label_name["text"] = self.color[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
        
    def __updateScore():
        if(input_value == self.color[self.random_number_for_color]):
            print (self.color[self.random_number_for_color])
            self.__score = self-__score + random.randint(0,10)
            label_score["text"] = "Puntos =" + str(self.score)
            
    def get_user_value(self, input_value):
        __updateScore()
        
    def getInput():
        obj.get_user_value(value)
        input_value.delete(0,10)
        
 
btn = Button(root, text="Iniciar", command=getInput, bg="white", fg="white",
relief=FLAT, padx=10, pady=1, font=("Arial",15))

root.mainloop()