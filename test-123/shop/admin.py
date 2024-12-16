from django.contrib import admin
from shop.models import Tag, Item, Category


class ItemInLine(admin.TabularInline):
    model = Item
    extra = 1

class TagInLine(admin.StackedInline):
    model = Item.tags.through
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering = ['name']
    inline = [ItemInLine]

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name', 'description']
    ordering = ['price']
    inline = [TagInLine]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']




admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)