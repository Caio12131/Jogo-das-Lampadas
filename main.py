from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

# Passo 1: Definir as Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # Branca
co2 = "#3fb5a3"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra

# Passo 2: Criar a Janela Principal
janela = Tk()
janela.title("Jogo das Lâmpadas")
janela.geometry('400x260')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Passo 3: Criar os Frames
frame_cima = Frame(janela, width=500, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=250, bg=co4, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Passo 4: Configurar o Frame Superior
l_app = Label(frame_cima, text="Acenda as lâmpadas", height=1, anchor=NE, font=('Ivy 20 '), bg=co1, fg=co4)
l_app.place(x=5, y=5)

# Passo 5: Carregar Imagens
img_3 = Image.open('2.png').resize((40, 40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('3.png').resize((40, 40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('4.png').resize((40, 40))
img_5 = ImageTk.PhotoImage(img_5)

img_6 = Image.open('5.png').resize((40, 40))
img_6 = ImageTk.PhotoImage(img_6)

# Passo 6: Configurar o Frame Inferior
app_estado = Label(frame_baixo, image=img_3, compound=LEFT, relief="flat", bg=co4)
app_estado.place(x=30, y=10)

l_estado = Label(frame_baixo, text="Estou com medo", anchor=NW, font=('Ivy 13 '), bg=co4, fg=co1)
l_estado.place(x=80, y=20)

# Passo 7: Inicializar as Variáveis e Imagens
contador = 0
control = ['lampada_1', 'lampada_2', 'lampada_3']
lampada_on = '1.png'
lampada_off = '0.png'

img_lampada_on = Image.open(lampada_on).resize((110, 110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

img_lampada_off = Image.open(lampada_off).resize((110, 110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

l_lampada_1 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_lampada_1.place(x=5, y=70)

l_lampada_2 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_lampada_2.place(x=105, y=70)

l_lampada_3 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_lampada_3.place(x=200, y=70)

# Passo 8: Definir a Função para Ligar Lâmpadas
def ligar_lampada(i):
    global control

    # Desabilitar o botão após o clique
    if i[1] == 'Interuptor - 1':
        b_interuptor_1['state'] = 'disable'
    elif i[1] == 'Interuptor - 2':
        b_interuptor_2['state'] = 'disable'
    elif i[1] == 'Interuptor - 3':
        b_interuptor_3['state'] = 'disable'
    elif i[1] == 'Interuptor - 4':
        b_interuptor_4['state'] = 'disable'
    else:
        b_interuptor_5['state'] = 'disable'

    # Atualizar o controle
    def substituir_valor(i):
        global control
        nova_lista = []
        for string in control:
            novo_valor = string.replace(i[0], i[1])
            nova_lista.append(novo_valor)
        control = nova_lista

    # Selecionar valor na lista aleatoriamente
    valor_selecionado = random.choice([0, 1])
    print(valor_selecionado)

    if valor_selecionado == 1:
        if control[0] == 'lampada_1':
            l_lampada_1['image'] = img_lampada_on
            app_estado['image'] = img_4
            l_estado['text'] = 'Ok, obrigado!'
            substituir_valor(['lampada_1', str(1)])

        elif control[1] == 'lampada_2':
            l_lampada_2['image'] = img_lampada_on
            app_estado['image'] = img_5
            l_estado['text'] = 'Por favor, acenda também a última'
            substituir_valor(['lampada_2', str(2)])

        elif control[2] == 'lampada_3':
            l_lampada_3['image'] = img_lampada_on
            app_estado['image'] = img_6
            l_estado['text'] = 'Muito obrigado'
            substituir_valor(['lampada_3', str(3)])

# Passo 9: Adicionar os Botões de Interruptores
b_interuptor_1 = Button(frame_baixo, command=lambda i=['Interuptor - 1']: ligar_lampada(i), text="Interuptor - 1", bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_interuptor_1.place(x=300, y=50)

b_interuptor_2 = Button(frame_baixo, command=lambda i=['Interuptor - 2']: ligar_lampada(i), text="Interuptor - 2", bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_interuptor_2.place(x=300, y=80)

b_interuptor_3 = Button(frame_baixo, command=lambda i=['Interuptor - 3']: ligar_lampada(i), text="Interuptor - 3", bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_interuptor_3.place(x=300, y=110)

b_interuptor_4 = Button(frame_baixo, command=lambda i=['Interuptor - 4']: ligar_lampada(i), text="Interuptor - 4", bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_interuptor_4.place(x=300, y=140)

b_interuptor_5 = Button(frame_baixo, command=lambda i=['Interuptor - 5']: ligar_lampada(i), text="Interuptor - 5", bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_interuptor_5.place(x=300, y=170)

# Passo 10: Iniciar o Loop Principal
janela.mainloop()
