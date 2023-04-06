from datetime import datetime

from store_database import article_list
from store_database import article_name_list

# Personal comment: Should I do a list of dictionaries instead of 
# 2 lists of order_item_list and order_quantity_list?

# The dictionaries would have article_name and quantity as keys.


class CustomerForm():

    def order_validation(self):
        self.customer_number_validation()
        self.delivery_date_validation()

        while not hasattr(self, "break_loop"):
            self.article_validation()
            self.quantity_validation()

    ## Check validity of customer_number
    def customer_number_validation(self):
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
        self.customer_id = input_id

    ## Check the validity of the delivery_date
    def delivery_date_validation(self):
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
        self.delivery_date = input_date





    def article_validation(self):

        ## Create an empty list for self.order_item_list if the attribute does not exist for the first loop
        if not hasattr(self, "order_item_list"):
            self.order_item_list = []
        else:
            pass

        order_item_list = self.order_item_list
        
        ## If this is the first item
        if order_item_list == []:
            while True:
                error_message = "ERROR: PLEASE TYPE A VALID ARTICLE FROM THE LIST BELOW."

                print(article_name_list)
                input_article = input("Select the item you wish to order from the list above: ")
                print()

                if input_article not in article_name_list:
                    print()
                    print(error_message)
                else:
                    order_item_list.append(input_article)
                    self.order_item_list = order_item_list
                    break

        ## If it already has items, add more items to the list
        else:
            while True:
                error_message = "ERROR: PLEASE TYPE A VALID ARTICLE FROM THE LIST BELOW."
                
                print(f"\n Do you want to order another item? \n {article_name_list}")
                input_article = input("If yes, please type a valid article from the list above \nOnce you are finish, please type 'done': ")

                if input_article not in article_name_list and input_article != "done":
                    print()
                    print(error_message)
                
                elif input_article in article_name_list:
                    order_item_list.append(input_article)
                    self.order_item_list = order_item_list
                    break     

                elif input_article == "done":
                    self.break_loop = "done"
                    break

    
    ## Accept the number of the item for a previously chosen article.
    def quantity_validation(self):

        ## Create an empty list for self.order_quantity_list if the attribute does not exist for the first loop
        if not hasattr(self, "order_quantity_list"):
            self.order_quantity_list = []
        else:
            pass

        order_quantity_list = self.order_quantity_list

        ## Stop the function if the attribute break_loop was created.
        if hasattr(self, "break_loop"):
            pass

        ## Accept the customer input as the quantity of items required.
        else:
            while True:
                error_message1 = "Please enter an integer between 1 and 10"         ## Name of variable can be improved
                error_message2 = "For bulk orders with more than 10 items, please call our office at +614-0000-0000"        ## Name of variable can be improved
                input_quantity = input("How many of the good selected previously do you want?")

                try:
                    input_quantity = int(input_quantity)
                    if input_quantity > 10:
                        print(error_message1)
                        print(error_message2)
                    else:
                        break

                except ValueError:
                    print(error_message1)
            
            input_quantity = int(input_quantity)
            order_quantity_list.append(input_quantity)
            self.order_quantity_list = order_quantity_list





order = CustomerForm()
# order.customer_number_validation()
# order.delivery_date_validation()

order.order_validation()
print(order.__dict__)