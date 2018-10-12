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

         
def ask_questions():
    with open("questions.txt") as f:
         questions = f.read().split("\n")[:-1]
         
    score = 0
     
    for q in questions:
        qlist = q.split("|")
        
        # questions = q.split("|")[0]
        # answers = q.split("|")[1]
        
        quest, ans = qlist
        guess = input(quest)
        
        if guess.capitalize() == ans.capitalize():
            score +=1
    print ("Your score now is {0} out of {1}".format(score,len(qlist)))
            
         

def add_a_question():
     question = input("Enter a question: ")
     answer = input ("You are very clever human! Tell me," + question + " I know you know it!")
     
     with open("questions.txt", "a") as f:
         line = question + "|" + answer + "\n"
         f.write(line)

         

while True:
    option = show_menu()
    
    if option == "1":
        ask_questions()
        
       
    if option == "2":
        add_a_question()
       
    
    if option == "3":
      
        break
    
    