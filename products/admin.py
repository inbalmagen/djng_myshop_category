from django.contrib import admin
from .models import Product, Category

# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity')  # Display category fields in admin

# Register Product model with Category many-to-many field
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_categories')  # Display product fields and categories
    filter_horizontal = ('categories',)  # Adds a multi-select widget for categories

    # Define a custom method to show categories in the product list view
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    
    get_categories.short_description = 'Categories'


