from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Registered(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    phone_message = 'Phone number must be entered in the format: 9*********'

    # your desired format
    phone_regex = RegexValidator(
        regex=r'^(9)\d{9}$',
        message=phone_message
    )

    # finally, your phone number field
    mobile = models.CharField(validators=[phone_regex], max_length=10,
                              null=True, blank=True, unique=True)
