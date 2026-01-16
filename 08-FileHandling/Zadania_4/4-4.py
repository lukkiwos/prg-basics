with open('it_company.csv', 'r') as file:
    count = 0

    for line in file:
        print(line, end="")
        count += 1
    
        if count == 5:
            enter = input("\nType 'enter' to continue: \n")
            count = 0
        
    
