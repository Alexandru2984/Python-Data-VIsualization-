from django.contrib import admin

# Register your models here.


from .models import Product, Category

admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description",)
    search_fields = ("name",)
    prepopulated_fields = {"slug" : ("name",)}
