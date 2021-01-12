from enum import Enum, unique

from django.db import models


@unique
class QuestionType(Enum):
    text_answer = 'text answer'
    choose_single_answer = 'choose single answer'
    choose_multiple_answer = 'choose multiple answer'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Poll(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(
        max_length=256,
        choices=QuestionType.choices()
    )
