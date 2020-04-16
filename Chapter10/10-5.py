#while循环的输入:

active = True
reason = []
filename = 'reasons.txt'
while True:
    why =input("why you like:")
    if why == 'quit':
        break
    else:
        reason.append(why)

with open(filename,'w') as file_object:
    for r in reason:
        file_object.write(r + "\n")

