


you = "spongebob quarepants"
question = ""
yes = 0
no = 1
ready = False

def main():
    print("mother fucker")
    print("You don't get another chance!")
    print("this opportunity comes once in a lifetime")

while ready == False:
    if yes < no:
        print("It would seem that you are not ready!")
        question = input("are you ready now?")
        if question == ("im ready"):
            yes += 1
            no = 0
    else:
        ready = True


ready_combo_meter = 0


while ready == True:
    if yes > no:
        if ready_combo_meter != 0:
            print("you are still ready")
            question = input("Are you still ready?")
        if ready_combo_meter == 0:
            print("you are finally ready!")
            question = input("Are you still ready?")
            ready_combo_meter += 1
        if question != ("im ready"):
            yes = 0

    else:
        ready = False
        yes = 0
        ready_combo_meter = 0



print("whoops you aren't ready again!")
loop_back = input('want to try to be ready again? ')

while loop_back == ("im ready"):
    main()

print("you weren't ready anyway")

