from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField('Nome',max_length=30)
    about = models.CharField('Sobre',max_length=150)
    website = models.URLField('Site',max_length=100)
    
    def __str__(self):
        return self.name
    


class  WatchList(models.Model):
    title = models.CharField('Filmes',max_length=50)
    storyline = models.CharField('Descrição', max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    