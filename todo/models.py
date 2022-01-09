from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255, blank=True,null=True)
    
    
    def __str__(self):
        return "{}. {}".format(self.id,self.title)