from django.contrib import admin

# Register your models here.
from .models import Cart
admin.site.register(Cart)


from .models import CartItem
admin.site.register(CartItem)