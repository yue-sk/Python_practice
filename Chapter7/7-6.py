#使用标记

prompt = "\nTell me Pizza Toppings"
prompt += "\nEnter 'quit' end the program"

active = True

while active:
    message = input(prompt)

    if message =='quit':
        active = False
    else:
        print(message)