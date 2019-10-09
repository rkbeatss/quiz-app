from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FilePathField(path="/img")

    def _str_(self):
    	return self.name, self.description
    
#ForeignKey defines a many to one relationship
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)

    def _str_(self):
    	return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE) #many question instances in one quiz
    description = models.CharField(max_length=255)
    def _str_(self):
    	return self.description
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers') #many answers to a question
    text = models.CharField(max_length=255)
    is_answer = models.BooleanField(default=False)
    
    def _str_(self):
    	return self.text
#implement user type and keeping scores in next iteration
