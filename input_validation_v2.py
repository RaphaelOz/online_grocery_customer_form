from datetime import datetime

from store_database import article_list
from store_database import article_name_list


class CustomerForm():
    # def __init__(self):
    #     pass

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

    def order_validation(self):
        self.order_item_list = []
        self.order_quantity_list = []

        # self.article_validation_step1()
        self.quantity_validation_step1()

    ## To be used inside order_validation() or make sure to initilise self.order_item_list = []
    def article_validation_step1(self):
        order_item_list = self.order_item_list
        
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
    
    ## To be used inside order_validation() or make sure to initilise self.order_quantity_list = []
    def quantity_validation_step1(self):
        order_quantity_list = self.order_quantity_list

        while True:
            error_message1 = "Please enter an integer between 1 and 10"
            error_message2 = "For bulk orders with more than 10 items, please call our office at +614-0000-0000"
            input_quantity = input("How many of the good selected previously do you want?")

            try:
                input_quantity = int(input_quantity)
                if input_quantity > 10:
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