A=open("newfile.txt","a+",encoding="utf-8")
def Menu():
    while True:
        print("1.Enter Exam Note\n2.Read All Exam Scores\n3.Quit")
        Result=input(":")
        if Result=="3":
            print("Logged Out")
            A.close()
            break
        elif Result=="1":
            Name=input("Enter Student Name:  ")
            ExamNote=int(input("Enter Exam Note:  "))
            ExamNote1=int(input("Enter Another Exam Note:  "))
            ExamNote2=int(input("Enter Another Exam Note:  "))
            Total=(ExamNote+ExamNote1+ExamNote2)/3
            if ExamNote<0 or ExamNote1<0 or ExamNote2<0:
                print("Wrong Notes")
            elif Total>=50:
                A.write(f"Name:{Name} Exam Result:{Total} Status:Passed\n")
            elif 0<Total<50:
                A.write(f"Name:{Name} Exam Result:{Total} Status:Failed\n")
        elif Result=="2":
            A.seek(0)
            check=A.read()
            print(check)
Menu()
