# 1- create class named User
# 2- initiate three attribute : name, email_address and drivers_licence 
# 3- create three objects and assign them to three variable

class User:
    def __init__(self, name, email_address, drivers_license=None):
        self.name = name
        self.email_address = email_address
        self.drivers_license = drivers_license

user1 = User("Alice Smith", "alice@example.com", "B1234567")
user2 = User("Bob Johnson", "bob@example.com", "C2345678")
user3 = User("Carol Williams", "carol@example.com", "D3456789")

