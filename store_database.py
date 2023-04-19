import pandas as pd
from input_validation_v3 import CustomerFormValidation
from datetime import datetime

class Article:
    """Create an and it's relevant information for the store database"""
    
    def __init__(self, name: str, id: int, price: int, section: str):
        assert type(name) == str
        self.name = name
        assert type(id) == int
        self.id = id
        assert type(price) == int
        self.price = price
        assert type(section) == str
        self.section = section

    def __repr__(self):
        ### Personal comment: __repr__ to be improved. Experiment to get a better understanding
        """Return a string representation of the object"""        
        return f"\nArticle: {', '.join(f'{attribute} = {value}' for attribute, value in vars(self).items() if not attribute.startswith('__') and not callable(getattr(self, attribute)))}" 




class ArticleList():
    """Create a list of article"""
    def __init__(self):
        self.article_list = []



    def __repr__(self):
        """Return a string representation of the object"""        
        return f"ArticleList: {', '.join(f'{attribute} = {value}' for attribute, value in vars(self).items() if not attribute.startswith('__') and not callable(getattr(self, attribute)))}" 

    def create_list(self, csv_file: str):
        """Create the list from a csv file"""
        self.csv_file = csv_file
        df = pd.read_csv(f"{self.csv_file}.csv")
        for index in range(0, df.shape[0]):
            temp = Article(df.iloc[index][0], int(df.iloc[index][1]), int(df.iloc[index][2]), df.iloc[index][3])
            self.article_list.append(temp)


    def display_name(self):
        """Create a list of name of all the articles in the class"""
        ## Useful information for the customer during his/her input phase.
        name_list = []
        for index in range(0, len(self.article_list)):
            name_list.append(self.article_list[index].name)
        self.name_list = name_list


class Store(ArticleList):
    """Create a store with an article_list from a csv file"""

    def __init__(self, csv: str):
        ArticleList.__init__(self)
        self.create_list(csv)
        self.display_name()        


class ArticleListCustomer(ArticleList):
    def __init__(self):
        ArticleList.__init__(self)
        self.article_list_customer = []

    ### Personal comment: Should all the methods below belong to ArticleListCustomer or CustomerForm?
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
        


class CustomerForm(ArticleListCustomer, CustomerFormValidation):
    def __init__(self):
        ArticleListCustomer.__init__(self)
        CustomerFormValidation.__init__(self)
        self.customer_order = {}

    def get_whole_customer_order(self):
        """Get all the information needed for the customer's order"""
        self.get_valid_customer_id()
        self.get_valid_delivery_date()
        self.get_all_articles()
        self.get_total_cost()
        self.display_order_summary()

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
        print(f"Your order will be delivered on the {self.delivery_date}")         

# a = CustomerForm()
# a.create_list("store database")
# a.display_name()
# print(a.__dict__)
# # a.get_valid_customer_id()
# # a.get_valid_delivery_date()
# # # # print(a.customer_id)
# # # # print(a.delivery_date)
# a.get_valid_article_name()
# print(a.temp_article_name)
# a.get_valid_article_quantity()
# print(a.temp_article_quantity)
# a.add_article_and_quantity()
# print(a.article_list_customer)

# a.get_valid_finished_order_status()
# print(f"finished_order_status is {a.finished_order_status}")

# a.get_whole_customer_order()
