

estr1 = 0
estr2 = 0
cont_hijos0 = 0 
cont_hijos1_2 = 0 
cont_hijos3 = 0
case1 = 0
case2 = 0
case3 = 0
case4 = 0
case5 = 0
case6 = 0
bonificacion1 = int()
bonificacion2 = int()
bonificacion3 = int()
bonificacion4 = int()
bonificacion5 = int()
bonificacion6 = int()

mensaje = int(input("¿Desea ingresar datos? 1.SI / 2.NO: "))
while(mensaje == 1):
    estrato = int(input("Ingrese a qué estrato socioeconomico pertenece (1 o 2): "))

    canthijos= int(input("Digite la cantidad de hijos que tiene: "))

   
    if(estrato == 1 and canthijos == 0):
        bonificacion1 = 20000
        estr1 = 1 + estr1
        case1 += 1 
        cont_hijos0 +=1
        print(f"su bono por ser de estrato {estrato} y tener {canthijos} hijos es de: ${bonificacion1}")
    elif(estrato == 1 and canthijos >0 and canthijos<=2):
        bonificacion2 = 25000
        estr1 = 1 + estr1
        case2 += 1
        cont_hijos1_2 += 1
        print(f"su bono por ser de estrato {estrato} y tener {canthijos} hijos es de: ${bonificacion2}")
    elif(estrato == 1 and canthijos >= 3):
        bonificacion3 = 30000
        estr1 = 1 + estr1
        case3 += 1
        cont_hijos3 += 1
        print(f"su bono por ser de estrato {estrato} y tener {canthijos} hijos es de: ${bonificacion3}")
    elif(estrato == 2 and canthijos == 0):
        bonificacion4 = 16500
        estr2 = 1 + estr2
        case4 += 1
        cont_hijos0 += 1
        print(f"su bono por ser de estrato {estrato} y tener {canthijos} hijos es de: ${bonificacion4}")
    elif(estrato == 2 and canthijos >0 and canthijos <=2):
        bonificacion5 = 21500
        estr2 = 1 + estr2
        case5 += 1
        cont_hijos1_2 += 1
        print(f"su bono por ser de estrato {estrato} y tener {canthijos} hijos es de: ${bonificacion5}")
    elif(estrato == 2 and canthijos >= 3):
        bonificacion6 = 26500 
        estr2 = 1 + estr2
        case6 += 1
        cont_hijos3 += 1
        print(f"su bono por ser de estrato {estrato} y tener {canthijos} hijos es de: ${bonificacion6}")
    else:
        print("Usted no tiene ninguna bonificación")
    
   
    
    print(f"La cantidad de personas con estrato 1 es de: {estr1}")
    print(f"La cantidad de personas con estrato 2 es de: {estr2}")
    boni_estrato1 = (bonificacion1  + bonificacion2  + bonificacion3)
    print(f"El dinero total entregado a las personas con estrato 1 es de: {boni_estrato1} " )
    boni_estrato2 = (bonificacion4  + bonificacion5  + bonificacion6 )
    print(f"El dinero total entregado a las personas con estrato 2 es de: {boni_estrato2} " )
    
    print(f"La cantidad de perosnas sin hijos que recibieron el beneficio es de: {cont_hijos0}")
    print(f"La cantidad de personas que recibieron el beneficio con uno o dos hijos es de: {cont_hijos1_2}" )
    print(f"La cantidad de personas que recibieron el beneficio y que cuentan con más de 3 hijos: {cont_hijos3}" )

   
    
  
    boni_per0 = (bonificacion1 + bonificacion4)
    print(f"El total de dinero entregado a las personas sin hijos: {boni_per0}")
    boni_per1_2 = (bonificacion2  + bonificacion5)
    print(f"El total de dinero entregado para beneficiarios con un hijo o dos es de: {boni_per1_2}")
    boni_per3 = (bonificacion3 + bonificacion6)
    print(f"El total de dinero entregado a las personas con más de tres hijos es de: {boni_per3}")
    
    print("-------TOTAL PAGADO POR BONOS--------- ")
    boni_total = (bonificacion1 + bonificacion2 + bonificacion3 + bonificacion4 + bonificacion5  + bonificacion6)
    print(boni_total)
    
else:
    print("Vuelvalo a intentar")




