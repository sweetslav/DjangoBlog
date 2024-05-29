from .models import Product, Order, Client
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_description_summary', 'price', 'quantity', 'date_added')
    list_filter = ('name', 'date_added')
    search_fields = ('name', 'quantity', 'price')
    readonly_fields = ('date_added',)
    actions = ['reset_quantity_to_zero']
    fieldsets = (
        (
            'Product information', {
                'fields': ('name', 'description', 'price', 'photo'),
                'classes': ('wide',)
            }
        ),
        (
            'Warehouse Details', {
                'fields': ('quantity', 'date_added',),
                'classes': ('wide',)
            }
        ),
    )

    def reset_quantity_to_zero(self, request, queryset):
        queryset.update(quantity=0)

    reset_quantity_to_zero.short_description = 'Сбросить количество до нуля'

    def get_description_summary(self, obj):
        words = obj.description.split()[:5]
        return ' '.join(words)

    get_description_summary.short_description = 'Description summary'


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_registered')
    list_filter = ('date_registered',)
    search_fields = ('name', 'address')
    readonly_fields = ('date_registered',)
    # actions = []
    fieldsets = (
        (
            'Client Information', {
                'fields': ('name', 'email', 'phone', 'date_registered')
            }
        ),
        (
            None, {
                'fields': ('address',),
                'classes': ('collapse',)
            }
        ),
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_client_name', 'get_products', 'total', 'status', 'date_ordered')
    list_filter = ('status', 'date_ordered')
    search_fields = ('client__name', 'products__name')  # Изменено на 'client__name' и 'products__name' для поиска по именам клиентов и продуктов
    readonly_fields = ('date_ordered',)

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    get_products.short_description = 'Products'

    def get_client_name(self, obj):
        return obj.client.name
    get_client_name.short_description = 'Client'

    fieldsets = (
        (None, {
            'fields': ('client', 'total', 'status', 'date_ordered'),
        }),
        ('Products', {
            'fields': ('products',),
        }),
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
