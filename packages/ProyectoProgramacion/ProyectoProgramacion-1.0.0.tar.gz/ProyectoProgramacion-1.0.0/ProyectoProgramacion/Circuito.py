import numpy as np
R1=float(input("valor de la resistecia 1 :"))
R2=float(input("valor de la resistecia 2 :"))
R3=float(input("valor de la resistecia 3 :"))
R4=float(input("valor de la resistecia 4 :"))
R5=float(input("valor de la resistecia 5 :"))
R6=float(input("valor de la resistecia 6 :"))
V1=float(input("valor de la fuente indepediente 1 :"))
V2=float(input("valor de la fuente indepediente 2 :"))
I1=float(input("valor de la fuente de corriente 1 :"))
V3=float(input("valor de la fuente depediente 1 :"))
a1=(I1-(V1/R1))
a2=0
a3=(-I1+(V2/R3))
sol=np.array([a1,a2,a3])
#1
A11=(-(1/R1)-(1/R5)-(1/R4))
A12=(1/R5)
A13=(1/R4)
#2
B21=((1/R5)+(I1/(R4*R2)))
B22=(-(1/R5)-(1/R2)-(1/R6))
B23=(-(I1/(R4*R2))+(1/R6))
#3
C31=(1/R4)
C32=(1/R6)
C33=(-(1/R3)-(1/R6)-(1/R4))
sis=np.array([[A11,A12,A13],[B21,B22,B23],[C31,C32,C33]])
res=np.linalg.solve(sis,sol)
print(res)
#print(B21)
#A=np.array([[-0.35,0.2,0.1],[0.28,-0.6,0.2],[0.1,0.2,-0.37]])
#B=np.array([2.25, 0, -2.33])
#C=np.linalg.solve(A,B)
#print(C)




