#BUSCA Y ELIMINA LA KEY, QUE SE PASA COMO PARAMETRO DE UN DICCIONARIO Y DEVUELVE EL VALOR, SI NO EXISTE
#DA ERROR. PARA QUE ESO SUCEDA, SE PUEDE UTILIZAR EL SEGUNDO PARAMETRO DE POP() QUE ES EL VALOR
#SI LA KEY NO EXISTE

#POP APARTE DE ELMINAR ME DEVUELVE EL ELEMENTO ELIMINADO O LA KEY ELIMINADA COMO EN ESTE CASO QUE USAMOS UN DICT

lista =[ {"edad":"25","nota":9},
        {"nombre":"Jose","edad":34,"nota":8},
        {"nombre":"Sol","edad":46,"nota":7},
        {"nombre":"Beto","edad":28,"nota":6},   
        ]

for e_nombre in lista:
    print(e_nombre.get("nombre","SIN NOMBRE"))

dic_cero=dict(lista[0])
valor_eliminado=dic_cero.pop("nombre","NO EXISTE") #POP ME DEVUELVE None O CUALQUIER VALOR QUE LE DE COMO ACA "NO EXISTE"
                                                #ACA LE PEDIMOS A POP QUE ME ELIMINE LA KEY "nombre" DE LA POSICION 0 DE LA LISTA PERO COMO NO EXISTE
print("valor eliminado",valor_eliminado)        #USO EL OTRO VALOR QUE LE DI A POP "NO EXISTE" Y ESO SE ASIGNA A valor_eliminado PARA LUEGO PRINTEAR

