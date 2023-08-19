import math
salarioB = float(input("Qual seu Sálario Bruto: "))


if salarioB < 1302.01:
   salarioL = float(salarioB * 0.075)
   print (f"Calculo do INSS:R$ {salarioL}")
   salarioL = salarioB - salarioL
   print (f"Salario Líquido - inss:R$ {salarioL}")
    
elif salarioB < 2571.30:
    salarioL = float(salarioB * 0.09)- 15.80
    print (f"calculo do INSS: R$ {salarioL}")
    salarioL =salarioB - salarioL
    print (f"salario liquido - inss:R$ {salarioL}")
    
elif salarioB < 3856.94:
    salarioL = float(salarioB * 0.12)-96.87
    print (f"Calculo do INSS:R$ {salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salario Liquido - Inss:R$ {salarioL}")
    
elif salarioB < 7507.49:
    salarioL =float(salarioB * 0.14)- 173.81
    print (f"Calculo do INSS:R$ {salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salario Liquido - INSS:R$ {salarioL}")
    
else:
    salarioB > 75067.49
    salarioL = float(salarioB - 876.85)
    print (f"Calculo do INSS: R${salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salario Liquido - INSS: R${salarioL}")