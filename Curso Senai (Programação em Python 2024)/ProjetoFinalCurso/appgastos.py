import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Funções de banco de dados
def conectar_banco():
    return sqlite3.connect('gastos.db')

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        email TEXT,
                        senha TEXT
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS gastos (
                        id INTEGER PRIMARY KEY,
                        usuario_id INTEGER,
                        data TEXT,
                        categoria TEXT,
                        descricao TEXT,
                        valor REAL,
                        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
                      )''')
    conexao.commit()
    conexao.close()

def cadastrar_usuario(nome, email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conexao.commit()
    conexao.close()

def verificar_usuario(email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario

def adicionar_gasto(usuario_id, data, categoria, descricao, valor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO gastos (usuario_id, data, categoria, descricao, valor) VALUES (?, ?, ?, ?, ?)',
                   (usuario_id, data, categoria, descricao, valor))
    conexao.commit()
    conexao.close()

def visualizar_gastos(usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM gastos WHERE usuario_id=?', (usuario_id,))
    gastos = cursor.fetchall()
    conexao.close()
    return gastos

# Interface gráfica com tema escuro
class TelaLoginCadastro:
    def __init__(self, master):
        self.master = master
        master.title("Aplicativo de Controle de Gastos")
        master.configure(bg='#000000')
        
        # Frames
        self.frame_login = tk.Frame(master, bg='#000000')
        self.frame_login.pack(pady=20)

        self.frame_cadastro = tk.Frame(master, bg='#000000')
        
        # Título
        self.label_titulo = tk.Label(self.frame_login, text="LOGIN", font=("Montserrat", 20), bg='#000000', fg='#FFFFFF')
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Labels e Entrys de Login
        self.label_email = tk.Label(self.frame_login, text="Email:", font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.label_email.grid(row=1, column=0, pady=10, padx=10)
        self.entry_email = tk.Entry(self.frame_login, font=("Montserrat", 10), bg='#000000', fg='#FFFFFF')
        self.entry_email.grid(row=1, column=1, pady=10, padx=10)

        self.label_senha = tk.Label(self.frame_login, text="Senha:", font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.label_senha.grid(row=2, column=0, pady=10, padx=10)
        self.entry_senha = tk.Entry(self.frame_login, font=("Montserrat", 10), bg='#000000', fg='#FFFFFF', show="*")
        self.entry_senha.grid(row=2, column=1, pady=10, padx=10)

        # Botão de Login
        self.botao_login = tk.Button(self.frame_login, text="Login", font=("Montserrat", 14), bg='#4682B4', fg='#FFFFFF', command=self.login)
        self.botao_login.grid(row=3, column=0, columnspan=2, pady=10)

        # Link para Cadastro
        self.label_cadastrar = tk.Label(self.frame_login, text="Não tem uma conta? Cadastre-se aqui.", font=("Montserrat", 10), bg='#000000', fg='#FFFFFF', cursor="hand2")
        self.label_cadastrar.grid(row=4, column=0, columnspan=2)
        self.label_cadastrar.bind("<Button-1>", self.mostrar_cadastro)

        # Frame Cadastro (inicialmente escondido)
        self.frame_cadastro = tk.Frame(master, bg='#000000')
        self.frame_cadastro.pack(pady=20, padx=20)
        self.frame_cadastro.pack_forget()

        # Título
        self.label_titulo_cadastro = tk.Label(self.frame_cadastro, text="CADASTRO", font=("Montserrat", 20), bg='#000000', fg='#FFFFFF')
        self.label_titulo_cadastro.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Labels e Entrys de Cadastro
        self.label_nome_cadastro = tk.Label(self.frame_cadastro, text="Nome:", font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.label_nome_cadastro.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nome_cadastro = tk.Entry(self.frame_cadastro, font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.entry_nome_cadastro.grid(row=1, column=1, pady=10, padx=10)

        self.label_email_cadastro = tk.Label(self.frame_cadastro, text="Email:", font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.label_email_cadastro.grid(row=2, column=0, pady=10, padx=10)
        self.entry_email_cadastro = tk.Entry(self.frame_cadastro, font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.entry_email_cadastro.grid(row=2, column=1, pady=10, padx=10)

        self.label_senha_cadastro = tk.Label(self.frame_cadastro, text="Senha:", font=("Montserrat", 12), bg='#000000', fg='#FFFFFF')
        self.label_senha_cadastro.grid(row=3, column=0, pady=10, padx=10)
        self.entry_senha_cadastro = tk.Entry(self.frame_cadastro, font=("Montserrat", 12), bg='#000000', fg='#FFFFFF', show="*")
        self.entry_senha_cadastro.grid(row=3, column=1, pady=10, padx=10)

        # Botão de Cadastro
        self.botao_cadastro = tk.Button(self.frame_cadastro, text="Cadastrar", font=("Montserrat", 14), bg='#4682B4', fg='#FFFFFF', command=self.cadastrar)
        self.botao_cadastro.grid(row=4, column=0, columnspan=2, pady=5)

    def login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if email and senha:
            usuario = verificar_usuario(email, senha)
            if usuario:
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                self.master.destroy()
                root = tk.Tk()
                app = AplicativoGastos(root, usuario[0])
                root.mainloop()
            else:
                messagebox.showerror("Erro", "Email ou senha incorretos!")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")

    def cadastrar(self):
        nome = self.entry_nome_cadastro.get()
        email = self.entry_email_cadastro.get()
        senha = self.entry_senha_cadastro.get()

        if nome and email and senha:
            cadastrar_usuario(nome, email, senha)
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            self.mostrar_login(None)
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")

    def mostrar_cadastro(self, event):
        self.frame_login.pack_forget()
        self.frame_cadastro.pack(pady=20)

    def mostrar_login(self, event):
        self.frame_cadastro.pack_forget()
        self.frame_login.pack(pady=20)

class AplicativoGastos:
    def __init__(self, master, usuario_id):
        self.master = master
        master.title("Bem Vindo")
        master.configure(bg='#000000')
        self.usuario_id = usuario_id
        
        # Título
        self.label_titulo = tk.Label(master, text="Controle de Gastos", font=("Arial", 24), bg='#000000', fg='#FFFFFF')
        self.label_titulo.pack(pady=10)

        # Formulário de adicionar gastos
        self.frame_form = tk.Frame(master, bg='#000000')
        self.frame_form.pack(pady=20)

        # Campos de entrada para adicionar gastos
        self.label_data = tk.Label(self.frame_form, text="Data:", font=("Montserrat", 14), bg='#000000', fg='#FFFFFF')
        self.label_data.grid(row=0, column=0, pady=10, padx=10)
        self.entry_data = tk.Entry(self.frame_form, font=("Montserrat", 14), bg='#4E4E4E', fg='#FFFFFF')
        self.entry_data.grid(row=0, column=1, pady=10, padx=10)

        self.label_categoria = tk.Label(self.frame_form, text="Categoria:", font=("Montserrat", 14), bg='#000000', fg='#FFFFFF')
        self.label_categoria.grid(row=1, column=0, pady=10, padx=10)
        self.entry_categoria = tk.Entry(self.frame_form, font=("Montserrat", 14), bg='#4E4E4E', fg='#FFFFFF')
        self.entry_categoria.grid(row=1, column=1, pady=10, padx=10)

        self.label_descricao = tk.Label(self.frame_form, text="Descrição:", font=("Montserrat", 14), bg='#000000', fg='#FFFFFF')
        self.label_descricao.grid(row=2, column=0, pady=10, padx=10)
        self.entry_descricao = tk.Entry(self.frame_form, font=("Montserrat", 14), bg='#4E4E4E', fg='#FFFFFF')
        self.entry_descricao.grid(row=2, column=1, pady=10, padx=10)

        self.label_valor = tk.Label(self.frame_form, text="Valor:", font=("Montserrat", 14), bg='#000000', fg='#FFFFFF')
        self.label_valor.grid(row=3, column=0, pady=10, padx=10)
        self.entry_valor = tk.Entry(self.frame_form, font=("Montserrat", 14), bg='#4E4E4E', fg='#FFFFFF')
        self.entry_valor.grid(row=3, column=1, pady=10, padx=10)

        # Botão de adicionar gasto
        self.botao_adicionar = tk.Button(self.frame_form, text="Adicionar Gasto", font=("Montserrat", 14), bg='#4682B4', fg='#FFFFFF', command=self.adicionar_gasto)
        self.botao_adicionar.grid(row=4, column=0, columnspan=2, pady=10)

        # Botão de gerar relatório
        self.botao_relatorio = tk.Button(self.frame_form, text="Gerar Relatório", font=("Montserrat", 14), bg='#4682B4', fg='#FFFFFF', command=self.gerar_relatorio)
        self.botao_relatorio.grid(row=5, column=0, columnspan=2, pady=10)

        # Área de visualização dos gastos
        self.label_gastos = tk.Label(master, text="Gastos Recentes", font=("Montserrat", 18), bg='#000000', fg='#FFFFFF')
        self.label_gastos.pack(pady=(20, 0))

        self.frame_gastos = tk.Frame(master, bg='#000000')
        self.frame_gastos.pack(pady=10)

        self.tree_gastos = ttk.Treeview(self.frame_gastos, columns=('Data', 'Categoria', 'Descrição', 'Valor'), show='headings', height=10)
        self.tree_gastos.heading('Data', text='Data')
        self.tree_gastos.heading('Categoria', text='Categoria')
        self.tree_gastos.heading('Descrição', text='Descrição')
        self.tree_gastos.heading('Valor', text='Valor')
        self.tree_gastos.column('Data', anchor='center', width=100)
        self.tree_gastos.column('Categoria', anchor='center', width=100)
        self.tree_gastos.column('Descrição', anchor='center', width=200)
        self.tree_gastos.column('Valor', anchor='center', width=100)
        self.tree_gastos.pack()

        self.carregar_gastos()

    def adicionar_gasto(self):
        data = self.entry_data.get()
        categoria = self.entry_categoria.get()
        descricao = self.entry_descricao.get()
        valor = self.entry_valor.get()

        try:
            valor = float(valor)
            adicionar_gasto(self.usuario_id, data, categoria, descricao, valor)
            messagebox.showinfo("Sucesso", "Gasto adicionado com sucesso!")
            self.carregar_gastos()
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Por favor, insira um número.")

    def carregar_gastos(self):
        for i in self.tree_gastos.get_children():
            self.tree_gastos.delete(i)
        gastos = visualizar_gastos(self.usuario_id)
        for gasto in gastos:
            self.tree_gastos.insert('', 'end', values=gasto[2:])

    def gerar_relatorio(self):
        gastos = visualizar_gastos(self.usuario_id)
        df = pd.DataFrame(gastos, columns=['ID', 'Usuário', 'Data', 'Categoria', 'Descrição', 'Valor'])
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
        df.set_index('Data', inplace=True)
        df['Valor'] = df['Valor'].astype(float)

        # Gráfico de barras por categoria
        plt.figure(figsize=(10, 5))
        df.groupby('Categoria')['Valor'].sum().plot(kind='bar', color='#00BCD4')
        plt.title('Gastos por Categoria')
        plt.ylabel('Valor Total')
        plt.xlabel('Categoria')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

        # Gráfico de linha de gastos ao longo do tempo
        plt.figure(figsize=(10, 5))
        df.groupby(df.index)['Valor'].sum().plot(kind='line', color='#00BCD4', marker='o')
        plt.title('Gastos ao Longo do Tempo')
        plt.ylabel('Valor Total')
        plt.xlabel('Data')
        plt.grid()
        plt.tight_layout()
        plt.show()

# Execução do aplicativo
if __name__ == "__main__":
    criar_tabelas()
    root = tk.Tk()
    app = TelaLoginCadastro(root)
    root.mainloop()