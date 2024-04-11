from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
	    return self.title