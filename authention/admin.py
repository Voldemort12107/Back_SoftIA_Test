from django.contrib import admin
from authention.models import Permission,Role,User

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(User)
