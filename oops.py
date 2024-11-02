# import csv


# class Item:
#     pay_rate = 0.8 # The pay rate after 20% discount
#     all = []
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self object
#         self.__name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)

#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price = self.price * self.pay_rate

#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)

#         for item in items:
#             Item(
#                 name=item.get('name'),
#                 price=float(item.get('price')),
#                 quantity=int(item.get('quantity')),
#             )

#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are point zero
#         # For i.e: 5.0, 10.0
#         if isinstance(num, float):
#             # Count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False
    
#     @property
#     def name(self):
#         print("your accessing getter method")
#         return self.__name
    
#     @name.setter
#     def name(self,value):
#         print("your accessing setter method")
#         self.__name = value

#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


#     def send_email(self):
#         self.__connect()
#         self.__prepare_body()
#         self.__send()
#         return "Mail Sent Successfully"
    
#     def __connect(self):
#         return "connection config retrive"

#     def __prepare_body(self):
#         return f"""Dear Team
#             You have received email

#             regards,
#             Abhishek
        
#         """

#     def __send(self):
#         pass



# class Phone(Item):
#     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
#         # Call to super function to have access to all attributes / methods
#         super().__init__(
#             name, price, quantity
#         )

#         # Run validations to the received arguments
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

#         # Assign to self object
#         self.broken_phones = broken_phones



# phone1 = Item("jscPhonev10", 500, 5)
# # phone1.name = "abhishek"
# # phone1.read_only = "BBB"


# print(phone1.send_email())
# # print(Item.all)



# Parent classes
class ParentA:
    def show(self):
        print("ParentA's show method")

class ParentB(ParentA):
    def show(self):
        # super().show()  # Calls ParentA's show
        print("ParentB's show method")

class Child(ParentB):
    def show(self):
        # super().show()  # Follows MRO, calls ParentB's show
        print("Child's show method")

# Usage


child = Child()
ParentA.show(child)
ParentB.show(child)
# child.show()
# Output:
# ParentA's show method
# ParentB's show method
# Child's show method
