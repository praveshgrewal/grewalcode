from django.contrib import admin
from .models import Testimonial, Blog


# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'created_at')
    list_filter = ('role', 'rating', 'created_at')
    search_fields = ('name', 'message')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'author')
    ordering = ('-created_at',)