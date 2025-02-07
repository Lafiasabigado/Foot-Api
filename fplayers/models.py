from django.db import models

# Create your models here.
class Player(models.Model):
    firstname = models.CharField(max_length=300,verbose_name="Firstname")
    lastname = models.CharField(max_length=300,verbose_name="Lastname")
    date_of_birthday = models.DateField(null=True,blank=True,verbose_name="Date of birthday")
    nationality = models.CharField(max_length=150)
    club = models.CharField(max_length=150)
    salary  = models.IntegerField(default=70000)
    position = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    image = models.URLField(null=True,blank=True)
    goals = models.IntegerField(default=50)
    assists = models.IntegerField(default=50)

    def __str__(self):
        return self.lastname

