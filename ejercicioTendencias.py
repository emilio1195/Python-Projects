def cuentaEtiquetas(dicTendencias, RangoFechas):
    list_Etiquetas = []
    for fecha in RangoFechas:
        list_Etiquetas.extend(list(dicTendencias[fecha]))
    dict_etiquetas = {}
    set_etiquetas = list(set(list_Etiquetas))
    for etiqueta in set_etiquetas:
        dict_etiquetas[etiqueta] = list_Etiquetas.count(etiqueta)
    return dict_etiquetas

def reportaTendencias(dicTendencias, RangoFechas):
    dic_Etiquetas = cuentaEtiquetas(dicTendencias, RangoFechas)
    totalFechas = len(RangoFechas)
    list_todoTendencia = []
    list_unaTendencia = []

    for k in dic_Etiquetas:
        v = dic_Etiquetas[k]
        if v == totalFechas:
            #si el valor de la etiqueta el igual al tamano de la lista de fechas, fue tendencia en todas las fechas
            list_todoTendencia.append(k)
        if v == 1:
            list_unaTendencia.append(k)
    print('\nLas etiquetas que fueron tendencia en todas las fechas estabelcidas:\n', list_todoTendencia)
    print('Las etiquetas que fueron tendencia una vez en las fechas estabelcidas:\n', list_unaTendencia)

def tendenciasExcluyentes(dicTendencias, fecha1, fecha2):
    dic_Etiquetas = cuentaEtiquetas(dicTendencias, [fecha1, fecha2])
    totalFechas = 2
    list_unaTendencia = []

    for k in dic_Etiquetas:
        v = dic_Etiquetas[k]
        if v == 1:
            list_unaTendencia.append(k)
    print('\nLas Etiquetas que fueron tendencia solo en una fecha son:\n',list_unaTendencia)



tendencias = {'05-16-2020':{'#ECU', '#CUPAMERICA', '#QUEDATECASA', 'DISTANCIAMIENTOSOCIAL', '#CHINA'},
              '08-23-2020':{'#CHINA', '#COVID', '#QUEDATECASA', 'DISTANCIAMIENTOSOCIAL'},
              '11-29-2020': {'#NOSCUIDAMOS', '#COVID', '#QUEDATECASA', "#USOMASCARILLA", 'DISTANCIAMIENTOSOCIAL'},
              '02-12-2021': {'#NORMALIDAD', 'DISTANCIAMIENTOSOCIAL', '#USOMASCARILLA', '#VACUNACOVID'}
              }

dict_etiquetas = cuentaEtiquetas(tendencias, ['08-23-2020', '02-12-2021'])
print(dict_etiquetas,'\n')

reportaTendencias(tendencias, ['08-23-2020', '02-12-2021', '05-16-2020'])

tendenciasExcluyentes(tendencias, '11-29-2020', '02-12-2021')