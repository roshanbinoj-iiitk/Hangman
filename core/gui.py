import tkinter as tk

# === Props ===
bg = '#4c00e6'
btn_bg = btn_active_fg = 'black'
btn_fg = btn_active_bg = '#884dff'
text_bg = '#aa80ff'
text_col = '#19004d'
# ===

# Function to get the number of letters from the user
def get_no_letters():
    a = []
    hangman = tk.Tk()
    hangman['background'] = bg

    getvar = tk.StringVar()

    def done():
        no_of_letters = getvar.get()
        a.append(no_of_letters)
        hangman.destroy()

    string1 = tk.Label(text='Enter the number of letters', bg=text_bg, fg=text_col, font=("Arial", 13))
    string1.place(x=10, y=5)
    tk.Entry(textvariable=getvar).place(x=10, y=30)
    tk.Button(text="Ok", command=done, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=55)
    tk.Button(text="QUIT", command=exit, bg='black', fg='#f2665c', activebackground='#f2665c').place(x=10, y=250)
    hangman.title("Hangman solver")
    hangman.geometry("750x300")
    hangman.mainloop()
    return a

# Function for the human-player gameplay
def game_play(word, wrd_txt):
    a = []
    hangman = tk.Tk()
    hangman['background'] = bg

    getvar = tk.StringVar()

    def done():
        positions = getvar.get()
        a.append(eval(positions + ','))
        a.append(True)
        hangman.destroy()

    def yes():
        string1 = tk.Label(text='At what positions?', bg=text_bg, fg=text_col, font=("Arial", 13))
        string1.place(x=10, y=110)
        tk.Entry(textvariable=getvar).place(x=10, y=140)
        tk.Button(text="Ok", command=done, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=170)

    def no():
        a.append(' ')
        a.append(False)
        hangman.destroy()

    wordstr = ''
    for i in word:
        wordstr = wordstr + ' ' + i

    tk.Label(text=wordstr, bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=80)
    tk.Label(text=wrd_txt, bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=5)
    tk.Button(text="Yes", command=yes, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=40)
    tk.Button(text="No", command=no, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=140, y=40)
    tk.Button(text="QUIT", command=exit, bg='black', fg='#f2665c', activebackground='#f2665c').place(x=10, y=250)
    hangman.title("Hangman Solver")
    hangman.geometry('750x300')
    hangman.mainloop()
    return a[0], a[1]

# Function to check if the guessed word is correct
def game_play_word_check(word):
    a = []
    hangman = tk.Tk()
    hangman['background'] = bg

    def yes():
        hangman.destroy()
        a.append('y')

    def no():
        hangman.destroy()
        a.append('n')

    string1 = tk.Label(text=f'Is the word {word}?', bg=text_bg, fg=text_col, font=("Arial", 13))
    string1.place(x=10, y=10)
    tk.Button(text="Yes", command=yes, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=40)
    tk.Button(text="No", command=no, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=140, y=40)
    tk.Button(text="QUIT", command=exit, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=250)
    hangman.title("Hangman Solver")
    hangman.geometry('750x300')
    hangman.mainloop()
    return a

# Function for the intro screen to choose between human or computer play
def pc_h_intro():
    a = []
    hangman = tk.Tk()
    hangman['background'] = bg

    def yes():
        a.append('1')
        hangman.destroy()

    def pc_play():
        a.append('2')
        hangman.destroy()

    string1 = tk.Label(text="What do you want to do today?", bg=text_bg, fg=text_col, font=("Arial", 13))
    string1.place(x=10, y=5)
    tk.Button(text="Play hangman", command=yes, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=45)
    tk.Button(text="Let the computer play :)", command=pc_play, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=85)
    tk.Button(text="EXIT", command=exit, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=125)
    hangman.title("Hangman")
    hangman.geometry('750x300')
    hangman.mainloop()
    return a

# Function for human-player gameplay
def human_pc_gameplay1(word, rem_lives, asked_chars):
    d = ''
    wrd = ''
    for i in asked_chars:
        d += f'{i},'
    a = []
    for i in word:
        wrd += f'{i} '

    hangman = tk.Tk()
    hangman['background'] = bg

    getvar = tk.StringVar()

    def done():
        letter = getvar.get()
        a.append(letter)
        hangman.destroy()

    tk.Label(text=f'{8-rem_lives} lives remaining || Asked chars: {d}', bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=5)
    tk.Label(text=f'Word Length: {len(word)}', bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=30)
    tk.Label(text=f'{wrd}', bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=55)
    entry = tk.Entry(textvariable=getvar).place(x=10, y=90)
    tk.Button(text="Ok", command=done, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=115)
    tk.Button(text="QUIT", command=exit, bg='black', fg='#f2665c', activebackground='#f2665c').place(x=10, y=250)
    hangman.title("Play Hangman")
    hangman.geometry("750x300")
    hangman.mainloop()
    return a

# Function to display game result for human vs. computer gameplay
def human_pc_game_win(status, word, lives_lost, person="You"):
    a = []
    if status == True:
        msg = f"{person} Won!!.. The Word is {word}"
    else:
        if person == 'You':
            msg = f"{person} Lost.. The word is {word}"
        elif person == 'I':
            msg = f"{person} Lost.."
    hangman = tk.Tk()
    getvar = tk.StringVar()

    def done():
        w0rd = getvar.get()
        a.append(w0rd)
        hangman.destroy()

    hangman['background'] = bg
    tk.Label(text=msg, bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=0)
    tk.Label(text=f'{lives_lost} lives lost out of 8', bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=25)
    if person == 'I' and status == False:
        tk.Label(text='May I know what the word was?', bg=text_bg, fg=text_col, font=("Arial", 13)).place(x=10, y=50)
        entry = tk.Entry(textvariable=getvar).place(x=10, y=75)
        tk.Button(text="OK", command=done, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=110)
    tk.Button(text="Play Again", command=hangman.destroy, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=175)
    tk.Button(text="EXIT", command=exit, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg).place(x=10, y=205)
    hangman.title("Play Hangman")
    hangman.geometry("750x300")
    hangman.mainloop()
    return a

# Function to handle life lost
def lifelost(life_no):
    if life_no == 0:
        return 0
    elif life_no == 1:
        return 1
    elif life_no == 2:
        return 2
    elif life_no == 3:
        return 3
    elif life_no == 4:
        return 4
    elif life_no == 5:
        return 5
    elif life_no == 6:
        return 6
    elif life_no == 7:
        return 7
    elif life_no == 8 or life_no == 9:
        return 8

                                                                                                                        
                                                                                                                        



