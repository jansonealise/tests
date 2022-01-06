import cenas
ilgums=int(input("Kurš līguma gads: "))
pirms=float(input("Iepriekšējais skaitītāja rādītājs: "))
pec=float(input("Esošais skaitītāja rādītājs: "))
print("Patērētās kWh: ",cenas.paterets(pirms,pec),"kWh")
print("Rēķina summa: ",cenas.total(ilgums),"€")
