from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello,world.You're at the poll index.")


def detail(request, question_id):
    return HttpResponse("you are looking %s." % question_id)


def result(request, question_id):
    response = "you are looking at the result %s" % question_id
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse("you are voting on question %s" % question_id)
