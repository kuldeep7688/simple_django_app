from django.urls import path
# from rest_framework.routers import SimpleRouter
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views


# router = SimpleRouter()
# router.register('products', views.ProductViewSet)
# router.register('collections', views.CollectionViewSet)

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# router.register('reviews', views.ReviewViewSet)


urlpatterns = router.urls + products_router.urls

# urlpatterns = [
#     # path("products/", views.product_list),
#     path("products/", views.ProductList.as_view()),
#     # path("products/<iknt:id>/", views.product_detail),
#     # path("products/<int:id>/", views.ProductDetail.as_view()),
#     path("products/<int:pk>/", views.ProductDetail.as_view()),
#     # path("collections/", views.collection_list),
#     path("collections/", views.CollectionList.as_view()),
#     # path("collections/<int:pk>/", views.collection_detail, name="collection-detail"),
#     # path("collections/<int:pk>/", views.collection_detail, name="collection-detail"),
#     path("collections/<int:pk>/", views.CollectionDetail.as_view(), name="collection-detail"),
#     path("reviews/", views.ReviewList.as_view()),
#     path("reviews/<int:pk>", views.ReviewDetail.as_view()),
# ]