from django.db import models


class StreamPlatform(models.Model):
    pass




class  WatchList(models.Model):
    title = models.CharField('Filmes',max_length=50)
    storyline = models.CharField('Descrição', max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    