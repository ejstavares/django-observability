from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

### str method for better representation of the object in admin and shell
    def __str__(self):
        return self.nome