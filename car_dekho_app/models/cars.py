from django.db import models

# Create your models here.
from django.db import models
from django.forms import ValidationError
def alphanumeric(value):
    if not value.isalnum():
        raise ValidationError(
            '%(value)s is not alphanumeric',
            params={'value': value},
        )
# Create your models here.
class Cars(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length = 100, blank = True, null = True, validators=[alphanumeric])
    price = models.DecimalField(max_digits=9, decimal_places=2, blank = True, null = True)
    
    def __str__(self):
        return self.name