C1 = 3
C2 = 7
C3 = 11
C4 = 16
formulaS = f"1/(1/{C1}+1/{C2})" #add C in Series
CS = eval(formulaS)
formulaS2 = f"1/(1/{C3}+1/{C4})" #add C in Series
CS2 = eval(formulaS2)
formulaP = f"{CS}+{CS2}" #add C in parallel
CP = eval(formulaP)
print("CS:",formulaS,"{:.2f} μF".format(CS))
print("CS2:",formulaS2,"{:.2f} μF".format(CS2))
print("CP:",formulaP,"= {:.2f} μF".format(CP))
