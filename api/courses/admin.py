from django.contrib import admin
from .models import Category, Course


# custom admin site
class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'active']
    search_fields = ['id', 'name']
    list_filter = ['created_date']

admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
