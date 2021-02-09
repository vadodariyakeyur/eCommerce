from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Address, Coupon, Refund, UserProfile


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=True, refund_granted=True)


make_refund_accepted.short_description = "Grant Refund"


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon',
                    ]

    list_display_links = ['billing_address',
                          'shipping_address',
                          'payment',
                          'coupon',
                          'user'
                          ]

    list_filter = ['user',
                   'ordered',
                   'payment',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted'
                   ]

    search_fields = [
        'user__username',
        'ref_code'
    ]

    actions = [
        make_refund_accepted,
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user__username', 'street_address', 'apartment_address', 'zip']


# Register your models here.
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(UserProfile)
