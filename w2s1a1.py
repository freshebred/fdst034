scenario_question = ["Movie night: Enter your age: ", "Beach weather: What is the temperature? ", "Escape room: What is your score? (0-100) ","Theme park ride: What is your height in cm? ", "Food delivery: What is your order total? "]

def scenario(num):
    num = int(num)
    if not 1<=num<=5:
        return print("Invalid scenario option (choose 1-5)")
    else: 
        num = num-1
        match num:
            case 0:
                ans = int(input(scenario_question[num]))
                if ans >= 13:
                    print("You can buy a ticket")
                else: 
                    print("You cannot buy a ticket")
            case 1:
                ans = float(input(scenario_question[num]))
                if ans > 30:
                    print("It is too hot")
                elif ans >=20:
                    print("It is comfortable")
                else:
                    print("It is cool")
            case 2:
                ans = int(input(scenario_question[num]))
                if ans >= 90:
                    print("You get a GOLD badge")
                elif ans >=70:
                    print("You get a SILVER badge")
                elif ans >= 50:
                    print("You get a BRONZE badge")
                else:
                    print("You gotta try again")
            case 3:
                ans = int(input(scenario_question[num]))
                if ans >=120:
                    print("You can ride")
                else: 
                    print("you cannot ride")
            case 4:
                ans = int(input(scenario_question[num]))
                if ans >50:
                    print("Your delivery fee is $0")
                elif ans >=20:
                    print("Your delivery fee is $5")
                else:
                    print("Your delivery fee is $8")

    
scenario(int(input("Input scenario selection (1-5) ")))