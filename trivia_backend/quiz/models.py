from django.db import models

# Create your models here.
class Question(models.Model):
    query= models.CharField(max_length = 100)
    choice1 =models.CharField(max_length= 100, default = '')
    choice2 =models.CharField(max_length= 100, default = '')
    choice3 =models.CharField(max_length= 100, default = '')
    choice4 =models.CharField(max_length= 100, default = '')
    correct_choice = models.IntegerField()
    #quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.query


# class Quiz(models.Model):
#     name = models.CharField(max_length =  100)
#     duration = models.integerField()
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)

#     def __str__(self):
#         return self.name

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
