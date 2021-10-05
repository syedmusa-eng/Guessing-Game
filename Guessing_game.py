























secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("HINT! Tallest animal of the planet.")
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: \n")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loss!")
else:
    print("You win!")
