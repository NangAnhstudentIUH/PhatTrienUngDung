from django.contrib import admin
from .models import Item
from .models import Location
from .models import User
from .models import Role
from .models import UserRole

from .models import Permission
from .models import PermissionRole

from .models import Tag
from .models import Article

# admin.site.register(Item)
# admin.site.register(Location)

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserRole)

admin.site.register(Permission)
admin.site.register(PermissionRole)

admin.site.register(Tag)
admin.site.register(Article)