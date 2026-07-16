def name():
    Word=input("Enter Your Word:  ")
    How_many_times=int(input("How Many Times Do you want to see this word:  "))
    while How_many_times>0:
        How_many_times=How_many_times-1
        print(Word)
name()
def unlimited_list(*liste):
    max=list(liste)
    print(max)
unlimited_list(1,2,3,"adana",4,5)

def divide(number):
    return [i for i in range(1,number+1) if number %i==0]
print(divide(21))