horasTrabajadas = float(input("Ingrese la cantidad de horas que trabajo: "))
jornal = float(input("Ingrese el salario por hora: "))
if horasTrabajadas > 48:
    horasExtras = horasTrabajadas - 48
    sueldoTotal = (horasTrabajadas*jornal) + (horasExtras*(jornal*0.50))
    print("Su salario total asciende a ", sueldoTotal, " y tuviste ", horasExtras, " horas extras")
else:
    sueldoTotal = horasTrabajadas * jornal
    print("Su sueldo es ",sueldoTotal)