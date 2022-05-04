#Author: Jaevanie Ferguson
#Date Created: May 2, 2022
#Course: ITT103
#Purpose: To calculate and print the commission received by a salesperson at JAMEx

sales_num = '1' #Set salesperson number variable to preset value so the while condition triggers
while sales_num != '0': #Program will continue as long as user does not enter 0 for salesperson number
    valid_sales_num = False
    while(not valid_sales_num):
        
        sales_num = input('Enter salesperson number (enter 0 to close the program): ')
        if(sales_num.strip() == ''):
            print('Error: Salesperson number cannot be empty')
        else:
            valid_sales_num = True
            
    if(sales_num != '0'):
        
        valid_sales_amt = False
        while(not valid_sales_amt): #Continue requesting sales amount until a valid input is entered
            sales_amt = input('Enter sales amount: ')
            try:
                float(sales_amt) #Check if input can be converted to float to denote that the sales amount is valid
            except ValueError:                
                print('Error: Invalid sales amount')
            else:
                valid_sales_amt = True
        
        valid_class = False
        while(not valid_class): #Continue requesting class until a valid input is entered
            class_ = input('Enter class (a digit from 1 to 3): ')
            try:
                int(class_) #Check if input can be converted to integer to denote that the class is valid
            except ValueError:
                print('Error: Class must be a digit from 1 to 3')
            else:
                valid_class = True

            if(valid_class):
                sales_amt = float(sales_amt) #Change sales amount to float for calculation
                match int(class_): #Use match to process the results of different class values
                    case 1:
                        if(sales_amt <= 1000):
                            rate = 6
                        elif sales_amt < 2000:
                            rate = 7
                        else:
                            rate = 10
                    case 2:
                        if sales_amt < 1000:
                            rate = 4
                        else:
                            rate = 6
                    case 3:
                        rate = 4.5
                    case _: #Print error message if class is not digit from 1 to 3
                        print('Error: Class must be a digit from 1 to 3')
                        valid_class = False #Set variable to false to allow program to continue prompting for valid class input

                if(valid_class):
                    commission = sales_amt * rate / 100 #Calculate commission after valid class entered and rate determined
                    print('Commission for salesperson ' + sales_num + ' is $' + str(round(commission,2))) #Print commission for salesperson to two decimal places
                    
print('Program terminated.') #Print program termination message to user
