class Question:
    def __init__(self,quest,answer):
        self.quest=quest
        self.answer=answer
    def answercheck(self,inputanswer):
        return inputanswer==self.answer
questions=[
Question("What is the answer to 60 + 24?",84),
Question("What is the answer to 100 + 27?",127),
Question("What is the answer to 13 + 9?",22)
]
score=0
for i in questions:
    print(i.quest)
    inputanswer1=int(input("Answer:  "))
    if i.answercheck(inputanswer1):
        score=score+1
    else:
        pass
print(f"Your Score is {score}")