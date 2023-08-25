from django.contrib import admin
# import modeLs from crm app
from .models import ContactInfo, Company, Person


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'contact_info')
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'contact_info')
    ordering = ('name',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'company', 'contact_info')
    list_display = ('first_name', 'last_name', 'company')
    list_filter = ('company',)
    search_fields = ('first_name', 'last_name', 'company', 'contact_info')
    ordering = ('last_name', 'first_name')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    fields = ('email', 'phone', 'street', ('city', 'state', 'zip_code'))
    list_display = ('email', 'phone', 'street', 'city', 'state', 'zip_code')
    list_filter = ('state',)
    search_fields = ('email', 'phone', 'street', 'city', 'state', 'zip_code')
    ordering = ('state', 'city', 'street')
