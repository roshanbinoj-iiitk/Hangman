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
    word = data[random.randint(0, len(data) - 1)][0]
    db.close()
    # Creating a list of underscores to represent the word
    word_ = list('_' * len(word))
    
    while lives_lost < 8:
        cls() 
        print(lifelost(lives_lost))  
        print(word_)  # Print current guessed state
        letter = human_pc_gameplay1(word_, lives_lost, guessed_chars)[0]
        
        if letter not in guessed_chars:
            guessed_chars.append(letter)
            
        if letter in word:
            # Replacing underscores with the correct letter
            for i in range(len(word)):
                if word[i] == letter:
                    word_[i] = letter
        else:
            lives_lost += 1 
        
        if word_ == list(word):  
            human_pc_game_win(True, word, lives_lost)  # Win message
            break
            
        if lives_lost == 8: 
            cls()
            lifelost(lives_lost)
            human_pc_game_win(False, word, lives_lost)  # Loss message

def human_pc():  # Computer guessing
    lives_lost = 0
    used_chars = []
    unused_chars = []
    char_var = 0
    word_length = int(get_no_letters()[0])  # Get number of letters
    word = list('_' * word_length)

    def get_rnd_char(char_var):
        if char_var < 4:
            return random.choice(common_chars1)
        return educated_guess(word, unused_chars, used_chars)  # Defined in dbcon.py

    while lives_lost < 8:
        cls()  
        print(lifelost(lives_lost)) 
        print(word)
        rnd_char = get_rnd_char(char_var)
        
        if rnd_char is None or rnd_char in used_chars:
            continue 
        
        char_var += 1  
        used_chars.append(rnd_char)
        
        wrd_txt = f'Is {rnd_char} present in the word? (Y/N)'
        a, b = game_play(word, wrd_txt)
        
        if b:  # Letter is present
            for i in a:
                word[i - 1] = rnd_char  # Update the word state
            
            word_list = filter_out(word, unused_chars)
            if len(word_list) == 1:  # Only one possibility remains
                human_pc_game_win(True, word_list[0], lives_lost, 'I')  
                break
        else:  # Letter is not present
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

        # Check if the word is completely guessed
        if '_' not in word:  
            cls()  # Clear the screen before showing the win message
            print("The computer has guessed the word:", ''.join(word))  # Show the guessed word
            human_pc_game_win(True, ''.join(word), lives_lost, 'I')  # GUI function to display win message
            break

    if lives_lost == 8:  
        cls()
        print(lifelost(lives_lost))
        print(word)
        c_word = human_pc_game_win(False, word, lives_lost, 'I')  
        if c_word:
            learn_word(c_word[0])  # Learn the word if guess was wrong
