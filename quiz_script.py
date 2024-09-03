# Quiz game 
# This is a quiz game about basic computer knowledge
# Made by kenny tang 
# Check my github in github.com/k3nnytang

print('''      ================================================

       Welcome to My Simple Computer Knowledge Quiz !
      
      ================================================
      '''
      )

input_answer = input('Do you want to start the game (y/n) ? ')

while input_answer != "y" :

    if input_answer == "n":
        print('''
              =========================

              Okay, See you Next Time !
              
              =========================
              ''')
        quit()

    elif input_answer == 'y':
        break

    print("\nPlease type either 'y' for yes or 'n' for no")
    input_answer = input("(y/n) : ") 

print("\n Alright, Let's Start with The First Question \n")
score = 0

def key(x,y:str):
    global score
    if x.lower() == y:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

answer1 = input("What does 'CPU' stand for ? ")
key(answer1,"central processing unit")

answer2 = input("What does 'RAM' stand for ? ")
key(answer2,"random access memory")

answer3 = input("What does 'GPU' stand for ? ")
key(answer3,"graphics processing unit")

answer4 = input('''
Which device is used to input text into a computer?

A) Monitor
B) Mouse
C) Keyboard
D) Printer

 Answer (A/B/C/D) : ''')
key(answer4,'c')

answer5 = input('''
What is the main function of a computer's operating system?

A) To run software programs
B) To provide internet access
C) To store files
D) To display websites

 Answer (A/B/C/D) : ''')
key(answer5,'a')

print(f"You got {score} questions correct ! ")
print(f"You got {score/5 *100}% ! \n")
print("\n=== Thanks For Playing ! ===\n")


