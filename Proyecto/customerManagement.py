from utils import add_class, remove_class
from js import document, console
import json
import os

out = document.getElementById("out")
out.innerHTML += "⏳Loading Python code..."
isLoaded = False
ultimo_div = document.getElementById("basicInfo")

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

def getInputData(id):
    data = document.querySelectorAll('#' + id)
    if data[1].value is not None:
        out.innerHTML += f"\\\nSe obtuvo: {data[1].value}" 
    return data

def getSelCountry(id):
    selectElement = document.getElementById(id)
    selText = selectElement.options[selectElement.selectedIndex].text
    out.innerHTML += 'Pais seleccionado: ' + selText
    return selText

def setData():
    out.innerHTML += "\\\Saving Data...\\\n"
    userData = {}
    userData['client'] = []
    userData['client'].append({
            'Contact_Information': {
                'first_name': getInputData("first_name"),
                'last_name': getInputData("last_name"),
                'birthdDay' : getInputData("birthDay"),
                'phone': getInputData("phone"),
                'email': getInputData("email"),
            },
            'Job_Information': {
                'company': getInputData("company"),
                'title': getInputData("title")
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
    #with open('data.json', 'r+') as file:
    #    #json.dump(userData, file, indent=4)
    #    fileData = json.load(file)
    #    fileData["customer"].append(userData)
    #    file.seek(0)
    #    json.dump(fileData, file, indent=4)        
    out.innerHTML += f"\\\n✔️Client saved successfully: {userData}"

def getDetails(userName, userData):
    out.innerHTML += f"\\\n👉Customer selected: {userName}"

    for category in userData:
        for val in category:
            #document.getElementById(f"{attr}").innerHTML = val
            detInput = document.getElementById(val)
            if val == 'birthDay' or val == 'birthMonth' or val == 'birthYear':
                birthDayInput = document.getElementById("birthDay")
                birtDayDate = category['birthDay'] + "-" + category['birthMonth'] + "-" + category['birthYear']
            if detInput:
                out.innerHTML += f"\nEl input {val} es correcto"
            else:
                out.innerHTML += f"\nError al encontrar el input {val}"

            #detInput.innerText = category[val]

            out.innerHTML += f"\n{val}: {category[val]}"
    document.getElementById("details").click()



def create_contact(*ags, **kws):
    out.innerHTML += "\\\n🛈 Verificando archivo de base de datos...\\\n"
    setData()
    #createNewFile()
    #out.innerHTML += "<p>Obteniendo entrada del usuario...</p>"
    #setData()

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