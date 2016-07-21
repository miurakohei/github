from django.contrib import admin
from cms.models import User


# admin.site.register(user)

class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','post','address')
    list_display_links=('id','name')
admin.site.register(User,UserAdmin)
