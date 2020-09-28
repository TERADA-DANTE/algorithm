operations = input().split()
while len(operations) > 1:

    for i in range(len(operations)):
        if not operations[i].lstrip('-').isdigit():

            operator = operations.pop(i)
            a = int(operations.pop(i-1))
            b = int(operations.pop(i-2))
            if operator == '+':
                d = a+b
            elif operator == '-':
                d = b-a
            else:
                d = a*b
            operations.insert(i-2, str(d))
            break
print(operations[0])
