class Product:
    """Create a good and it's relevant information for the database"""
    
    def __init__(self, name: str, id: int, price: float, section: str):
        assert type(name) == str, "Wrong type define for name"
        self.name = name
        self.id = id
        self.price = price
        self.section = section
        self.quantity = 0
    
    def set_quantity(self, quantity):
        self.quantity = quantity

class ArticleList:
    def __init__(self):
        self.article_list = []

    def add_item(self, item: Product):
        """Add item to article list"""
        self.article_list.append(item)

    def remove_item(self):
        pass

    def display_list(self):
        for item in self.article_list:
            print(item.name)
    
    
class ArticleListShop(ArticleList):
    def __init__(self, magasin_name):
        ArticleList.__init__(self)
        self.shop = magasin_name

class ArticleClient(ArticleList):
    def __init__(self, client_name):
        ArticleList.__init__(self)
        self.client = client_name

    def checkout(self):
        print("Paid!")



list_article = ArticleList()

## Creating the list of articles available for purchase.
# fichier = pd.read_csv("product_list.csv")
# for index, row in fichier.iterrows():
#     list_article.add_item(Product(row.name, row.id, row.price, row.section))
list_article.add_item(Product("frozen chicken", 30000, 6, "frozen"))
list_article.add_item(Product("ice cream", 30001, 8.99, "frozen"))
list_article.add_item(Product("frozen vegetables", 30002, 4.99, "frozen"))
list_article.add_item(Product("whole chicken", 20000, 6, "chilled"))
list_article.add_item(Product("beefsteak", 20001, 12, "chilled"))
list_article.add_item(Product("milk", 20002, 2, "chilled"))
list_article.add_item(Product("cheese", 20003, 7.99, "chilled"))
list_article.add_item(Product("bread", 10000, 1.5, "ambient"))
list_article.add_item(Product("pasta", 10001, 3.5, "ambient"))
list_article.add_item(Product("pasta sauce", 10002, 4, "ambient"))
list_article.add_item(Product("rice", 10003, 12.99, "ambient"))