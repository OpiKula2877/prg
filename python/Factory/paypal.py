class PayPal:
    def zaplatit(self, castka):
        return f"Platím {castka} přes PayPal."

class Kreditka:
    def zaplatit(self, castka):
        return f"Platím {castka} kartou."

# To je naše Factory
class PaymentFactory:
    @staticmethod
    def vytvor_platbu(metoda):
        tovarna = {
            "paypal": PayPal(),
            "karta": Kreditka()
        }
        return tovarna.get(metoda, ValueError("Neznámá metoda"))

# Použití
platba = PaymentFactory.vytvor_platbu("paypal")
print(platba.zaplatit(100))