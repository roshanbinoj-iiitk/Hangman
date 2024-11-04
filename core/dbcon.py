import mysql.connector as cn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database credentials
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')

def db_con_():
    """Creating a database connection and returning the connection and cursor objects."""
    try:
        db = cn.connect(host='localhost', database="hangman", user=db_user, passwd=db_pass, charset="utf8")
        cur = db.cursor()
        return db, cur
    except cn.Error as e:
        print(f"Error connecting to database: {e}")
        return None, None

def initial_setup():
    """Initial setup for the database and table creation."""
    if not os.path.exists('./core/.done'):
        print("Setting up the database...")
        db = cn.connect(host='localhost', user=db_user, passwd=db_pass, charset='utf8')
        cur = db.cursor()
        cur.execute('CREATE DATABASE IF NOT EXISTS hangman')
        cur.execute('USE hangman')
        cur.execute('CREATE TABLE IF NOT EXISTS words (word VARCHAR(50))')

        # Ensure words.txt file exists
        if os.path.exists('./core/words.txt'):
            with open('./core/words.txt') as file:
                words = [word.strip() for word in file if word.strip()]  # Strip whitespace and avoid empty lines
                cur.executemany('INSERT INTO words (word) VALUES (%s)', [(word,) for word in words])
            db.commit()
        else:
            print("Error: words.txt file not found.")
        
        db.close()
        open('./core/.done', 'w').close()
        print("Database setup complete.")

def learn_word(word):
    """Learn a new word by inserting it into the database."""
    db, cur = db_con_()
    if cur is None:
        return
    
    cur.execute('INSERT INTO words (word) VALUES (%s)', (word,))
    print("Word learnt.")
    db.commit()
    db.close()

def filter_out(word, trash_chars):
    """Filter out words based on the provided characters."""
    new_word = ''.join(word)
    db, cur = db_con_()
    if cur is None:
        return []

    cur.execute('SELECT word FROM words WHERE word LIKE %s', (new_word,))
    filtered_words = [i[0] for i in cur.fetchall()]
    db.close()
    
    # Filter out words that contain any of the trash characters
    return [w for w in filtered_words if not any(char in w for char in trash_chars)]

common_chars1 = ['a', 'e', 'o', 'i']

def educated_guess(word, trash_chars, used_chars):
    # Initialize a dictionary to count letter occurrences
    letter_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    
    # Join the word into a string (not necessary, but for clarity)
    new_word = ''.join(word)

    # Fetch potential words from the database
    db, cur = db_con_()
    cur.execute(f'SELECT word FROM words WHERE word LIKE "{new_word}";')
    filtered_words = [row[0] for row in cur.fetchall()]
    db.close()

    # Remove words that have letters in the trash_chars
    filtered_words = [w for w in filtered_words if not any(char in trash_chars for char in w)]

    # Count occurrences of each letter in the remaining words
    for w in filtered_words:
        for char in w:
            if char not in used_chars and char not in trash_chars:
                letter_count[char] += 1

    # Determine the letter with the maximum count
    var = max(letter_count, key=letter_count.get, default=None)

    # Return the most frequent letter found, or None if all are used or trash
    return var if letter_count[var] > 0 else None