from unicodedata import category

from django.db import models
from django.db.models import CASCADE


class Document (models.Model):
    series = models.CharField(max_length = 4)
    number = models.CharField(max_length = 6)
    date_of_issue = models.DateField()
    issued_by = models.CharField(max_length = 50)

class Category (models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits= 9, decimal_places= 2)
    description = models.TextField()

class Item(models.Model):
    name = models.CharField(max_length = 50)

class Guess(models.Model):
    fio = models.CharField(max_length = 60)
    numbers = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits = 5, decimal_places= 2)

class Room(models.Model):
    floor = models.IntegerField()
    room_count = models.IntegerField()
    bed_count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Equipment(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    item = models.ForeignKey(Item, on_delete=CASCADE)

    class Meta:
        unique_together = ('category', 'item')

class Booking(models.Model):
    client = models.ForeignKey(Guess, on_delete=CASCADE)
    room = models.ForeignKey(Room, on_delete=CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    cost = models.DecimalField(max_digits = 9, decimal_places= 2)
    fact_of_payment = models.BooleanField(default=False)

class Service(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 9, decimal_places= 2)
    description = models.TextField()

class ServiceProvision (models.Model):
    booking = models.ForeignKey(Booking, on_delete=CASCADE)
    service = models.ForeignKey(Service, on_delete=CASCADE)
    count = models.IntegerField()
    date = models.DateField()

