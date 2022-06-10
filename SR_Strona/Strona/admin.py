from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import Data


class Admin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Data, Admin)