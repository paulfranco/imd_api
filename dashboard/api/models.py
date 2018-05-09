from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Carrier(models.Model):
    company_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.company_name

class Settlement(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()
    quarter = models.IntegerField()
    check_number = models.IntegerField()
    paid = models.BooleanField(default=False)
    stop_count = models.IntegerField()
    route_count = models.IntegerField()
    revenue = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    REGULAR = 'RG'
    ELITE = "EL"
    BONUS = 'BO'
    OTHER = 'OT'
    SETTLEMENT_TYPE_CHOICES = (
        (REGULAR, 'Regular'),
        (ELITE, 'Elite'),
        (BONUS, 'Bonus'),
        (OTHER, 'Other')
    )
    settlement_type = models.CharField(max_length=2,
                                       choices=SETTLEMENT_TYPE_CHOICES,
                                       default=REGULAR,
                                       )

    def __str__(self):
        return self.title


class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    truck_number = models.IntegerField()
    route_date = models.DateField()
    mileage = models.IntegerField()
    piece_count = models.IntegerField()
    stop_count = models.IntegerField()
    #route_revenue = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    #settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE)


