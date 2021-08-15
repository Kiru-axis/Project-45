from django.contrib import admin
from .models import Customer,Creditor,Debtor,MyDebts
# Register your models here.

admin.site.register(Customer)
admin.site.register(Creditor)
admin.site.register(Debtor)
admin.site.register(MyDebts)