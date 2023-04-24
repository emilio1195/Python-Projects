cadena = 'hola mundo, este programa integra el conteo de vocales en una ' \
         'cadena de texto y almacenar en Un diccionario'
cadena = 'hello world, this programm integrates the vowels counting in a ' \
         'string and stores it in a dictionary'

cadena = cadena.lower()
contador = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

contador['a'] = cadena.count('a')
contador['e'] = cadena.count('e')
contador['i'] = cadena.count('i')
contador['o'] = cadena.count('o')
contador['u'] = cadena.count('u')

print(contador)