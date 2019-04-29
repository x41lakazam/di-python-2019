import random


class Hangman:

    def __init__(self):
        file = open("words.txt", 'r')
        self.words = file.readlines()
        file.close()

    def play(self):
        self.lives = 5
        self.used_letters = []
        self.word_to_guess = self.generate_random_word(self.words)
        self.encrypted_word = self.encrypt_word(self.word_to_guess)

        while True:
            self.print_state()
            self.turn()
            print("\n\n")
            if self.check_win() or self.check_no_lives():
                again = input("Do you wanna play again?[Y/n]\n$ ")
                if again.lower() == 'y':
                    self.play()
                else:
                    print("Thanks, bye.")
                break

    def print_state(self):
        print("Word: {} || {} lives".format(self.encrypted_word, self.lives))
        print("Used letters: {}".format(self.used_letters))

    def check_win(self):
        if self.encrypted_word.upper() == self.word_to_guess.upper():
            print("You won with {} lives, the word was {}".format(self.lives, self.word_to_guess))
            return True
        else:
            return False

    def check_no_lives(self):
        if self.lives >= 0:
            return False
        else:
            print("You lose, the word was {}".format(self.word_to_guess))
            return True

    def turn(self):
        while True:
            user_letter = input("Choose a letter\n$ ").upper()
            if user_letter in self.used_letters:
                print("{} was already used.".format(user_letter))
                print("Used letters: {}".format(self.used_letters))
            else:
                break

        self.used_letters.append(user_letter)

        if user_letter in self.word_to_guess:
            self.decrypt_word(user_letter)
            print("Right, {} was in the word".format(user_letter))
            return True
        else:
            self.lives -= 1
            print("Sorry, {} was not in the word".format(user_letter))
            return False

    def generate_random_word(self, list_of_words):
        random_word = random.choice(list_of_words)
        return random_word.upper()

    def decrypt_word(self, char_to_decrypt):
        new_encrypted_word = ""
        i = 0
        for letter in self.word_to_guess:
            if letter == char_to_decrypt:
                new_encrypted_word += char_to_decrypt
            else:
                new_encrypted_word += self.encrypted_word[i]
            i += 1
        self.encrypted_word = new_encrypted_word

        return self.encrypted_word

        # With a list

    #         self.encrypted_word = list(self.encrypted_word)
    #         for ix in range(len(self.encrypted_word)):
    #             if self.word_to_guess[ix] == char_to_decrypt:
    #                 self.encrypted_word[ix] = char_to_decrypt
    #         self.encrypted_word = ''.join(self.encrypted_word)

    #         return self.encrypted_word

    def encrypt_word(self, word_to_encrypt):
        encrypted_word = "_" * len(word_to_encrypt)
        return encrypted_word
