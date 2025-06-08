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

 
#------dividindo a janela em duas partes-------


frame_cima= Frame(
    janela,
    width=295, 
    height=50, 
    bg=co0, 
    pady=0 , 
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


#-----------configurando frame cima--------------

nome_app= Label(
    frame_cima,
    text='Calculadora de IMC',
    width=23,
    height=1,  
    padx=0,
    relief='flat', 
    anchor='center', 
    font=('Arial', 16, 'bold'), 
    bg=co0, fg=co1
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


#----------- configurando frame baixo --------------


#---------------- coletando peso -------------------

linha_peso= Label(
    frame_baixo,
    text='Insira seu peso',
    height=1, 
    padx=0, 
    relief='flat', 
    anchor='center', 
    font=('Arial', 10, 'bold'), 
    bg= co0, fg=co1
)
linha_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

result_peso= Entry(
    frame_baixo,
    width= 5,
    relief='solid', 
    font=('Arial', 10, 'bold'),
    justify='center' 
)
result_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


#---------------- coletando altura ------------------

linha_altura = Label(
    frame_baixo,
    text='Insira sua altura',
    height=1, 
    padx=0, 
    relief='flat', 
    anchor='center', 
    font=('Arial', 10, 'bold'), 
    bg= co0, fg=co1
)
linha_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

result_altura = Entry(
    frame_baixo,
    width= 5,
    relief='solid', 
    font=('Arial', 10, 'bold'),
    justify='center' 
)
result_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


#--------------- informando resultado ---------------

valor_imc= Label(
    frame_baixo,
    text='- - -',
    width= 5,
    height=1, 
    padx=12, 
    pady=12, 
    relief='flat', 
    anchor='center', 
    font=('Arial', 24, 'bold'), 
    bg= co2, fg=co0
)
valor_imc.place(x=175, y=10)


#----------------- inrformando IMC -------------------

resultado_imc= Label(
    frame_baixo,
    text='O seu IMC é: sobrepeso',
    width= 37,
    height=1 , 
    padx=6, 
    pady=12, 
    relief='flat', 
    anchor='center', 
    font=('Arial', 10 , 'bold'), 
    bg=co0, fg=co1
)
resultado_imc.place(x=0, y=90) 


#------------- botão de calcular o imc ---------------

btn_calcular= Button(
    frame_baixo,
    text='Calcular IMC',
    width= 34 ,
    height=1 ,
    overrelief='solid', 
    relief='raised', 
    anchor='center', 
    font=('Arial', 10 , 'bold'), 
    bg=co2, fg=co1
)
btn_calcular.grid(row=4 ,column=0 ,sticky=NSEW ,pady=60 , padx=25, columnspan=30)


#-------------------- calculos -----------------------

peso= 76
altura= 1.7

resultado= peso / altura ** 2

if resultado < 18.5:
    print('De acordo com seu IMC vc está abaixo do peso')
elif resultado >= 18.5 and resultado < 25:
    print('De acordo com seu IMC vc está normal')
elif resultado >= 25 and resultado <30:
    print('De acordo com seu IMC vc está sobrepeso')
else:
    print('De acordo com seu IMC vc está em obesidade')







janela.mainloop()

#criação da janela realizada 