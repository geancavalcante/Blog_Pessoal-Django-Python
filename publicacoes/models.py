from django.db import models

    
class Books(models.Model):
    book = models.CharField(max_length=10)
    link = models.CharField(max_length=10)

    def __str__(self):
        return 'livros'
    









    