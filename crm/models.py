from django.db import models
from django.core.validators import RegexValidator

# add address model with email, phone with validator, street, city, state, and zip code
class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=200, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2, validators=[RegexValidator(r'^[A-Z]{2}$')])
    zip_code = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{5}$')])

    def __str__(self):
        return self.street

# Create company model with required name and contact info
class Company(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# Create person model with first name, last name, foreign key to company, and foreign key to contact info
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

