from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields=('query', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choice',)
        