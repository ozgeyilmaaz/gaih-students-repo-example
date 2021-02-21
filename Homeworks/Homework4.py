class hangman():

      def __init__(self):
            self.words = ["DEJAVU", "SISTER", "FLY", "MOON", "SPACE"]
            self.tries = 6
            self.stages = ["""
                      --------
                      |      |
                      |      O
                      |     \\|/
                      |      |
                      |     / \\
                      -
                      """,
              """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |     / 
              -
              """,
              """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |     
              -
              """,
              """
              --------
              |      |
              |      O
              |     \\|
              |      |
              |     
              -
              """,
              """
              --------
              |      |
              |      O
              |      |
              |      |
              |     
              -
              """,
              """
              --------
              |      |
              |      O
              |      
              |      
              |     
              -
              """,
              """
              --------
              |      |
              |      
              |      
              |      
              |   
              -  
              """
              ]
            print("WELCOME TO HANGMAN GAME")
            print(self.stages[self.tries])
            import random
            self.word = random.choice(self.words)
            print("_ " * len(self.word))


      def game(self, guess):
            again = "Y"
            guessed_letters = []
            guessed_words = []
            while again == "Y":

                  if len(self.words) == 0:
                        print("You have seen all the words contained in the game.")
                        print("----- THE END -----")

                  if len(guess) == len(self.word) and self.tries > 0:
                        if guess == self.word:
                              print("Congratulations! You won the game.")
                              self.words.remove(self.word)
                              guessed_letters.clear()
                              guessed_words.clear()
                              again = input("Do you want to play again? (Y/N): ").upper()
                              if again == "Y":
                                    import random
                                    self.word = random.choice(self.words)
                                    print("_ " * len(self.word))
                                    guess = input("Enter letter or word: ").upper()
                                    continue
                              else:
                                    break

                        elif guess in guessed_words:
                              print("You already guessed the word", guess)
                              guess = input("Enter letter or word again: ").upper()
                              continue


                        elif guess != self.word:
                              self.tries -= 1
                              print(self.stages[self.tries])
                              print(guess, "not the word.")
                              guessed_words.append(guess)
                              guess = input("Enter letter or word again: ").upper()
                              continue


                  elif len(guess) == 1 and self.tries > 0:
                        if guess in guessed_letters:
                              print("You already guessed the letter", guess)
                              guess = input("Enter letter or word again: ").upper()
                              continue

                        elif guess not in self.word:
                              self.tries -= 1
                              print(self.stages[self.tries])
                              print(guess, "is not in the letter.")
                              guessed_letters.append(guess)
                              guess = input("Enter letter or word again: ").upper()
                              continue

                        else:
                              print(f"Congratulations! {guess} is in the word.")
                              guessed_letters.append(guess)
                              if len(guessed_letters) == len(self.word):
                                    print("Congratulations! You found the word.")
                                    again = input("Do you want to play again? (Y/N): ").upper()
                                    if again == "Y":
                                          self.words.remove(self.word)
                                          guessed_letters.clear()
                                          guessed_words.clear()
                                          import random
                                          self.word = random.choice(self.words)
                                          print("_" * len(self.word))
                                          guess = input("Enter letter or word: ").upper()
                                          continue
                              else:
                                    guess = input("Enter letter or word again: ").upper()
                                    continue

                  elif self.tries <= 0:
                        print("GAME OVER")
                        guessed_letters.clear()
                        guessed_words.clear()
                        self.words.remove(self.word)
                        again = input("Do you want to play again? (Y/N): ")
                        if again == "Y":
                              import random
                              self.word = random.choice(self.words)
                              print("_" * len(self.word))
                              guess = input("Enter letter or word: ")
                              continue
                        else:
                              break

                  else:
                        print("Invalid guess.")
                        print("Be sure to try a word of the same length.")
                        guess = input("Enter letter or word: ")
                        continue



a = hangman()
hangman.game(a, input("Enter letter or word: ").upper())