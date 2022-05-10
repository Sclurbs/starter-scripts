

def main():  # defines the area in indents that will be triggered with main()#
    print('hi')
    print("hi")

question = ""
yes = 0
no = 1
ready = False


while ready == False:
    if yes < no:
        print("It would seem that you are not ready!")
        question = input("are you ready now?")
        if question == ("yes"):
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
        if question != ("yes"):
            yes = 0

    else:
        ready = False
        yes = 0
        ready_combo_meter = 0



print("you aren't ready again!")
loop_back = input('LOOP ')

if loop_back == ("yes"):
    main()



main()