
secret_Word = "giraffe"
guess = ""

guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_Word and not(out_of_guesses):
    if guess_count < guess_limit:

        guess = input("Enter Your Guess : ")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses, YOU LOSE ")
else:
    print("You Win")













