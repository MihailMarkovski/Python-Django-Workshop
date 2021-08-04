from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like

#filtering by name and age in the panel
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'age']
    list_filter = ['type', 'age']


admin.site.register(Pet, PetAdmin)
admin.site.register(Comment)
# admin.site.register(Like)