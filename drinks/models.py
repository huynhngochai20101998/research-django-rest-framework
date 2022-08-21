from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100, null=False, unique=True)
    els_name = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(BaseModel):
    pass


class Drinks(BaseModel):
    image_url = models.URLField(unique=True, blank=True, null=True)
    activate = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
