import cenas
ilgums=int(input("Līguma termiņš: "))
pirms=float(input("Iepriekšējais skaitītāja rādītājs: "))
pec=float(input("Esošais skaitītāja rādītājs: "))
print("Patērētās kWh: ",cenas.paterets(pirms,pec),"kWh")
print("Rēķina summa: ",cenas.total(ilgums),"€")
