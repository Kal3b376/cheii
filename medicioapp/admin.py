from django.contrib import admin
from medicioapp.models import Product,Branch,Contact,Appointment

# Register your models.
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Appointment)

