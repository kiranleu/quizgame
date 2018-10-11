def show_menu():
    print("Quiz Game")
    print("**************************")
    print(" ")


    print("1. Run Quiz")
    print("2. Enter a Question")
    print("3. Exit")
    print(" ")

    option= input("Enter option: ")

    return option

def add_a_question():
     question = input("Enter a question: ")
     answer = input ("You are very clever human! Tell me," + question + " I know you know it!")
     
     with open("questions.txt", "a") as f:
         line = question + "|" + answer + "\n"
         f.write(line)

while True:
    option = show_menu()
    
    if option == "1":
        print("You picked to run the quiz")
    if option == "2":
        add_a_question()
       
    
    if option == "3":
      
        break
    
    