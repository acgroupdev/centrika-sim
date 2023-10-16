from django.db import models


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50)
    ticket_id = models.CharField(max_length=50)
    ticket_reference = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    card_id = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=20)
    route_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
