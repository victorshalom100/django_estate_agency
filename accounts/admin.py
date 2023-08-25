from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'reg_date')
    list_display_links = ('id', 'fullname')
    list_filter = ('reg_date',)
    search_fields = ('fullname',)
    list_per_page = 25


admin.site.register(Users, UsersAdmin)



