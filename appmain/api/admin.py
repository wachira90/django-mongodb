from django.contrib import admin
from .models import Musician, Album

# Register your models here.
class AlbumDisp(admin.ModelAdmin):
    list_display = ('artist', 'name', 'release_date', 'num_stars')

admin.site.register(Album, AlbumDisp)

class MusicianDisp(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument')

admin.site.register(Musician, MusicianDisp)