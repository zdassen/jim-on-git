from django.contrib import admin

from .models import Article, Point, Thought


# Register your models here.
models = (Article, Point, Thought)
for model in models:
    admin.site.register(model)