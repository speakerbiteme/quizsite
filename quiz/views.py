# coding: utf-8

from django.shortcuts import render


quizzes = {
	"klassiker": {
   		"name": u"Quizzen om Simon",
	   	"description": u"Vet du allt om Simon och hans värld?"
	},
	"fotboll": {
	   	"name": u"Quizzen om Erika",
	   	"description": u"Vet du allt om Erika och hennes värld?"
	},
}

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request):
	return render(request, "quiz/quiz.html")
def question(request):
	return render(request, "quiz/question.html")
def completed(request):
	return render(request, "quiz/completed.html")

# Create your views here.
