from django.contrib import admin
from nodes.models import NetworkNode
from nodes.filters import CityFilter
from nodes.actions import clear_debts


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'node_type', 'contact', 'supplier', 'debt', 'created_at')
    list_display_links = ['supplier']
    search_fields = ('id', 'name', 'node_type')
    list_filter = ('node_type', 'supplier', CityFilter,)
    actions = [clear_debts]


admin.site.register(NetworkNode, NetworkNodeAdmin)
