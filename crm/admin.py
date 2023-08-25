from django.contrib import admin
# import modeLs from crm app
from .models import ContactInfo, Company, Person


# Register ALL IMPORTED MODELS
admin.site.register(ContactInfo)
admin.site.register(Company)
admin.site.register(Person)

