from datetime import datetime

# class ArticleList():

# class CustomerFormValidation():
#       """Validate input of CustomerForm based on input quality"""

# class CustomerForm(ArticleList, CustomerFormValidation):


class CustomerFormValidation():
    """Possesses all the validation methods needed for the customer's input"""

    def customer_id_validation(self):
        """Validate attribute: customer_id as a correct integer
        returns attribute: error_status as True if the customer_id attribute is in the wrong format"""

        if hasattr(self, "customer_id"):  
            customer_id_upper_limit = 100000
            error_message = f"Please enter a positive integer between 0 and {customer_id_upper_limit}"
            try:
                int_test = int(self.customer_id)
                if int_test < 0 or int_test > customer_id_upper_limit:
                    raise ValueError(error_message)
                self.error_status = False
            except ValueError:
                print(error_message)
                self.error_status = True

    
    def delivery_date_validation(self):
        """Validate the delivery_date attribute is in a correct date format
        returns error_status attribute as True if the delivery_date attribute is in the wrong format"""

        if hasattr(self, "delivery_date"):
            error_message = "Enter the date using the dd/mm/yyyy format"
            try:
                date_test = datetime.strptime(self.delivery_date, '%d/%m/%Y')
                self.error_status = False
            except ValueError:
                print(error_message)
                self.error_status = True

    def article_name_validation(self):
        """Validate the temp_article_name attribute against the name_list attribute"""
        error_message = "ERROR: PLEASE TYPE A VALID ARTICLE FROM THE LIST BELOW."

        if self.temp_article_name not in self.name_list:
            print(error_message)
            self.error_status = True
        else:
            self.error_status = False    

    def article_quantity_validation(self):
        """Validate the temp_article_quantity attribute"""
        integer_error_message = "Please enter an integer between 1 and 10"         ## Name of variable can be improved
        bulk_order_error_message = "For bulk orders with more than 10 items, please call our office at +614-0000-0000"        ## Name of variable can be improved

        try:
            self.temp_article_quantity = int(self.temp_article_quantity)
            if self.temp_article_quantity > 10:
                print(bulk_order_error_message)
                self.error_status = True
            else:
                self.error_status = False
            
        except ValueError:
            print(integer_error_message)
            self.error_status = True

    def finished_order_validation(self):
        """Validate the temp_finished_order_status"""
        # Using a list as different type of accepted yes and no maybe accepted later on
        valid_yes = ["yes"]
        valid_no = ["no"]
        error_message = "ERROR: Please type only 'yes' or 'no'."
        
        try:
            # Test if if it a valid yes
            if self.temp_finished_order_status in valid_yes:
                self.finished_order_status = True
                delattr(self, "temp_finished_order_status")
                self.error_status = False
            
            # Test if it's a valid no
            elif self.temp_finished_order_status in valid_no:
                self.finished_order_status = False
                delattr(self, "temp_finished_order_status")
                self.error_status = False

            # Else, temp_finished_order_status is invald
            else:
                delattr(self, "temp_finished_order_status")
                self.error_status = True
                print(error_message)            

        except Exception:
            print(error_message)
            self.error_status = True
