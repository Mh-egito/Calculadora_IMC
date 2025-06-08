from tkinter import *
from tkinter import ttk

#cores

co0= '#ffffff'
co1= '#444466'
co2= '#4065a1' 


#importanto a biblioteca do tkinter para poder criar uma janela


janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co0)


#dividindo a janela em duas partes 


frame_cima= Frame(
    janela,
    width=295, 
    height=50, 
    bg=co0, 
    pady=0 , 
    padx=0, 
    relief='flat'
)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(
    janela, 
    width=295, 
    height=180, 
    bg=co0, 
    pady=0, 
    padx=0, 
    relief='flat'
)
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#configurando frame cima


nome_app= Label(
    frame_cima,
    text='Calculadora de IMC',
    width=400, 
    height=1, 
    padx=0, 
    relief='flat', 
    anchor='center', 
    font=('Arial', 16, 'bold'), 
    bg= co0, fg=co1
)
nome_app.place(relx=0.5, y=10, anchor='center')

linha_app= Label(
    frame_cima,
    text='',
    width=400,
    height=1,  
    padx=0,
    relief='flat', 
    anchor='center', 
    font=('Arial', 1,), 
    bg=co2, fg=co1
)
linha_app.place(x=0, y=35)



janela.mainloop()

#criação da janela realizada 

