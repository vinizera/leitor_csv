from tkinter import *

janela = Tk()
label = Label(janela, text='Menu Principal')
label.pack()

#Inclusão de uma janela onde irá aparecer o arquivo csv
def importar_csv():
    global janela
    janela.destroy()
    janela = Tk()
    label = Label(janela, text='Banco de Horas')
    label.pack()
    janela.geometry("300x300+150+50")
    janela.title("Leitor CSV")

    menu_bt = Button(janela, text='Retornar', command=tela_principal)
    menu_bt.pack()

#Inclusão de uma janela de tela principal
def tela_principal():
    global janela
    janela.destroy()
    janela = Tk()

    label = Label(janela, text='Tela Principal')
    label.pack()

    # Incluir um botão para chamar a função importar csv
    menu_bt_importar_csv = Button(janela, text='Importar csv',command=importar_csv)
    menu_bt_importar_csv.place(x=30, y=100)

    janela.geometry("300x300+150+50")
    janela.title("Leitor CSV")

    janela.mainloop()

janela.geometry("300x300+150+50")
janela.title("Leitor CSV")

janela.mainloop()


