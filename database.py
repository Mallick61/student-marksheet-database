detabase={}
a=1
def generateMarksheet(val):
    file = " markseet.txt"
    with open(file,"w") as file:
        for i in val:
            file.write(f"{i}"+", ")
def insert(name,roll,course,marks):
    res=[]
    res.append("name : "+name)
    res.append("roll : "+roll)
    res.append("course : "+course)
    res.append("marks : "+marks)
    if roll not in detabase:
        detabase[roll]=res
    else:
        print("\n roll already axist \n")
def search(roll):
    if roll in detabase:
        print(detabase[roll])
        return detabase[roll]
    else :
        print("\n roll not in detabase \n")
def update(roll,marks):
    if roll in detabase:
        res=detabase[roll]
        res[3]="marks : "+marks
        detabase[roll]=res
    else :
        print("\n roll not in detabase \n")
def modify(name,roll,course,marks):
    if roll in detabase:
        res=["name:"+name,"roll : "+roll,"course : "+course,"marks : "+marks]
        detabase[roll]=res
    else :
        print("\n roll not in detabase \n")
def marksheet():
    file = " markseet.txt"
    with open(file,"w") as file:
        file.write(" ")
    for key, values in detabase.items():
        res=values
        print(res)
        file = " markseet.txt"
        with open(file,"a") as file:
            for i in res:
                file.write(f"{i}"+", ")
def delete(roll):
    if roll in detabase:
        del detabase[roll]
    else :
        print("\n roll not in detabase \n")
def coursesearch(course):
    a=0
    file = " markseet.txt"
    with open(file,"w") as file:
        file.write(" ")
    for ke,val in detabase.items():
        i=val[2]
        res=i.split()
        if course in res:
            print(val)
            a+=1
            file = " markseet.txt"
            with open(file,"a") as file:
                for i in val:
                    file.write(f"{i}"+", ")
    if a==0:
        print("no course registered")
def namesearch(name):
    a=0
    file = " markseet.txt"
    with open(file,"w") as file:
        file.write(" ")
    for ke,val in detabase.items():
        i=val[0]
        res=i.split(" : ")
        if name in res:
            print(val)
            a+=1
            file = " markseet.txt"
            with open(file,"a") as file:
                for i in val:
                    file.write(f"{i}"+", ")
    if a==0:
        print("no person with that registered")
while a!= 0:
    b=int(input(("enter :: (1) for insert new student, (2) for search student, (3) for update records, (4) for modify records, (5) for generate marksheet, (6) for delete student record, (7) to exit : ")))
    if b==7:    #to exit
        file = " detabase1.txt"
        with open(file,"w") as file:
            for key, value in detabase.items():
                for i in value:
                    file.write(f"{i}"+", ")
        a=0
    elif b==1:    #for insert new student
        name=input("enter name : ")
        roll=input("roll : ")
        course=input("enter course : ")
        marks=input("enter marks : ")
        insert(name,roll,course,marks)
        file = " detabase1.txt"
        with open(file,"w") as file:
            for key, value in detabase.items():
                for i in value:
                    file.write(f"{i}"+", ")
    elif b==2:    #for search student
        c=int(input("enter (1) for search by roll no, (2) for search by course, (3) for search by name : "))
        if c== 1:  #for search by roll no
            roll=input("enter roll : ")
            search(roll)
        elif c==2:   #for search by course
            course=input("enter ccoursee name : ")
            coursesearch(course)
        elif c==3:   #for search by name
            name=input("enter name : ")
            namesearch(name)
    elif b==3:    #for update records
        roll=input("enter roll : ")
        marks=input("enter marks : ")
        update(roll,marks)
        file = " detabase1.txt"
        with open(file,"w") as file:
            for key, value in detabase.items():
                for i in value:
                    file.write(f"{i}"+", ")
    elif b==4:    #for modify records
        roll=input("enter roll to modify : ")
        name=input("enter name : ")
        course=input("enter course : ")
        marks=input("enter marks : ")
        modify(name,roll,course,marks)
        file = " detabase1.txt"
        with open(file,"w") as file:
            for key, value in detabase.items():
                for i in value:
                    file.write(f"{i}"+", ")
    elif b==5:    #for generate marksheet
        c=int(input('enter (1) for generate for all student, (2) for specific course, (3) for a suednt: '))
        if c==1:    #for generate for all student
            marksheet()
        elif c==2:    #for specific course
            course=input("enter coursee name : ")
            coursesearch(course)
            
        elif c==3:
            d=int(input("enter (1) for generate by roll, (2) for gnerate by name : "))
            if d== 1:  #for generate by roll no
                roll=input("enter roll : ")
                val=(search(roll))
                generateMarksheet(val)
            elif d==2:   #for generate by name
                name=input("enter name : ")
                namesearch(name)
    elif b==6:    #for delete student record
        roll=input("enter roll : ")
        delete(roll)
        file = " detabase1.txt"
        with open(file,"w") as file:
            for key, value in detabase.items():
                for i in value:
                    file.write(f"{i}"+", ")