from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
# Create your views here.


from .models import Question
from .serializers import QuestionSerializer


class QuestionsAPIView(generics.ListCreateAPIView):
    search_fields = ['question_text','author']
    filter_backends = (filters.SearchFilter,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer