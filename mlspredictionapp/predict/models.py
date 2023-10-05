from django.db import models

# Create your models here.

class Homes(models.Model):
    price = models.IntegerField(("Price"), default=None)
    baths = models.DecimalField(("Baths"), max_digits=4, decimal_places=1, default=None)
    beds = models.IntegerField(("Beds"), default=None)
    square_feet = models.IntegerField(("Square_Feet"), default=None)
    year_built = models.IntegerField(("Year_Built"), default=None)
    garages = models.IntegerField(("Garages"), default=None)
    lot_sqft = models.IntegerField(("Lot_SqFt"), default=None)
