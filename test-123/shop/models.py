from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import (Count)



class CategoryManager(models.Manager):
    def with_item_count():
        categories = Category.objects.annotate(item_count=Count('items'))
        for category in categories:
            print(category.name, category.item_count)


class ItemManager(models.Manager):
    def with_tag_count():
        items = Item.objects.annotate(tag_count=Count('tags'))
        for item in items:
            print(item.name, item.tag_count)


class TagManager(models.Manager):
    def popular_tags(min_items):
        return Tag.objects.annotate(items_count=Count('items')).filter(items_count__gt=min_items)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    images = GenericRelation('Image', related_query_name="category")
    objects = CategoryManager()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    images = GenericRelation("Image", related_query_name="item")
    objects = ItemManager()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tags', blank=True)
    objects = TagManager()

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')