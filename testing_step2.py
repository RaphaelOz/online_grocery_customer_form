from input_validation import *

def final_validation():
    while True:
        print("final_val pre_step1") ## For testing purpose
        order_item_list = article_validation_step1()          ## Why is step1 going twice?
        print("final_val after step1") ## For testing purpose
        order_item_list = article_validation_step2()
        print("final_val after step2")
        break
    # order_item_list = article_validation_step2() ## Loss of the return value of step2
    # return order_item_list
    return order_item_list
# print(order_item_list)
test = final_validation()
print(test)