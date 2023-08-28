class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount

    def transfer(self, sender, receiver, amount):
        if self.owner != sender:
            print("No tienes permiso para transferir desde este monedero.")
            return False
        if self.balance < amount:
            print("Saldo insuficiente en el monedero.")
            return False

        self.balance -= amount
        receiver.wallet.deposit(amount)
        print(f"Transferencia exitosa. {receiver.name} recibió {amount}.")

        return True
