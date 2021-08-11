from django.db import models
from quizes.models import Quiz


# For a specific question
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()



#To keep track of the correct answer and the option answered  by user.
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
