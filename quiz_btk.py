class Question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsIndex=0

    def getQuestion(self):
        return self.questions[self.questionsIndex]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f"soru {self.questionsIndex + 1}:{question.text}" )

        for q in question.choices:
            print("-" + q)
        answer = input("cevap:")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionsIndex+=1
    
    def loadQuestion(self):
        if len(self.questions)==self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
      

    def showScore(self):
        print("score:",self.score)      
    def displayProgress(self):
        totalQuestion =len(self.questions)
        questionNumber=self.questionsIndex + 1

        if questionNumber > totalQuestion:
            print("quiz bitt.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))
        




q1= Question("en iyi programlama dili hangisidir?",["c#","python","javascript","java"],"python")
q2= Question("en popüler programlama dili hangisidir?",["c#","python","javascript","java"],"python")
q3= Question("en çok kazandıran programlama dili hangisidir?",["c#","python","javascript","java"],"python")
questions=[q1,q2,q3]
# print(q1.checkAnswer("python")) #true
# print(q1.checkAnswer("c#")) #false

quiz= Quiz(questions)

quiz.loadQuestion()