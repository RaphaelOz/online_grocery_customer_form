from datetime import datetime

from store_database import ArticleList
from input_validation_v3 import CustomerFormValidation


class CustomerForm(ArticleList, CustomerFormValidation):
    def __init__(self, store: str):
        ArticleList.__init__(self)
        # CustomerFormValidation.__init__(self)
        self.article_list = store.article_list
        self.name_list = store.name_list
        self.article_list_customer = []

    def get_whole_customer_order(self):
        """Get all the information needed for the customer's order"""
        self.get_valid_customer_id()
        self.get_valid_delivery_date()
        self.get_all_articles()
        self.get_total_cost()
        self.display_order_summary()

    def get_customer_id(self):
        """Get the customer_id from the customer"""
        self.customer_id = input("What is your customer number?")

    def get_delivery_date(self):
        """Get the delivery date from the customer"""
        self.delivery_date = input("Which day do you want your order to be delivered?")

    def get_article_name(self):
        """Get an article within ArticleList from the customer"""
        print(self.name_list)
        self.temp_article_name = input("Select the item you wish to order from the list above: ")

    def get_article_quantity(self):
        """Get a quantity for the temp_article_name"""      
        self.temp_article_quantity = input(f"How many of {self.temp_article_name} do you want?")

    def get_finished_order_status(self):
        """Ask the customer whether they want to stop ordering more items using finished attribute"""
        self.temp_finished_order_status = input("Do you wish to order more articles? \nIf yes, type: yes. \nIf no, type: no. ")


    def get_valid_customer_id(self):
        """Get a valid customer_id attribute by checking the error_status attribute"""
        while not hasattr(self, "error_status") or self.error_status == True:
            self.get_customer_id()
            self.customer_id_validation()
        delattr(self, "error_status")
        self.customer_id = int(self.customer_id)

    def get_valid_delivery_date(self):
        """Get a valid delivery_date attribute by check the error_status attribute"""
        while not hasattr(self, "error_status") or self.error_status == True:
            self.get_delivery_date()
            self.delivery_date_validation()
        delattr(self, "error_status")
        self.delivery_date = datetime.strptime(self.delivery_date, '%d/%m/%Y')
        self.delivery_date = self.delivery_date.date()

    def get_valid_article_name(self):
        """Get a valid article name from the name_list created by the display_name method"""
        while not hasattr(self, "error_status") or self.error_status == True:
            self.get_article_name()
            self.article_name_validation()
        delattr(self, "error_status")

    def get_valid_article_quantity(self):
        """Get a valid article quantity"""
        while not hasattr(self, "error_status") or self.error_status == True:
            self.get_article_quantity()
            self.article_quantity_validation()
        delattr(self, "error_status")    

    def get_valid_finished_order_status(self):
        """Get a valid finished order status which can be used to stop adding more articles to the order"""
        while not hasattr(self, "error_status") or self.error_status == True:
            self.get_finished_order_status()
            self.finished_order_validation()
        delattr(self, "error_status")


    def add_article_and_quantity(self):
        """Uses temp_article_name and temp_article_quantity to add the name, quantity and other details of the article to the article_list_customer"""
        # Search the index of the article_list which correspond to the temp_article_name
        for index in range(len(self.article_list)):
            if self.article_list[index].name == self.temp_article_name:

                # Add new article and its details to the article_list_customer and add its quantity 
                self.article_list_customer.append(self.article_list[index])

                # Stop loop once the new article has been added
                if self.article_list[index].name == self.temp_article_name:
                    break
        
        # Search the index of the article_list_customer which correspond to the temp_article_name
        for index2 in range(len(self.article_list_customer)):
            if self.article_list_customer[index2].name == self.temp_article_name:
                
                # Add quantity to the newly added article.
                self.article_list_customer[index2].quantity = self.temp_article_quantity


    def get_all_articles(self):
        """Order articles until the customer request to stop"""
        while not hasattr(self, "finished_order_status") or self.finished_order_status == True:
            self.get_valid_article_name()
            self.get_valid_article_quantity()
            self.add_article_and_quantity()
            self.get_valid_finished_order_status()

    def get_total_cost(self):
        """Calculate the total cost of the customer's order"""
        total_cost = 0

        for index in range(len(self.article_list_customer)):
            self.article_list_customer[index].cost = self.article_list_customer[index].price * self.article_list_customer[index].quantity
            total_cost += self.article_list_customer[index].cost
        
        self.total_cost = total_cost

    def display_order_summary(self):
        for index in range(len(self.article_list_customer)):
            print(f"You ordered {self.article_list_customer[index].quantity} {self.article_list_customer[index].name} at ${self.article_list_customer[index].price}/each for a total of ${self.article_list_customer[index].cost}")
        print(f"Total cost of the order: ${self.total_cost}")
        print(f"Your order will be delivered on the {self.delivery_date}")    ### Commented for test     
