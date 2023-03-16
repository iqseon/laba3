class BankAccount:
    balance: int
    accountNumber: int
    name: str
    def __init__(self):
            self.accountNumber = int
            amount = int(input("Введите номер карты:"))
            print("Номер карты:", amount)

            self.name = str(input("Имя:"))
            print("Имя:", self.name)

            self.balance = 0
            print("Ваш баланс:", self.balance)

    def deposit(self):
        amount = float(input("Введите сумму для депозита: "))
        self.balance += amount
        print("\n Сумма депозита:", amount)

    def withdraw(self):
        amount = float(input("Введите сумму для вывода: "))
        if amount <= self.balance:
            self.balance -= amount
            print("\n Ваша выведенная сумма:", amount)
            percent = amount * 0.05
            print("\n Комиссия =", percent)

    def bankFes(self):
            self.balance *= 0.95



    def display(self):
        print("\n Доступный баланс =", self.balance)





BankAccount = BankAccount()


BankAccount.deposit()
BankAccount.withdraw()
BankAccount.bankFes()
BankAccount.display()

