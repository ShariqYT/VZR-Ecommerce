from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product);
admin.site.register(TopDeal);
admin.site.register(Contact);
admin.site.register(Orders);
admin.site.register(Coupon);
admin.site.register(OrderUpdate);