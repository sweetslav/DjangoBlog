from .models import Coin
from django.contrib import admin


class CoinAdmin(admin.ModelAdmin):
    list_display = ('side', 'time')
    list_filter = ('side', 'time')


admin.site.register(Coin, CoinAdmin)
