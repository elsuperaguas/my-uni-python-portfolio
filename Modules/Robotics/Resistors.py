R1 = 2000
R2 = 2000
R3 = 2000
R4 = 2000
formulaP = f"1/(1/{R1}+1/{R2}+1/{R3}+1/{R3})" #add R in parallel
RP = eval(formulaP)
formulaS = f"{R1}+{R2}+{R3}+{R4}" #add R in Series
RS = eval(formulaS)
formulaT = f"{RS}+{RP}" #add it if you need to join them
RT = eval(formulaT)
print("RS:",formulaS,"= {} Ω".format(RS))
print("RP:",formulaP,"= {:.2f} Ω".format(RP))
print("RT: {:.2f} Ω".format(RT))
