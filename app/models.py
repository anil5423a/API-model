from django.db import models

# Create your models here.

class Employe(models.Model):
    Eid=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.Ename