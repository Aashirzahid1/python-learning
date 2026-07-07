students=[]
add=[]
while True:
    
    print("""
         1. Add Students
         2. Veiw Students
         3. Update Students
         4. Remove Students
         5. Show Highest Grade
         6. Show Lowest Grade
         7. Show Average Grade
          8. Exit
          9. search student
           """)
    

    num=int(input("Enter the choice"))

    if num==1:
            name=input("Enter the student name")
            add.append(name)
            grade=int(input("Enter his Grade"))
            add.append(grade)
            students.append(add.copy())
            print(students)
            add.clear()
            
    elif num==2:
          for stu in students:
                print(stu)
                print(stu[0]," - ",stu[1])
    elif num==3:
          for stu,index in enumerate(students):
                print(stu,index)
          upgrade=int(input("Enter the index of student whose grade you want to be updated"))
          new_grade=int(input("enter new grade"))
          if 0<=upgrade<=len(students)-1:
                students[upgrade][1]=new_grade
    elif num==4:
          for student,index in enumerate(students):
                print(students,index)
          remove=int(input("enter the student index you want to remove"))
          students.pop(remove)
    elif num==5:
          highest_grade=students[0][1]
          print(highest_grade)
          for student in students:
                      if student[1]>highest_grade:
                            highest_grade=student[1]
          print("The highest grade is:",highest_grade)
    elif num==6:
          lowest_grade=students[0][1]
          for student in students:
                      if student[1]<lowest_grade:
                            lowest_grade=student[1]
          print("the lowest grade is: ",lowest_grade)  
    elif num==7:
          total=0
          count=0
          for student in students:
                      count+=1
                      total+=student[1]
          print(f"Average: {total/count}")
    elif num==8:
          print("Exiting the student portal")
          break
    elif num==9:
           search=input("Enter student name")
           for student in students:
                  if student[0]==search:
                         print(student[0]," - ",student[1])
                  else:
                         print("student not found")