### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style


# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace=False):

  # If it's not in the word, display it with a red background
  if (not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if (isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")


# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in actual:

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if (letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")


# TO-DO: Write a Function that takes in a six-lettered word from the user
def the6letter():
  save = ""
  while (len(save) != 6):
    save = input("please enter a 6 letter word: ")
  return save


# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

# TO-DO: Write the logic of the game here!

print(
    r"""##      ##  #######  ########  ########     ########  ##          ###    ##    ## 
##  ##  ## ##     ## ##     ## ##     ##    ##     ## ##         ## ##    ##  ##  
##  ##  ## ##     ## ##     ## ##     ##    ##     ## ##        ##   ##    ####   
##  ##  ## ##     ## ########  ##     ##    ########  ##       ##     ##    ##    
##  ##  ## ##     ## ##   ##   ##     ##    ##        ##       #########    ##    
##  ##  ## ##     ## ##    ##  ##     ##    ##        ##       ##     ##    ##    
 ###  ###   #######  ##     ## ########     ##        ######## ##     ##    ##    """
)

print()

print("welcome to word play!")
print("======================")
print("you have 5 tries to get the correct word")
print(
    "The word is FIVE CHARACTERS long, and you must enter a guess of this length"
)
print("If a letter is in the correct place, it will be green")
print(
    "If a letter is in the word but NOT in the correct place, it will be yellow"
)
print("the letter is NOT in the word, it will be red")

print()

# Create secret word for user to guess
attempts = 6
secretWord = "bullet"

#  While user still has guesses
while attempts > 0:

  # that guess will check against secret word
  userGuess = the6letter()

  printGuessAccuracy(userGuess, secretWord)

  print()

  # If user wins

  if (userGuess == secretWord):
    print("Congratulations! You're a true wordsmith!")
    break

  attempts -= 1

  # if user loses
  if attempts == 0:
    print(f"Game over! Better luck next time! The word was: {secretWord} ")

