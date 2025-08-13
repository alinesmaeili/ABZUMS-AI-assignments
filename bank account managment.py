class BankAccount:
    bank_name = "First National Bank"
    def __init__(self, account_holder : str, initial_balance: float = 0.0) :
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transition = []

        

class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        # 1. Deposit (amount) - Add to balance if amount is valid
        if amount > 0:
            self.balance += amount
            # 3. Record transactions in format "Deposit: +$X"
            transaction_record = f"Deposit: +${amount:.2f}"
            self.transactions.append(transaction_record)
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount: float) -> None:
        # 2. Withdraw (amount) - Subtract from balance if funds are available
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                # 3. Record transactions in format "Withdrawal: -$X"
                transaction_record = f"Withdrawal: -${amount:.2f}"
                self.transactions.append(transaction_record)
                print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value")

class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount): # Use the new static method
            self.balance += amount
            transaction_record = f"Deposit: +${amount:.2f}"
            self.transactions.append(transaction_record)
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount): # Use the new static method
            if self.balance >= amount:
                self.balance -= amount
                transaction_record = f"Withdrawal: -${amount:.2f}"
                self.transactions.append(transaction_record)
                print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    # 1. Implement __str__ to return "Account Holder: X, Balance: $Y"
    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    # 2. Add class method change_bank_name (new_name)
    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    # 3. Add static method validate_amount (amount) returns bool
    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            transaction_record = f"Deposit: +${amount:.2f}"
            self.transactions.append(transaction_record)
            print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                transaction_record = f"Withdrawal: -${amount:.2f}"
                self.transactions.append(transaction_record)
                print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0



print("--- Task 4: Test Your Implementation ---")

account1 = BankAccount("Alice", 1000.0)
account2 = BankAccount("Bob", 500.0)
print("\n--- Accounts Created ---")
print(f"Account 1: {account1}")
print(f"Account 2: {account2}")



print("\n--- Performing Transactions ---")
account1.deposit(200.0)
account1.withdraw(50.0)
account1.withdraw(1500.0) 
account1.deposit(0) 
account2.deposit(100.0)
account2.withdraw(600.0) 
account2.withdraw(50.0)
account2.withdraw(-20) 



print("\n--- Changing Bank Name ---")
print(f"Current Bank Name: {BankAccount.bank_name}")
BankAccount.change_bank_name("Global Financials Inc.")
print(f"New Bank Name (accessed via class): {BankAccount.bank_name}")
print(f"New Bank Name (accessed via account1 instance): {account1.bank_name}")

print("\n--- Final Account States ---")
print(f"Account 1: {account1}")
print(f"Account 2: {account2}")

print("\n--- Validating Amounts ---")
amount_to_validate_1 = 100.0
amount_to_validate_2 = -50.0

print(f"Is {amount_to_validate_1} valid? {BankAccount.validate_amount(amount_to_validate_1)}")
print(f"Is {amount_to_validate_2} valid? {BankAccount.validate_amount(amount_to_validate_2)}")

print("\n--- Transaction History for Account 1 ---")
for transaction in account1.transactions:
    print(transaction)

print("\n--- Transaction History for Account 2 ---")
for transaction in account2.transactions:
    print(transaction)


class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            transaction_record = f"Deposit: +${amount:.2f}"
            self.transactions.append(transaction_record)
            print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                transaction_record = f"Withdrawal: -${amount:.2f}"
                self.transactions.append(transaction_record)
                print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    # Task 5: Implement a show_transactions() method that prints all transactions
    def show_transactions(self) -> None:
        if not self.transactions:
            print(f"No transactions found for {self.account_holder}.")
            return

        print(f"\n--- Transactions for {self.account_holder} ---")
        for transaction in self.transactions:
            print(transaction)
        print("-----------------------------------")


# --- Test the new show_transactions method ---

print("\n--- Testing Task 5: Add Transaction History ---")

my_account = BankAccount("Charlie", 750.0)
my_account.deposit(150.0)
my_account.withdraw(50.0)
my_account.deposit(300.0)
my_account.withdraw(100.50)

# Now, call the new method to show transactions
my_account.show_transactions()

# Test an account with no transactions
empty_account = BankAccount("No History", 0.0)
empty_account.show_transactions()

class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            transaction_record = f"Deposit: +${amount:.2f}"
            self.transactions.append(transaction_record)
            print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                transaction_record = f"Withdrawal: -${amount:.2f}"
                self.transactions.append(transaction_record)
                print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    def show_transactions(self) -> None:
        if not self.transactions:
            print(f"No transactions found for {self.account_holder}.")
            return

        print(f"\n--- Transactions for {self.account_holder} ---")
        for transaction in self.transactions:
            print(transaction)
        print("-----------------------------------")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
        print(f"Savings account created for {self.account_holder} with initial balance ${self.balance:.2f} and interest rate {self.interest_rate:.2%}")

    def add_interest(self) -> None:
        interest_amount = self.balance * self.interest_rate
        if interest_amount > 0:
            self.balance += interest_amount
            transaction_record = f"Interest Earned: +${interest_amount:.2f} ({self.interest_rate:.2%})"
            self.transactions.append(transaction_record)
            print(f"Interest of ${interest_amount:.2f} added. New balance: ${self.balance:.2f}")
        else:
            print("No interest added (balance is zero or interest rate is not positive).")

    def __str__(self) -> str:
        parent_str = super().__str__()
        return f"{parent_str}, Interest Rate: {self.interest_rate:.2%}"


print("\n--- Testing Task 6: Create SavingsAccount Subclass ---")

savings1 = SavingsAccount("David Lee", 2000.0, 0.025)
print(savings1)

savings1.deposit(500.0)
savings1.withdraw(100.0)

savings1.add_interest()

print(savings1)

savings1.show_transactions()

savings2 = SavingsAccount("Eve", 0)
savings2.add_interest()
print(savings2)

class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            transaction_record = f"Deposit: +${amount:.2f}"
            self.transactions.append(transaction_record)
            print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                transaction_record = f"Withdrawal: -${amount:.2f}"
                self.transactions.append(transaction_record)
                print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    def show_transactions(self) -> None:
        if not self.transactions:
            print(f"No transactions found for {self.account_holder}.")
            return

        print(f"\n--- Transactions for {self.account_holder} ---")
        for transaction in self.transactions:
            print(transaction)
        print("-----------------------------------")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
        print(f"Savings account created for {self.account_holder} with initial balance ${self.balance:.2f} and interest rate {self.interest_rate:.2%}")

    def add_interest(self) -> None:
        interest_amount = self.balance * self.interest_rate
        if interest_amount > 0:
            self.balance += interest_amount
            transaction_record = f"Interest Earned: +${interest_amount:.2f} ({self.interest_rate:.2%})"
            self.transactions.append(transaction_record)
            print(f"Interest of ${interest_amount:.2f} added. New balance: ${self.balance:.2f}")
        else:
            print("No interest added (balance is zero or interest rate is not positive).")

    def __str__(self) -> str:
        parent_str = super().__str__()
        return f"{parent_str}, Interest Rate: {self.interest_rate:.2%}"


print("\n--- Task 7: Test SavingsAccount ---")

savings_account_test = SavingsAccount("Charlie", 1000.0, 0.05)

savings_account_test.deposit(50.0)

savings_account_test.add_interest()

print(f"Savings Account - {savings_account_test}")






