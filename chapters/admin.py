from django.contrib import admin

# Register your models here.
from .models import Chap, Pair, Call, IChap, IPair

admin.site.register(Chap)
admin.site.register(Pair)
admin.site.register(Call)
admin.site.register(IChap)
admin.site.register(IPair)