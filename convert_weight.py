#Function convert_weight 
def convert_weight():
    #Welcome message to show that program started
    print ("Welcome to our weight conversion program")
    
    #Out loop for reapeating the entire program 
    while True: 
        #validate weight input
        valid_input = False 
        while not valid_input:
            try:
                #Ask user to enter weight
                weight = float(input("Enter the weight: "))
                print(f"Weight entered: {weight}")
                valid_input = True #input is valid, exit loop
            except ValueError:
                #This asks user to enter a number
                print("Invalid input for weight. Please enter a number.")
        
        #validate coversion type input    
        valid_input = False
        while not valid_input:
            try:
                #Ask user for conversion type
                conversion_type = int(input("1 = Kilograms to Pounds\n2 = Pounds to Kilograms\nEnter 1 or 2: ")) #Prompts user to enter 1 or 2 for converstion type 
                if conversion_type in [1,2]:
                    print(f"Conversion type chosen: {conversion_type}")
                    valid_input = True #input is valid, exit loop
                else:
                    print("Invalid selection, please choose 1 or 2.") #Asks user to input 1 or 2, after user has entered any other number instead
            except ValueError:
                print("Invalid input for conversion type. Please enter 1 or 2.") #Asks user to enter 1 or 2, user has entered in a non-numerical character
        
        #Perform conversion
        if conversion_type == 1:
            converted_weight = weight * 2.20462 
            print(f"{weight} Kilograms = {converted_weight: .2f} pounds.")
        else:
            converted_weight = weight / 2.20462
            print(f"{weight} pounds = {converted_weight: .2f} kilograms.")
            
        #Ask user if they want to restart or exit the program
        print("Would you like to perform another conversion? (y/n)")
        again = input().lower()
        if again == "n":
            print("Have a great day!") #Program ends 
            break 
        elif again != "y":
            print("Invalid input, exiting program.") #Program will end if user does not type y or n 
            break 
        
convert_weight()