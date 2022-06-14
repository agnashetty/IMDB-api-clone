from django.contrib import admin
from .models import watchlist, StreamPlatform, Review

# Register your models here.
@admin.register(watchlist)
class Movieadmin(admin.ModelAdmin):
    model = watchlist
    list_display= ['id', 'title', 'storyline', 'active','created']

@admin.register(StreamPlatform)
class Streamadmin(admin.ModelAdmin):
    model = StreamPlatform
    list_display= ['id','name', 'website', 'about']

@admin.register(Review)
class Reviewadmin(admin.ModelAdmin):
    model: Review
    list_display= ['rating','description', 'user', 'watchlist']

