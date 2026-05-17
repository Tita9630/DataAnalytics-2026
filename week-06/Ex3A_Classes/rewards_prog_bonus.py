cust_list = []
class RewardsProgram: # initializing rewarsprogram 
  '''This class represents a reward program'''
  def __init__(self, cust_name, phone, email):
    self.cust_name = cust_name
    self.phone = phone
    self.email = email
  def profile(self): # method 1
    print(f"Name: {self.cust_name}")
    print(f"Phone: {self.phone}")
    print(f"Email: {self.email}")
  def thank_you(self): # method 2
    print(f"Thank you, {self.cust_name}, for visiting our restaurant!")
  def add_to_cust_list(self): # method 3
    cust_list.append((self.cust_name, self.phone, self.email)) # adding customer data to cust_list
cust1 = RewardsProgram("Luna", "588-789-0978", "luna@yahoo.com")
cust2 = RewardsProgram("Alex", "789-876-4532", "Alex@gmail.com")
cust3 = RewardsProgram("Bez", "231-765-1245", "bez@gmail.com")

cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()

cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()

cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()

print(cust_list)


