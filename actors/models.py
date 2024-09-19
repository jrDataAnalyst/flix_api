from django.db import models


NATIONALITY_CHOICES = (
    ("USA", 'Estados unidos'),
    ("BRAZIL", 'Brasil'),
    ("CANADA", 'Canada'),
)



# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name
