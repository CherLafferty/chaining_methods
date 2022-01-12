class User:
    #constructor
    #instance method
    def __init__(self, name):
        self.name = name
        self.amount = 0
    #method
    def make_deposit(self, amount):
        # your code goes here...
        self.amount += self.make_deposit().make_withdrawal()
        # self.amount += amount
        return self

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


cher = User("Cher")
nibbles = User("Mr. Nibbles")
benny_bob = User("Benny Bob")

cher.make_deposit(100)
cher.make_deposit(200)
cher.make_deposit(50)
cher.make_withdrawl(45)
cher.display_user_balance()

nibbles.make_deposit(1000)
nibbles.make_deposit(1000)
nibbles.make_withdrawl(500)
nibbles.make_withdrawl(300)
nibbles.display_user_balance()

benny_bob.make_deposit(1500)
benny_bob.make_withdrawl(1000)
benny_bob.make_withdrawl(5000)
benny_bob.make_withdrawl(3000)
benny_bob.display_user_balance()


nibbles.transfer_money(400, cher)