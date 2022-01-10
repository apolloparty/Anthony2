import Class.Client as Client
import Class.Encheres as Encheres

numero_client, adresse_client = Client.Client().info_client()
cash_client = Client.Client().montant_portefeuille()

print(f"Le numero_client est: {numero_client}")
print(f"L'adresse du client': {adresse_client}")
print(f"Le montant du portefeuille du client est {cash_client}")