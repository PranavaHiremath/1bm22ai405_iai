from fractions import Fraction


P_DA = Fraction(5, 1000)  # Fraction defective output of Plant A
P_DB = Fraction(8, 1000)  # Fraction defective output of Plant B
P_DC = Fraction(10, 1000)  # Fraction defective output of Plant C

N_A = 500  
N_B = 1000  
N_C = 2000  

P_D = (P_DA * N_A + P_DB * N_B + P_DC * N_C) / (N_A + N_B + N_C)


P_AD = (P_DA * N_A) / (N_A + N_B + N_C)


print(P_AD / P_D)
