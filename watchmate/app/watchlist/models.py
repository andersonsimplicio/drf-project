from django.db import models

class  Movie(models.Model):
    name = models.CharField('Filmes',max_length=50)
    descriptions = models.CharField('Descrição', max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    