class Contact:
    def __init__(self, first_name, last_name, phone_number,email, workplace): 
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.workplace = workplace
    def print_contact (self):
        print (self.first_name, self.last_name, self.phone_number,self.email, self.workplace)
    def get_name (self):
        return self.first_name
    def get_surname (self):
        return self.last_name
    def get_number (self):
        return self.phone_number
        
class AddressBook:
    list_contacts = []
    def __init__(self, first_name, last_name, phone_number,email, workplace):
        self.contact = Contact(first_name, last_name, phone_number,email, workplace)
        self.list_contacts.append(self.contact)
    
    def print_list (self):
        numb=0
        for i in self.list_contacts:
            self.list_contacts[numb].print_contact()
            numb+=1
    def edit_contact(self, first_name, last_name, phone_number,email, workplace):
        numb=0
        for i in self.list_contacts:
            if first_name == self.list_contacts[numb].get_name():
                self.contact = Contact(first_name, last_name, phone_number,email, workplace)
                self.list_contacts[numb]=self.contact
            numb+=1
    def remove(self,first_name):
        numb=0
        for i in self.list_contacts:
            if first_name == self.list_contacts[numb].get_name():
                self.list_contacts.pop(numb)
            numb+=1
    def numb_of_contacts (self):
        return len(self.list_contacts)
    
    def find_by_name(self, first_name):
        numb=0
        for i in self.list_contacts:
            if first_name == self.list_contacts[numb].get_name():
                self.list_contacts[numb].print_contact()
            numb+=1
            
    def find_by_surname(self, surname):
        numb=0
        for i in self.list_contacts:
            if surname == self.list_contacts[numb].get_surname():
                self.list_contacts[numb].print_contact()
            numb+=1
    def find_by_number(self, number):
        numb=0
        for i in self.list_contacts:
            if number == self.list_contacts[numb].get_number():
                self.list_contacts[numb].print_contact()
            numb+=1
            
    def sort_by_name(self):
        numb1=0
        for i in self.list_contacts:
            numb2=0
            for j in self.list_contacts:
                if self.list_contacts[numb1].get_name() < self.list_contacts[numb2].get_name():
                    copy = self.list_contacts[numb1]
                    self.list_contacts[numb1] = self.list_contacts[numb2]
                    self.list_contacts[numb2] = copy
                numb2+=1
            numb1+=1
    def sort_by_surname(self):
        numb1=0
        for i in self.list_contacts:
            numb2=0
            for j in self.list_contacts:
                if self.list_contacts[numb1].get_surname() < self.list_contacts[numb2].get_surname():
                    copy = self.list_contacts[numb1]
                    self.list_contacts[numb1] = self.list_contacts[numb2]
                    self.list_contacts[numb2] = copy
                numb2+=1
            numb1+=1
                                  

menu = {}
menu['1']="Create contact" 
menu['2']="Edit a contact"
menu['3']="Remove a contact"
menu['4']="Number of contacts in AddressBook"
menu['5']="Search contact by"
menu['6']="Sort AddressBook"
menu['7']="Exit"
while True: 
    options=menu.keys()
    sorted(options)
    for entry in options: 
      print (entry, menu[entry])
    selection=input("Please Select: ") 
    if selection =='1': 
      name = input("Input name: ") 
      surname = input("Input surname: ") 
      number = input ("Input number: ")
      email = input ("Input email: ")
      workplace = input ("Input workplace: ")
      s1 = AddressBook (name, surname, number, email, workplace)
    elif selection == '2': 
        name = input("Input name: ") 
        surname = input("Input surname: ") 
        number = input ("Input number: ")
        email = input ("Input email: ")
        workplace = input ("Input workplace: ")
        s1.edit_contact(name, surname, number, email, workplace)
        print ("Edit")
    elif selection == '3':
        print ("Remove" )
        name = input("Input name: ") 
        s1.remove(name)
    elif selection == '4':
        print ("Number of contacts:", s1.numb_of_contacts())  
    elif selection == '5':
        while True:
            print ("Search contact by:" )  
            print ("1 Name" )  
            print ("2 Surname" )  
            print ("3 Phone number" )  
            userinput=int(input("Please Select:") )
            if userinput == 1:
                name = input("Input name: ") 
                s1.find_by_name(name)
                break
            elif userinput == 2:
                surname = input("Input surname: ") 
                s1.find_by_surname(surname)
                break
            elif userinput == 3:
                numb = input ("Input number: ")
                s1.find_by_number(numb)
                break
            else:
                print ("Unknown Option Selected!" )
    elif selection == '6':
        while True:
            print ("Sort adressbook by:" )  
            print ("1. Name" )  
            print ("2. Surname" )     
            userinput=int(input("Please Select:"))
            if userinput == 1:
                s1.sort_by_name()
                print ("Sorted list by name: ")
                s1.print_list()
                break
            elif userinput == 2:
                s1.sort_by_surname()
                print ("Sorted list by surname: ")
                s1.print_list()
                break
            else:
                print ("Unknown Option Selected!" )
    elif selection == '7': 
      break
    else: 
      print ("Unknown Option Selected!" )
