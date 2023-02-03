import csv
import random
import sys
# (CSV like: Inf P PP Fr)

# welcome bar :
print("###########################################################")
print("# --- Welcome to the MCQ of irregular vers in English --- #")
print("###########################################################")
print("\n")

# Menu bar :
print("###########################################################")
print("# ---        What kind of MCQs do you want ?          --- #")
print("# ---                                                 --- #")
print("# ---        F : Just French Verbs                    --- #")
print("# ---        E : For English and French Verbs         --- #")
print("# ---                                                 --- #")
print("###########################################################")
print("\n")
menu_enter = input(" write F or E, here !    --> ")
print("\n")
how_much = input(" How many verbs do you want to do ?     --> ")
print("\n")


# Verif the Enter of Menu bar :
def Verif_menu_bar(Enter):
    if Enter== "F" or Enter=="E":
        return True
    else :
        sys.exit()

Verif_menu_bar(menu_enter)



# Recup Verbs:
def List_Verbs(): 
    List_total=[]
    L=""
    file = open('Classeur1.csv','r')
    csv_file =csv.reader(file,delimiter=";")
    for row in csv_file:
        for i in range(len(row)):
            List_total.append(row[i])
    file.close()
    return List_total

LT = List_Verbs()
#print(LT)

#Verif the Enter of how_much
def Verif_how_much(how_much,leni):
    if int(how_much)>=5 and int(how_much)<=leni :
        return True
    else :
        sys.exit()
    
Verif_how_much(how_much,len(LT))



# Aleatoire X
def alea_Q():
    NL= [i for i in range(0,int(len(LT)/4),1)]
    RL= random.sample(NL,int(how_much))
    return RL

RL = alea_Q()
#print(RL)

# Print Q and Result

VF=[]
print("###########################################################")
print("# ---                   There we go !                 --- #")
print("###########################################################")
print("\n")

print("###########################################################")

if menu_enter == "E" :
    for i in range(0,len(RL)):
        print("# ---  Question ", i+1 ,") :")
        print("# ---  ", LT[(int(RL[i])*4)+0] ,"=", LT[(int(RL[i])*4)+3], " ")
        P = input("# ---  P :   ---> ")
        PP = input("# ---  PP :  ---> ")
        print("\n")
        if P == LT[(int(RL[i])*4)+1] and PP == LT[(int(RL[i])*4)+2]:
            VF.append(1)
        else:
            VF.append(0)
    note=0
    for i in range(0,len(VF)):
        if VF[i]==0:
            print("You was wrong at Q ", i+1 ," : " , LT[(int(RL[i])*4)+0], " , " , LT[(int(RL[i])*4)+1] ," , ",  LT[(int(RL[i])*4)+2] ," , ",  LT[(int(RL[i])*4)+3], "."  )
        note = note + int(VF[i])
    print("In total you\'ve got an : ", note, " / ", len(VF),".")

else :
    for i in range(0,len(RL)):
        print("# ---  Question ", i+1 ,") :")
        print("# ---  ", LT[(int(RL[i])*4)+3], " ")
        E = input("# ---  Eng : ---> ")
        P = input("# ---  P :   ---> ")
        PP = input("# ---  PP :  ---> ")
        print("\n")
        if E == LT[(int(RL[i])*4)+0] and P == LT[(int(RL[i])*4)+1] and PP == LT[(int(RL[i])*4)+2]:
            VF.append(1)
        else:
            VF.append(0)
    note=0
    for i in range(0,len(VF)):
        if VF[i]==0:
            print("You was wrong at Q ", i+1 ," : " , LT[(int(RL[i])*4)+0], " , " , LT[(int(RL[i])*4)+1] ," , ",  LT[(int(RL[i])*4)+2] ," , ",  LT[(int(RL[i])*4)+3], "."  )
        note = note + int(VF[i])
    print("In total you\'ve got an : ", note, " / ", len(VF),".")

