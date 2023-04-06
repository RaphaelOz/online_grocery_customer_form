class GoodCreator:
    """Create a good and it's relevant information for the database"""
    
    def __init__(self, name, id, price, section):
        self.name = name
        self.id = id
        self.price = price
        self.section = section

## Return the list of articles to be displayed of the whole store for the customer
def display_article_list():
    display_available_items = []
    for index in range(0, len(article_list)):
        display_available_items.append(article_list[index].name)
    return display_available_items

## Creating the list of articles available for purchase.
new_good = GoodCreator("frozen fruits", 30000, 6, "frozen")
new_good2 = GoodCreator("ice cream", 30001, 8.99, "frozen")
new_good3 = GoodCreator("frozen vegetables", 30002, 4.99, "frozen")
new_good4 = GoodCreator("whole chicken", 20000, 6, "chilled")
new_good5 = GoodCreator("beefsteak", 20001, 12, "chilled")
new_good6 = GoodCreator("milk", 20002, 2, "chilled")
new_good7 = GoodCreator("cheese", 20003, 7.99, "chilled")
new_good8 = GoodCreator("bread", 10000, 1.5, "ambient")
new_good9 = GoodCreator("pasta", 10001, 3.5, "ambient")
new_good10 = GoodCreator("pasta sauce", 10002, 4, "ambient")
new_good11 = GoodCreator("rice", 10003, 12.99, "ambient")

article_list = [new_good, new_good2, new_good3, new_good4, new_good5, new_good6, 
                 new_good7, new_good8, new_good9, new_good10, new_good11]


## Create a list of name of all the articles in the store.
article_name_list = []
for index in range(0, len(article_list)):
    article_name_list.append(article_list[index].name)

