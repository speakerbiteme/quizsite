from django.shortcuts import render

def startpage(request):
	return render(request, "quiz/start.html")
def quiz(request):
	return render(request, "quiz/quizstart.html")
def question(request):
	return render(request, "quiz/question.html")
def completed(request):
	return render(request, "quiz/completed.html")

# Create your views here.
