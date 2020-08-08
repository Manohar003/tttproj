from django.contrib import admin
from .models import Submitnum

class SubmitnumAdmin(admin.ModelAdmin):
    fields=["ttt_datime",
            "ttt_text"]

admin.site.register(Submitnum)
# Register your models here.
