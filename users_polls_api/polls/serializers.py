from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'end_date', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['poll', 'question_text', 'question_type']
