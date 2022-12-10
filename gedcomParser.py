path = "duportal.ged"

class Individual:
    def __init__(self, id, name, firstname, nickname, birthdate, sex, birthplace, job, note):
        self.id= id
        self.name = name
        self.firstname=firstname
        self.nickname=nickname
        self.birthdate=birthdate
        self.sex=sex
        self.birthplace=birthplace
        self.job=job
        self.note=note
        self.father =""
        self.mother=""
        self.siblings = []
        self.godFather=""
        self.godMother=""
        self.stepparents = []
        self.stepsiblings = []
        self.edittime=""

def skipHeader():
    for i in range(28):
        f.readline()

def detectNewIndi(line):
    newIndi = False
    if line[0] == "0":
        newIndi = True
    return newIndi


def birthInfo(individu):
    birthdate = ""
    birthplace = ""
    for i in range(len(individu)):
        if individu[i][0] == "1" and individu[i][1] == "BIRT":
            if individu[i+1][1] == "DATE":
                birthdate = " ".join(individu[i+1][2:])
            if individu[i+2][1]:
                birthplace = " ".join(individu[i+2][2:])
            break
    return birthdate, birthplace


def interpretIndividu(individu):
    individuId = ""
    name = ""
    firstname = ""
    birthdate, birthplace = birthInfo(individu)
    sex = ""
    job = ""
    note = ""
    

    for critere in individu:
        if critere[0]=="1":
            if critere[1]=="_UID":
                individuId = critere[2]
            if critere[1]=="SEX":
                sex=critere[2]
            if critere[1]=="OCCU":
                job=critere[2]
        elif critere[0]=="2":
            if critere[1]=="SURN":
                name = critere[2]
            if critere[1] == "GIVN":
                firstname=critere[2]
    return Individual(individuId, name, firstname, "",birthdate,sex,birthplace,job,"")

    

f = open(path, "r")
#skipHeader()
#while not detectNewIndi(f.readline()):
    #print(f.readline())
gedFile = f.readlines()
gedFile = gedFile[28:len(gedFile)-1]
famille = []
individu = [[]]
for line in gedFile:
    if line[0]!="0":
        individu.append(line.replace("\n","").split(" "))
    else:
        individu = individu[1:]
        famille.append(interpretIndividu(individu))
        individu=[]
    
f.close()
print(len(famille))


