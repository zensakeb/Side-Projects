print("Welcome To Human Data House")
print()

class human:
    def __init__(self):
        self.name = input("enter a name to create a human: ")
        self.height = input("enter a height of your human(in cm): ")
        self.weight = input("enter a weight of your human(in kg): ")
        self.body_type = input("enter a preferable body type: ")
        self.age = input("enter your human's age: ")
        self.sex = input("enter sex of your human: ")
        self.ethnicity = input("enter ethnicity of your human: ")

case_dict = {}

while True:
    print("Choose your activity:")
    print("For creating a new human, type 'create'<-------> For finding human data, type 'find'")
    print("To exit, type 'Exit'")
    activity = input()

    if activity == "Exit":
        print("Thank You For Using Human Data House")
        break 

    if activity == "create": 
        take_num = int(input("How many humans you want to create: "))
        print()
 
        for i in range(take_num):
            i_d = input("Human Test Case ID: ") 
            test_case = i_d
            print()
            i_d = human()
            case_no = i_d
            case_dict[test_case] = case_no
            print()        
            print("Congrats Your Human is created")
            print("\n","A human data has been created on your specs")
            print("Acces your human data with the following: ")
            print()
            print("\n","Human Test Case ID",test_case,"\n",i_d.name,"==>",i_d.height+"cm","==>",i_d.weight+"kg","==>",i_d.body_type,"==>",i_d.age+"years","==>",i_d.sex,"==>",i_d.ethnicity)
            print()

    if activity == "find":
        while True:
            find_id = input("HTCI: ")
            if find_id == "Back":
                print()
                break

            if find_id in case_dict.keys():
                for k,v in case_dict.items():
                    if k == find_id:
                        print()
                        print("Detais of",k,":")
                        print()
                        print("Name: ",v.name)
                        print("Height: ",v.height)
                        print("Weight: ",v.weight)
                        print("Body Type: ",v.body_type)
                        print("Age: ",v.age)
                        print("Sex: ",v.sex)
                        print("Ethnicity: ",v.ethnicity)
                        break

            else:
                print("There is no Human according to this HTCI. Enter a valid HTCI Or To create a human type, 'Back' in HTCI: ")
                print()
    if activity != "create" or activity != "find": 
        print()
        print("Wrong input. Choose between the the given activities")
        print()