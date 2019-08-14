from django.shortcuts import render
from quizzes.models import Category, Quiz, Question, Answer

#This is an example of a basic function based views

def category_view(request):
    categories = Category.objects.all()
    main_categories = {
        'categories' : categories
        }
    return render(request, 'categories_view.html', main_categories)


def quiz_view(request, pk):
	quizzes = Quiz.objects.filter(category_id=pk)
	quizzes = {
		'quizzes': quizzes
	}
	return render(request, 'quizzes_view.html', quizzes)


def question_view(request, pk):
	questions = Question.objects.filter(quiz_id=pk)
	answers = Answer.objects.filter(question_id = questions[0].id)
	questions = {
		'questions': questions,
		'answers': answers
	}
	return render(request, 'question_view.html', questions)

def add_quiz(request):
	quiz_to_add = "test"
