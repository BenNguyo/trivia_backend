from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import viewsets
from rest_framework.response import Response

#pk = 1

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class= QuestionSerializer

    # def list(self, request):
    #     info = Question.objects.get(id=1)
    #     serializer = self.get_serializer(info)
    #     return Response(serializer.data)
    


# class QuizViewset(viewsets.ModelViewSet):
#     queryset= Quiz.objects.all()
#     serializer_class=QuizSerializer

# class CategoryViewset(viewsets.ModelViewSet):
#     queryset= Category.objects.all()
#     serializer_class=CategorySerializer




