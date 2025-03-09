import json
import os
import unidecode

FILENAME = "C:\\Python\\Learning\\miniPrograms\\contactManager\\contacts.json"

def verifyIfFileExists(file):
    return os.path.exists(file) and os.path.isfile(file)

def escolher_indicativo():
    indicativos = {
        "1": ("🇺🇸 Estados Unidos", "+1"),
        "2": ("🇨🇦 Canadá", "+1"),
        "3": ("🇧🇷 Brasil", "+55"),
        "4": ("🇵🇹 Portugal", "+351"),
        "5": ("🇪🇸 Espanha", "+34"),
        "6": ("🇫🇷 França", "+33"),
        "7": ("🇩🇪 Alemanha", "+49"),
        "8": ("🇮🇹 Itália", "+39"),
        "9": ("🇬🇧 Reino Unido", "+44"),
        "10": ("🇦🇺 Austrália", "+61"),
        "11": ("🇯🇵 Japão", "+81"),
        "12": ("🇨🇳 China", "+86"),
        "13": ("🇮🇳 Índia", "+91"),
        "14": ("🇲🇽 México", "+52"),
        "15": ("🇷🇺 Rússia", "+7"),
        "16": ("🇦🇷 Argentina", "+54"),
        "17": ("🇨🇱 Chile", "+56"),
        "18": ("🇨🇴 Colômbia", "+57"),
        "19": ("🇿🇦 África do Sul", "+27")
    }
    
    while True:
        print("\n🌍 Escolha o indicativo do país: ")
        for key, (pais, indicativo) in indicativos.items():
            print(f"{key}. {pais} ({indicativo})")
            
        escolha = input("\nDigite o número correspondente ao país: ").strip()
        if escolha in indicativos:
            pais, indicativo = indicativos[escolha]
            return indicativo
        else:
            print("\n❌ Escolha inválida, tente novamente.")

def numeroTelemovel():
    while True:
        numero = input("Digite o número de telemóvel (9 dígitos): ").strip()
        if len(numero) == 9 and numero.isdigit():
            contacts = load_contacts()
            if any(contact['phone'] == numero for contact in contacts):
                print("❌ Esse número já existe na sua lista de contactos.")
                continue
            return numero
        else:
            print("❌ Número inválido. O número deve ter exatamente 9 dígitos.")


# Carregar os contatos do ficheiro
def load_contacts():
    if verifyIfFileExists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    return []

            
# Guardar os contatos no ficheiro
def save_contacts(contacts):
    if verifyIfFileExists(FILENAME):
        try:
            with open(FILENAME, "w") as file:
                json.dump(contacts, file, indent=4)
        except :
            print()
            
def verifyIfNameExists(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            return True
    return False

# Adicionar um novo contato
def add_contact():
    first_name = input("Primeiro Nome: ")
    last_name = input("Apelido: ")
    name = f"{first_name} {last_name}"
    if(verifyIfNameExists(name)):
        print(f"O nome '{name}' já existe, por favor insira um diferente")
    else:
        indicative = escolher_indicativo()
        phone_number = numeroTelemovel()
        email = input("Email(deve conter '@'): ")
        contacts = load_contacts()
        contacts.append({"name": name, "indicative": indicative, "phone": phone_number, "email": email})
        save_contacts(contacts)
    
# Listar todos os contatos
def list_contacts():
    if verifyIfFileExists(FILENAME):
        contacts = load_contacts()
        if contacts:
            print("\n\nSeus contactos: ")
            for contact in contacts:
                print(f"\n💀 {contact['name']} - {contact['indicative']} {contact['phone']} - {contact['email']}")
        else:
            print("\nNão há contactos cadastrados.")
    else:
        print("O ficheiro não foi encontrado")
        
# Pesquisar contato por nome


def search_contact():
    contacts = load_contacts()
    searchName = input("Digite o nome de quem procura: ").strip().lower()
    searchName = unidecode.unidecode(searchName)  # Remove acentos

    found_contacts = []
    
    for contact in contacts:
        normalized_name = unidecode.unidecode(contact["name"].lower())  # Remove acentos do nome do contato
        if searchName in normalized_name:
            found_contacts.append(contact)

    if found_contacts:
        print("\n🔍 Resultados da pesquisa 🔎:")
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['indicative']} {contact['phone']} - {contact['email']}")
    else:
        print("❌ Contato não encontrado.")

 
            
# Apagar um contato
def delete_contact():
    contacts = load_contacts()
    nameToDelete = input("Digite o nome do contacto que pretende remover: ").strip()
    
    if verifyIfNameExists(nameToDelete):
        updated_contacts = []
        
        for contact in contacts:
            if contact["name"].lower() != nameToDelete.lower():
                updated_contacts.append(contact)
        
        save_contacts(updated_contacts)
        print(f"✅ Contato '{nameToDelete}' apagado com sucesso.")
    else:
        print("❌ Contato não encontrado.")


# Menu principal
def menu():
    while True:
        print("\n-------------------------------------")
        print("     🧾  CONTACT MANAGER  📱")
        print("-------------------------------------")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Pesquisar Contato")
        print("4. Apagar Contato")
        print("5. Sair")

        option = input("\nEscolha uma opção: ")
        
        if option == "1":
            add_contact()
        elif option == "2":
            list_contacts()
        elif option == "3":
            search_contact()
        elif option == "4":
            delete_contact()
        elif option == "5":
            print("\nExiting....")
            break
        else:
            print("\nOpção inválida, tente novamente...")

if __name__ == "__main__":
    menu()
