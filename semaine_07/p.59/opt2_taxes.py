"""
Elysabeth Dallaire
Optionnel #2 - Taxes
"""


def calculer_montant_total(prix_affiche):
    montant_tps = round(prix_affiche * 0.05, 2)
    montant_tvq = round(prix_affiche * 0.09975, 2)
    prix_total = round(prix_affiche + montant_tps + montant_tvq, 2)
    return montant_tps, montant_tvq, prix_total


montant_tps, montant_tvq, prix_total = calculer_montant_total(152.14)
print("----------------")
print(f"MONTANT TPS : {montant_tps} $")
print(f"MONTANT TVQ : {montant_tvq} $")
print(f"PRIX TOTAL  : {prix_total} $")