import pandas as pd

produkty = ["Mysz", "Klawiatura", "Monitor", "Podkladka"]
ceny = [50, 120, 650, 30]
ilosci = [10, 5, 3, 20]

df = pd.DataFrame({
    "Produkt": produkty,
    "Cena": ceny,
    "Ilosc": ilosci
})

df["Wartosc"] = df["Cena"] * df["Ilosc"]

print(df)

print("Produkty drozsze niz 100 zl:")
drogie_produkty = df[df["Cena"] > 100]["Produkt"]
for produkt in drogie_produkty:
    print(produkt)

wartosc_magazynu = df["Wartosc"].sum()
srednia_cena = df["Cena"].mean()

print(f"Wartosc magazynu: {wartosc_magazynu} zl")
print(f"Srednia cena: {srednia_cena:.2f} zl")