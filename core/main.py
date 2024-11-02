from core.dbcon import *
from core.gui import *
import random

def cls():
    print("\n")
    

def pc_human():
    guessed_chars = []
    lives_lost = 0
    # Establishing database connection
    db, cur = db_con_()
    # Fetching words from the database
    cur.execute('SELECT * FROM words')
    data = cur.fetchall()
    # Selecting a random word
    word = data[random.randint(0, len(data))][0]
    db.close()
    # Creating a list of underscores to represent the word so that LIKE operator can be used moving forward
    word_ = list('_' * len(word))
    while lives_lost < 8:
        cls() 
        print(lifelost(lives_lost))  
        print(word)
        letter = human_pc_gameplay1(word_, lives_lost, guessed_chars)[0]
        if letter not in guessed_chars:
            guessed_chars.append(letter)
        if letter in word:
            # Replacing underscores with the correct letter
            for i in range(0, len(word)):
                if word[i] == letter:
                    word_[i] = letter
        else:
            lives_lost += 1 
        if word_ == list(word):  
            human_pc_game_win(True, word, lives_lost) #gui function to display win message #refer gui.py
            break
        if lives_lost == 8: 
            cls()
            lifelost(lives_lost)
            human_pc_game_win(False, word, lives_lost)  # gui funtion to display loss message #refer gui.py

def human_pc():#computer guessing
    lives_lost = 0
    used_chars = []
    unused_chars = []
    char_var = 0
    word_length = int(get_no_letters()[0]) # for definition of get_no_letters() refer gui.py
    word = list('_' * word_length)

    def get_rnd_char(char_var):
        if char_var < 4:
            char = random.choice(common_chars1)
        else:
            char = educated_guess(word, unused_chars, used_chars)#defined in dbcon.py
        return char

    # Main game loop
    while lives_lost < 8:
        cls()  
        print(lifelost(lives_lost)) 
        print(word)
        rnd_char = get_rnd_char(char_var)
        if rnd_char in used_chars:
            continue 
        char_var += 1  
        used_chars.append(rnd_char)
        wrd_txt = f'Is {rnd_char} present in the word? (Y/N)'
        a, b = game_play(word, wrd_txt)
        if b:  
            for i in a:
                # Replacing underscores with the correct letter
                word[i - 1] = rnd_char
            word_list = filter_out(word, unused_chars)
            if len(word_list) == 1:  # Checking if only one word possibility remains
                human_pc_game_win(True, word_list[0], lives_lost, 'I')  
                break
        else:
            unused_chars.append(rnd_char)
            lives_lost += 1  
        if lives_lost == 7:  
            cls()
            print(lifelost(lives_lost))
            print(word)
            word_list = filter_out(word, unused_chars)
            if len(word_list) > 0: 
                c = game_play_word_check(word_list[0])[0]
                if c.lower() == 'y':
                    human_pc_game_win(True, word_list[0], lives_lost, 'I')  
                    break
                else:
                    lives_lost += 1 
                    break
    if lives_lost == 8:  
        cls()
        print(lifelost(lives_lost))
        print(word)
        c_word = human_pc_game_win(False, word, lives_lost, 'I')  
        if c_word != []:
            learn_word(c_word[0])  # Learning the word if guess was wrong