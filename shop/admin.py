from django.contrib import admin
from .models import Kategori, Product, Catalog, UserProfile, Cart, CartItem, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock_produk', 'is_active']
    search_fields = ['name', 'category__name']

admin.site.register(Kategori)
admin.site.register(Product, ProductAdmin)
admin.site.register(Catalog)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
