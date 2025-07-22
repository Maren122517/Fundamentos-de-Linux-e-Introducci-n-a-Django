from django.urls import path

from ecommerce import views

urlpatterns = [
    path("", views.product_model_list_view, name="list"),
    path("<int:product_id>", views.product_model_detail_view, name="detail"),
    path("create", views.product_model_create_view, name="create"),
    path("<int:product_id>/edit/", views.product_model_update_view, name="update"),
    path("<int:product_id>/delete/", views.product_model_delete_view, name="delete"), 

    path('product/<int:product_id>/update/description/', views.product_model_description_view, name='update_description'),
    path('product/<int:product_id>/update/seller/', views.product_model_seller_view, name='update_seller'),
    path('product/<int:product_id>/update/color/', views.product_model_color_view, name='update_color'),
    path('product/<int:product_id>/update/dimensions/', views.product_model_dimensions_view, name='update_dimensions'),
]
