from store_database import display_article_list

from input_validation import customer_number_validation
from input_validation import delivery_date_validation


order = {}

input_id = customer_number_validation()
input_date = delivery_date_validation()
# input_id = input("Please enter your membership id:")
# input_date = input("Which day do you want your order to be delivered?")
# input_article = input("Which item do you need?")
# input_number = input("How many items do you need?")

order["customer_id"] = input_id
order["delivery_date"] = input_date
# order["delivery_date"] = input_date

# item_list = []
# item_list.append(input_article)
# order["item_list"] = item_list

# quantity_list = []
# quantity_list.append(input_number)
# order["item_quantity"] = quantity_list

print(order)


