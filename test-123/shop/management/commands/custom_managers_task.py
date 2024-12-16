from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from shop.models import Tag, Item, Category, Image, CategoryManager, ItemManager, TagManager

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(CategoryManager.with_item_count())

        print(ItemManager.with_tag_count())

        print(TagManager.popular_tags(1))