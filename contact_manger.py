contact_dict={}

def add_contact(name,cno):
    global contact_dict
    contact_dict.update({name:contact})
    print()
    print("="*20)
    print("Contact added!")
    print()
    

def find_contact(name):
    global contact_dict
    if contact_dict[name]:
        print()
        print("="*20)
        print(f"{name}   {contact_dict[name]}")
        
    else:
        print()
        print("="*20)
        print("Person not found!")
        print("="*20)

def modify_contact(name):
    global contact_dict
    if contact_dict[name]:
        print()
        print("="*20)
        print("Contact found!")
        print()
        old_contact=contact_dict[name]
        new_cno=int(input("Enter contact no..."))
        if old_contact==new_cno:
            print("Please enter a new contact no...")
        else:
            contact_dict.update({name:new_cno})
            print()
            print("="*20)
            print("Contact modified!")
            print()

def delete_contact(name):
    global contact_dict
    if contact_dict[name]:
        del_con=contact_dict[name]
        contact_dict.pop(name)
        print()
        print("="*20)
        print("Contact deleted!!")
        print()
    else:
        print()
        print("="*20)
        print("Contact not found...")
        print("="*20)
        

def show_contacts():
    global contact_dict
    print()
    print("="*20)
    print("Name           Contact No")
    for key,item in contact_dict.items():
        print(key," "*10,item)
    print("="*20)
        

while True:
    print("="*20)
    
    print("Welcome to Contact manager")
    print("1.add contact")
    print("2.see all contact")
    print("3.find contact from name..")
    print("4.modify contact")
    print("5.delte contact")
    print("6.exit")
    print("="*20)
    print()
    
    try:
        ch=int(input('Enter your choice...'))
    except ValueError:
        print("Invalid Choice, please choose option from given above!!")
    
    match ch:
        case 1:
            try:
                name=input("Enter contact name...")
                contact=int(input("Enter contact no..."))
                if len(str(contact))<10-1:
                    print("Contact number must be 10 digits!!")
                else:
                    add_contact(name,contact)
            except:
                print("Invalid Name or Contact No")
            
        case 2:
            show_contacts()
        case 3:
            try:
                c_name_find=input("Enter contact name...")
            except ValueError:
                print("Invalid value for name to find, try again...")
            find_contact(c_name_find)
        
        case 4:
            try:
                c_name_mod=input("Enter contact name to modify ...")
            except:
                print("Invalid Name to modify contact, please try again! ")
            modify_contact(c_name_mod)
        
        case 5:
            try:
                c_name_del=input("Enter value for  name to delete ...")
            except:
                print("Invalid value for a name to delete, try again")
            delete_contact(c_name_del)
        case 6:
            print("THANK YOU FOR VISITING!!")
            break
            
    
    
