from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from recipes.models import Recipe
import os


def delete_cover(isinstance):
    try:
        os.remove(isinstance.cover.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=Recipe)
def recipe_cover_delete(sender, instance, *args, **kwargs):
    old_instance = Recipe.objects.get(pk=instance.pk)
    delete_cover(old_instance)
 
    
@receiver(pre_save, sender=Recipe)
def recipe_cover_update(sender, instance, *args, **kwargs):
    old_instance = Recipe.objects.get(pk=instance.pk)
    is_new_cover = old_instance.cover != instance.cover
    
    if is_new_cover:
        delete_cover(old_instance)