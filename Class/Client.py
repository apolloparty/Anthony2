class Client:
    def __init__(self):
        self.numero = 100
        self.adresse = "11 rue des halles"
        self.cash = 100000
    
    def info_client(self):
        return self.numero, self.adresse

    def montant_portefeuille(self):
        return self.cash