def isGreater(student1,student2) :
    for i in range (1 , len(student1)) :
        if (int(student1[i]) <= int(student2[i])):
            print(student1[i], " ",student2[i])

            return False
    return True






def create_student_list (fhand) :
    students = []
    for line in fhand :
        student = line.strip().split()
        students.append(student)
    return students

fhand=open("studentRanking.txt")
student_list = create_student_list(fhand)
for i in rnage (0,len(students)-1) :






print(isGreater(student_list[0] ,student_list[1]))
# print(student_list)
