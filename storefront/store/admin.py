from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Collection)
admin.site.register(models.Product)


# @admin.register(models.Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['featured_product']
#     list_display = ['title', 'products_count']
#     search_fields = ['title']

#     @admin.display(ordering='products_count')
#     def products_count(self, collection):
#         url = (
#             reverse('admin:store_product_changelist')
#             + '?'
#             + urlencode({
#                 'collection__id': str(collection.id)
#             }))
#         return format_html('<a href="{}">{} Products</a>', url, collection.products_count)

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(
#             products_count=Count('product')
#         )