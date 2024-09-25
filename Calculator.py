logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculator(n1, n2,op):
    if op == '+':
        return float (n1) + float (n2)
    elif op == '-':
        return float (n1) - float (n2)
    elif op == '*':
        return float (n1) * float (n2)
    elif op == '/':
        return float(n1) / float (n2)
decision = 'n'
decisionb = 'restart'
while decisionb == 'restart' and decision == 'n':
    print(logo)
    decision = 'y'
    numbera = input("What's the first number?: ")
    while decision == 'y':
        operation = input("+\n-\n*\n/\nPick an operation: ")
        numberb = input("What's the next number?: ")
        solution = calculator(numbera,numberb,operation)
        print(f"{float(numbera)} {operation} {float(numberb)} = {float(solution)}")
        decision = input("Type 'y' to continue calculating with 15.0, or type 'n' to continue: ").lower()
        if decision == 'y':
            numbera = solution

    input("Alright. Type 'restart' to start a new calculation.").lower()

print("Goodbye! See you soon.")

