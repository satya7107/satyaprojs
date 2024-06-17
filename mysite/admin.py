from django.contrib import admin

#Register your models here.
from .models import product
class productadmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields={'slug':('product_name',)}
admin.site.register(product,productadmin)