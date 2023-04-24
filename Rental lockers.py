import json
import os

def generateLockers(numCasilleros):
    dictCasilleros = {}
    for num in range(1, numCasilleros+1):
        dictCasilleros[str(num)]= '0' #0 significa casillero disponible
    return dictCasilleros

def write_txt(dic_data, name):
    with open(name, 'w') as file:
        json.dump(dic_data, file, indent=4, ensure_ascii=False)

def read_txt(name):

    with open(name) as file:
        data_json = json.load(file)
    return data_json

def getLockers_Clients():
    JsonRental = read_txt(name_file)
    return JsonRental['Lockers'], JsonRental['Customers'], JsonRental


def getData(dictAlquiler):
    codigo = input('Input a new customer\'s code: ')
    nomApe = input('Enter the customer\'s name and last name: ')
    mesVenc = input('Input the month of expiration for the locker rental (1-12): ')
    while True:
        numCasillero = input('Enter the number of locker to rent: ')
        if queryLocker(numCasillero):
            dictAlquiler['Lockers'][numCasillero] = codigo
            dictAlquiler['Customers'].append({'Code': codigo, 'Data': nomApe, 'Expire': mesVenc})
            return dictAlquiler

def assingLocker():
    dictAlquiler = read_txt(name_file)
    write_txt(getData(dictAlquiler), name_file)
    print('Assigned locker')

def queryLocker(numLocker):
    lockers, customers = getLockers_Clients()
    while True:
        #verifica si el numero de casillero existe
        if numLocker in lockers.keys():
            #verifica si el casillero esta disponible
            if lockers[numLocker] == '0':
                # casillero disponible
                print('Available locker')
                return True
            else:
                codeClient = lockers[numLocker]
                for client in customers:
                    if client['Code'] == codeClient:
                        print('Rented locker, Client code: {}, Expiration month: {}'
                                    .format(codeClient, client['Expire']))
                        return False
        else:
            print('No exist the assigned locker')
            return False

def queryUser():
    lockers, customers = getLockers_Clients()

    while True:

        codeClient = input('Enter the customer\'s code to be queried: ')
        if codeClient in lockers.values():
                # casillero alquilado
                for client in customers:
                    if client['Code'] == codeClient:
                        for locker, value in zip(lockers, lockers.values()):
                            if value == codeClient:
                                print('Client: {}, has the rented locker number: {}'
                                      .format(client['Data'], locker))
                                break
                break
        else:
            print('No exist a client with this code')
            return False

def expiredLocker():
    lockers, customers = getLockers_Clients()

    mes = int(input('Enter a month to check the rental lockers that have expirated (1-12): '))
    for client in customers:
        monthClient = int(client['Expire'])
        if monthClient <= mes:
            for locker, value in zip(lockers, lockers.values()):
                if value == client['Code']:
                    print("Expired rental lockers: \n")
                    print(' - Customer {}, Locker: {}'.format(client['Data'], locker))

def enableLocker():
    lockers, customers, JsonRental = getLockers_Clients()

    numLocker = input('Please specify the locker number to enable access: ')

    # verifica si el numero de casillero existe
    if numLocker in lockers.keys():
        codeClient = lockers[numLocker]
        list_customers = []
        for client in customers:
            if client['Code'] != codeClient:
                list_customers.append(client)

        lockers[numLocker] = "0"
        JsonRental['Lockers'].update(lockers)
        JsonRental['Customers'] = list_customers

        write_txt(JsonRental, name_file)
        print('The locker is enable right now')
    else:
        print('No exist the locker')


#******************************* EXECUTION MAIN *****************************************************************8

name_file = 'customers.txt'
#crea el archivo y datos iniciales
numLockers = 10

if not os.path.isfile(name_file):
    lockers = generateLockers(numLockers)
    dictRental = {'Customers':[], 'Lockers':lockers}
    write_txt(dictRental, name_file)

menu = ['Assign a locker', 'Consult a locker', 'Search an user', 'Notify an expired rental lockers',
        'Enable an expired locker', 'Exit']

while True:
    print('\n-------------MENU-------------------')
    print('*There are {} lockers.'.format(numLockers))
    for item, opcion in zip(menu, range(len(menu))):
        print(' - {} ({})'.format(item, opcion+1))

    opcion = int(input('Enter a option: '))

    if opcion == 1:
        assingLocker()
    if opcion == 2:
        numCasillero = input('Enter the locker\'s number to be queried: ')
        queryLocker(numCasillero)
    if opcion == 3:
        queryUser()
    if opcion == 4:
        expiredLocker()
    if opcion == 5:
        enableLocker()
    if opcion == 6:
        break

