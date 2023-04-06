from datetime import datetime

from store_database import article_list
from store_database import article_name_list


## Check validity of customer_number
def customer_number_validation():
    while True:
        error_message = "Please enter a positive integer between 0 and 100000"
        input_id = input("What is your customer number?")
        
        try:
            int_test = int(input_id)                        ## Test if the input is an interger
            if int_test < 0 or int_test > 100000:           ## Test if the input is between 0 and 100000
                raise ValueError(error_message)
            break
        except ValueError:
            print(error_message)
    input_id = int(input_id)                                ## Convert input into int
    return input_id


## Check the validity of the delivery_date
def delivery_date_validation():
    while True:
        error_message = "Enter the date using the dd/mm/yyyy format"
        input_date = input("Which day do you want your order to be delivered?")

        try:
            date_test = datetime.strptime(input_date, '%d/%m/%Y')       ## Test if the input is date using dd/mm/yyyy as a format
            break
        except ValueError:
            print(error_message)

    input_date = datetime.strptime(input_date, '%d/%m/%Y')              ## Transform input into the correct date type.
    input_date = input_date.date()
    return input_date


def order_validation():
    order_item_list = []
    order_quantity_list = []
    return order_item_list, order_quantity_list

## Planning: while True: 
##                  article_validation_step1
##                  quantity_validation_step1
##              break
##           while True:
##                  article_validation_step2
##                  quantity_validation_step2


## First step of the article validation. To be put inside a while True: loop.
## Before the first step of the quantity validation and before the second step of the article validation.
def article_validation_step1():
    order_item_list = order_validation()[0]
    print(order_item_list) ## FOr testing purpose
    print("pre-step of step 1") ## For testing purpose

    while True:
        # order_item_list = order_item_list
        error_message = "ERROR: PLEASE TYPE A VALID ARTICLE FROM THE LIST BELOW."
        
        print(article_name_list)  
        input_article = input("Select the item you wish to order from the list above: ")
        print()

        if input_article not in article_name_list:
            print()
            print(error_message)
        else:
            order_item_list.append(input_article)
            return order_item_list
        

## Second step of data validation
## Repeat the process until the customer wants to finish
def article_validation_step2():
    print("IS IT WHERE DOING STEP 1 A SECOND TIME?") ## FOR testing purpose

    order_item_list = article_validation_step1()
    error_message = "ERROR: PLEASE TYPE A VALID ARTICLE FROM THE LIST BELOW."
    while True:

        print(f"\n Do you want to order another item? \n {article_name_list}")
        input_article = input("If yes, please type a valid article from the list above \nOnce you are finish, please type 'done': ")

        if input_article not in article_name_list and input_article != "done":
            print()
            print(error_message)
        
        elif input_article in article_name_list:
            order_item_list.append(input_article)     

        elif input_article == "done":
            print(order_item_list) ## For testing purpose
            return order_item_list  
    

test = order_validation()
print(test)

    # input_number = input("How many items do you need?")

