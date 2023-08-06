from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Country)
admin.site.register(AccountConfig)
admin.site.register(FeeAccountConfig)
admin.site.register(AccountingEntry)
admin.site.register(Biller)
admin.site.register(BillerField)
admin.site.register(Provider)
admin.site.register(Channel)
