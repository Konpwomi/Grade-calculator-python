print('''==============================================================
***********      Welcome to Grade Calculator      ************
==============================================================''')
id = int(input("Enter student's ID : "))
name = input("Enter student's name : ")
fac = input("Enter student's facculty : ")
print(' ')
amount = int(input("Enter your amount : "))
subject = []
credit = []
grade = []
gc = []
for i in range (amount) :
  sec1 = input("Enter Subject %d : " %(i+1))
  subject.append(sec1)
  sec2 = int(input("Enter Credit : "))
  credit.append(sec2)
  sec3 = input("Enter Grade : ")
  grade.append(sec3)
  print("==============================================================")
  if sec3 == "A" :
     result=sec2*4
     gc.append(result)
  if sec3 == "B+" :
     result=sec2*3.5
     gc.append(result)
  if sec3 == "B" :
     result=sec2*3
     gc.append(result)
  if sec3 == "C+" :
     result=sec2*2.5
     gc.append(result)
  if sec3 == "C" :
     result=sec2*2
     gc.append(result)
  if sec3 == "D+" :
     result=sec2*1.5
     gc.append(result)
  if sec3 == "D" :
     result=sec2*1
     gc.append(result)
  if sec3 == "F" :
     result=sec2*0
     gc.append(result)
Gpa = sum(gc)/sum(credit)
print('''============================================================== 
|                      Grade Calculator                      | 
==============================================================''')
print("Student ID. %d" %id)
print('Name: %s' %name)
print('School: %s' %fac)
print('''==============================================================
|          Subject         |     Credit(s)     |    Grade    |             
==============================================================''')
for i in range (amount) :
  print(subject[i+0],credit[i+0],'               ',grade[i+0])
print('''=============================================================
                      | GPA. %.2f |
=============================================================''' % Gpa)