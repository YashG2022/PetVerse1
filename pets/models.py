from django.db import models

class pets(models.Model):
    petidnumber=models.AutoField(primary_key=True)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    birth_date = models.DateField()
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
       return self.breed
# Create your models here.
