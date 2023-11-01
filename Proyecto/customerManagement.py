from utils import add_class, remove_class
from js import document, console
import json
import os

out = document.getElementById("out")
out.innerHTML += "⏳Loading Python code..."


#Funcion rear un nuevo json en caso de que no haya ninguno
#Tiene que ejecutarse de manera manual invocando el método
def createNewFile():
    newFile = False
    try:
        file = open("data.json", "a+")
        if os.stat("data.json").st_size == 0:
            file.write('{\n\t"customer": []\n}')
            file.close()
    except:
        newFile = True
        out.innerHTML += "❌Fail to create file"


#Funcion que obtiene el texto que se ingresa en los input de la pestaña management
def getInputData(id):
    #se utiliza querySelectorAll porque hay duplicidad de id en los input en las pestañas
    #data[0] = inputs de pestaña 'Details'. data[1] = inputs de pestaña 'Management'
    data = document.querySelectorAll('#' + id)

    dataUserInput = ""
    if data[1].value is not None:
        dataUserInput = data[1].value
        out.innerHTML += f"\\\n🛈 {id}: {dataUserInput}"
    else:
        dataUserInput = ""
    return str(str(dataUserInput))


#Funcion que obtiene el pais seleccionado
def getSelCountry(id):
    selectElement = document.getElementById(id)

    if selectElement.value == "None":
        selText = "MX"
    else:
        selText = str(selectElement.value)
        
    out.innerHTML += f"\\\nSe obtuvo: {selText}"
    return selText 


#Funcion que guarda los datos
def setData():
    error = False
    errorMessage = ""
    userData = {}
    userData['client'] = []

    out.innerHTML += "\\\n🔄Saving Data...\\\n"

    userData['client'].append({
            'Contact_Information': {
                'first_name': getInputData("first_name"),
                'last_name': getInputData("last_name"),
                'birth': getInputData("birth"),
                'phone': getInputData("phone"),
                'email': getInputData("email")
            },
            'Job_Information': {
                "company": getInputData("company"),
                "title": getInputData("title")
            },
            'Billing_Information': {
                'country': getSelCountry("countrySelect"),
                'state': getInputData("state"),
                'city': getInputData("city"),
                'street': getInputData("street"),
                'houseExt': getInputData("houseExt"),
                'houseInt': getInputData("houseInt"),
                'suburb': getInputData("suburb"),
                'postalCode': getInputData("postalCode")
            }
        })

    out.innerHTML += '\\\nJSON: ' + str(userData)
    
    try:
        with open('data.json', 'r+') as file:
            fileData = json.load(file)
            fileData["customer"].append(userData)
            file.seek(0)
            json.dump(fileData, file, indent=4)
    except Exception as e:
        error = True
        errorMessage = e

    out.innerHTML += '\\\n' + (f'❌Fail to save: {errorMessage}' if error else '✅Client saved successfully')


#Funcion que muestra el cliente seleccionado de 'Contacts' y
#los muestra en 'Details'.
# userName = str de nombre completo
#userData = objeto que contiene toda la info del cliente empaquetada
def getDetails(userName, userData):
    out.innerHTML += f"\\\n👉Customer selected: {userName}"

    for category in userData:
        for id in category:
            toField = document.querySelectorAll('#' + id)[0]
            toField.value = category[id]
            #out.innerHTML += f"\n{val}: {category[val]}"
    document.getElementById("details").click()


#Funcion que obtiene todos los clientes de la BD
def getContactsName():
    ul = document.getElementById('myUL')
    with open('data.json') as file:
        data = json.load(file)
        counter = 0
        for clients in data['customer']:
            for client in clients['client']:
                contact = client['Contact_Information']
                job = client['Job_Information']
                billing = client['Billing_Information'] 

                name = f'{contact["first_name"]} {contact["last_name"]}'
                out.innerHTML += '\\\nContact found: ' + name
                ul = document.getElementById('myUL')
                ul.insertAdjacentHTML("beforeEnd", f"""
                <li id=\"element\">                
                    <py-button id=\"data{counter}\" label=\"{name}\" title=\"{name}\">
                        def on_click(evt):
                            getDetails(\"{name}\", [{contact}, {job}, {billing}])             
                    </py-button>
                </li>""")
                counter += 1


out.innerHTML += "\\\n✔️Python Loaded." 
out.innerHTML += "\\\n📁Getting contacts..." 
getContactsName()