from store_database import Store
from customer import CustomerForm

store1 = Store("store database")
store2 = Store("store database 2")


a = CustomerForm(store1)
a.get_whole_customer_order()
