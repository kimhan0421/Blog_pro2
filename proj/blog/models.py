from django.db import models 

class Blog(models.Model):    
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField() #Object error 해결위함
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]