from django.contrib import admin
from .models import Contact


class CityFilter(admin.SimpleListFilter):
    """Filter that allows you to filter network nodes by city of registration"""

    title = 'город'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = set([c.city for c in Contact.objects.all()])
        return [(c, c) for c in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact__city=self.value())
