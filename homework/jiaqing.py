print("scissors paper stone is a 2-3 player game,"
      "scissors beat paper, paper beat stone and stone beat scissors.")
user_a_choice = input("which scissors/paper/stone?")
user_b_choice = input("which scissors/paper/stone?")
user_c_choice = input("which scissors/paper/stone/exit")
if user_c_choice == "scissors":
      if user_a_choice == "scissors" and user_b_choice == "scissors":
            print("none win")
      elif user_a_choice == "stone" and user_b_choice == "scissors":
            print("user a win")
      elif user_a_choice == "paper" and user_b_choice == "scissors":
            print("user a and user b win")
      elif user_a_choice == "scissors" and user_b_choice == "stone":
            print("user b win")
      elif user_a_choice == "scissors" and user_b_choice == "paper":
            print("user a and user c win")
      elif user_a_choice == "stone" and user_b_choice == "stone":
            print("user a and user b win")
      elif user_a_choice == "stone" and user_b_choice == "paper":
            print("none win")
      elif user_a_choice =="paper" and user_b_choice == "stone":
            print("none")
      elif user_a_choice == "paper" and user_b_choice == "paper":
            print("user c win")
      else:
            print("none win")
elif user_c_choice == "stone":
      if user_a_choice == "scissors" and user_b_choice == "scissors":
            print("user c win")
      elif user_a_choice == "stone" and user_b_choice == "scissors":
            print("user a and user c win")
      elif user_a_choice == "paper" and user_b_choice == "scissors":
            print("none win")
      elif user_a_choice == "scissors" and user_b_choice == "stone":
            print("user b and user c win")
      elif user_a_choice == "scissors" and user_b_choice == "paper":
            print("none win")
      elif user_a_choice == "stone" and user_b_choice == "stone":
            print("none win")
      elif user_a_choice == "stone" and user_b_choice == "paper":
            print("user b win")
      elif user_a_choice =="paper" and user_b_choice == "stone":
            print("user a win")
      elif user_a_choice == "paper" and user_b_choice == "paper":
            print("user a and user b win")
elif user_c_choice == "paper":
      if user_a_choice == "scissors" and user_b_choice == "scissors":
            print("user a and b win")
      elif user_a_choice == "stone" and user_b_choice == "scissors":
            print("none win")
      elif user_a_choice == "paper" and user_b_choice == "scissors":
            print("user b win")
      elif user_a_choice == "scissors" and user_b_choice == "stone":
            print("none win")
      elif user_a_choice == "scissors" and user_b_choice == "paper":
            print("user a win")
      elif user_a_choice == "stone" and user_b_choice == "stone":
            print("user c win win")
      elif user_a_choice == "stone" and user_b_choice == "paper":
            print("user b and user c win")
      elif user_a_choice =="paper" and user_b_choice == "stone":
            print("user a and user c win")
      elif user_a_choice == "paper" and user_b_choice == "paper":
            print("none win")
else:
      if user_a_choice == "scissors":
            if user_b_choice == "scissors":
                  print("none win")
            elif user_b_choice == "stone":
                  print("user b win")
            else:
                  print("user a win")
      elif user_a_choice == "stone":
            if user_b_choice == "scissors":
                  print("user a  win")
            elif user_b_choice == "stone":
                  print("none win")
            else:
                  print("user b win")
      else:
            if user_b_choice == "scissors":
                  print("user b  win")
            elif user_b_choice == "stone":
                  print("user a  win")
            else:
                  print("none win")
print("thank you for playing")
