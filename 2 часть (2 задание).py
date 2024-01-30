from tkinter import *
import random

root = Tk()
root.title("SCP")
root.config(background='#00FFFF')
root.geometry('650x450')
root.resizable(width=False, height=False)

labelText = Label(
    root,
    text='Играй;)',
    font=('Comic Sans MS', 17, 'bold'),
    bg='white',
    foreground='black',
    width=48,
    height=1
)

def SCP(player_choice):
    computer_choice = random.choice(['камень', 'ножницы', 'бумага'])
    if computer_choice == player_choice:
        labelText.config(text='{} vs {}, ничья!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    elif computer_choice == 'камень' and player_choice == 'бумага':
        labelText.config(text='{} vs {}, ты выиграл!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    elif computer_choice == 'бумага' and player_choice == 'камень':
        labelText.config(text='{} vs {}, компьютер выиграл!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    elif computer_choice == 'камень' and player_choice == 'ножницы':
        labelText.config(text='{} vs {}, компьютер выиграл!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    elif computer_choice == 'ножницы' and player_choice == 'камень':
        labelText.config(text='{} vs {}, ты выиграл!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    elif computer_choice == 'ножницы' and player_choice == 'бумага':
        labelText.config(text='{} vs {}, компьютер выиграл!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    elif computer_choice == 'бумага' and player_choice == 'ножницы':
        labelText.config(text='{} vs {}, ты выиграл!'.format(str(computer_choice).upper(), str(player_choice).upper()))
    else:
        labelText.config(text="It's impossible;)")

labelText.pack()
stone = Button(root,
               text='камень',
               command=lambda: SCP('камень'),
               font=('Comic Sans MS', 15, 'bold'),
               bg='red',
               foreground='green',
               activebackground='green',
               activeforeground='red',
               width=15,
               height = 2
               )
stone.pack()
scissors = Button(root,
               text='ножницы',
               command=lambda: SCP('ножницы'),
               font=('Comic Sans MS', 15, 'bold'),
               bg='yellow',
               foreground='red',
               activebackground='red',
               activeforeground='yellow',
               width=15,
               height = 2
               )
scissors.pack()
paper = Button(root,
               text='бумага',
               command=lambda: SCP('бумага'),
               font=('Comic Sans MS', 15, 'bold'),
               bg='green',
               foreground='yellow',
               activebackground='yellow',
               activeforeground='green',
               width=15,
               height = 2
               )
paper.pack()
root.mainloop()
