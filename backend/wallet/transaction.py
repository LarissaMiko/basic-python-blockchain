import uuid

class Transaction:
    """
    Document of an exchange in currency from a sender
    to one ore more recipients
    """
    def __init__(self, sender_wallet, recipient, amount):
        self.id = str(uuid.uuid4())[0:8]
        self.output = {
            
        }
