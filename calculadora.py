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

 
#----- dividindo a janela em duas partes ------


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


#---------- configurando frame cima -------------

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


#------------------- calculos ----------------------

def calcular():

    peso= float(result_peso.get())
    altura= float(result_altura.get())

    imc  = peso / altura ** 2

    resultado = imc

    if resultado < 18.5:
        resultado_imc['text'] =  'De acordo com seu IMC: Você está abaixo do peso'

    elif resultado >= 18.5 and resultado < 25:
        resultado_imc['text'] = 'De acordo com seu IMC: Você está normal'

    elif resultado >= 25 and resultado <30:
        resultado_imc['text'] = 'De acordo com seu IMC: Você está com sobrepeso' 

    elif resultado >= 30 and resultado <35:
        resultado_imc['text'] = 'De acordo com seu IMC: você está com obesidade grau I'

    elif resultado >= 35 and resultado <40:
        resultado_imc['text'] = 'De acordo com seu IMC: você está com obesidade grau II'

    else:
        resultado_imc['text'] = 'De acordo com seu IMC: Você está com obesidade Grau III'


    valor_imc['text'] = '{:.{}f}'.format(resultado, 2)



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
    text='',
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
    text='',
    width= 37,
    height=1 , 
    padx=6, 
    pady=12, 
    relief='flat', 
    anchor='center', 
    font=('Arial', 9 , 'bold'), 
    bg=co0, fg=co1
)
resultado_imc.place(x=0, y=90) 


#------------- botão de calcular o imc ---------------

btn_calcular= Button(
    frame_baixo,
    command= calcular,
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




janela.mainloop()

#janela finalizada 