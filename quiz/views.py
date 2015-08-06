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

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    "question": u"Hur många bultar har ölandsbron?",
		"answer1": u"12",
	   	"answer2": u"66 400",
	    "answer3": u"7 428 954",
	    "quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)

def completed(request):
	return render(request, "quiz/completed.html")

# Create your views here.
