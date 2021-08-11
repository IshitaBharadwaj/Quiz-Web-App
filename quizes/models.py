from django.db import models

import random

CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)


#For defining a quiz topic
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number]

    class Meta:
        verbose_name_plural = 'Quizes'