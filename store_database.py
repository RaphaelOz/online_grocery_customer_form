import pandas as pd
from input_validation_v3 import CustomerFormValidation

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
