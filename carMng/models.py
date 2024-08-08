from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publishdate = models.DateField(auto_now_add=True)
    description = models.TextField()
    picture = models.FileField(upload_to='carProject/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    drivetrain = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

