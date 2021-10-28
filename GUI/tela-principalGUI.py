from tkinter import *
from tkinter import ttk

app = Tk()

class Application():
    def __init__(self):
        self.app = app
        self.tela_principal()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        app.mainloop()
    def tela_principal(self):
        self.app.title('Leitor CSV')
        self.app.configure(background='#1e3743')
        self.app.geometry("700x550")
        self.app.resizable(True, True)
        self.app.maxsize(width=900, height=800)
        self.app.minsize(width=500, height=400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.app, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.16)
        self.frame_2 = Frame(self.app, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.78)
    def widgets_frame1(self):
        ### Botão limpar - para limpar o campo de pesquisa
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.20, rely=0.12, relwidth=0.1, relheight=0.4)
        ### Botão buscar - para buscar o arquivo csv
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.30, rely=0.12, relwidth=0.1, relheight=0.4)
        ### Botão pesquisar - para pesquisar um funcionario pela matricula
        self.bt_pesquisar = Button(self.frame_1, text='Filtrar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_pesquisar.place(relx=0.6, rely=0.12, relwidth=0.1, relheight=0.4)
        ### Botão limpar - para editar/alterar o campo de pesquisa
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.12, relwidth=0.1, relheight=0.4)
        ### Botão limpar - para apagar o campo de pesquisa
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.12, relwidth=0.1, relheight=0.4)

        ### Criação da Label para inserção da matrícula, realizar pesquisa
        self.lb_matricula = Label(self.frame_1, text='Matrícula', bd=2, bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold'))
        self.lb_matricula.place(relx=0.04, rely=0.08, relwidth=0.12, relheight=0.15)

        self.matricula_entry = Entry(self.frame_1)
        self.matricula_entry.place(relx=0.04, rely=0.4, relwidth=0.12, relheight=0.25)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=1, column=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))

        #Linhas da tabela
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Matrícula')
        self.listaCli.heading('#2', text='Entrada1')
        self.listaCli.heading('#3', text='Saída1')
        self.listaCli.heading('#4', text='Entrada2')
        self.listaCli.heading('#5', text='Saída2')
        self.listaCli.heading('#6', text='TotalHoras')

        #Colunas da tabela
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=50)
        self.listaCli.column('#3', width=50)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)
        self.listaCli.column('#6', width=50)

        self.listaCli.place(relx=0.01, rely=0.08, relwidth=0.95, relheight=0.88)

        #Barra de rolagem da tabela
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.08, relwidth=0.04, relheight=0.88)

Application()