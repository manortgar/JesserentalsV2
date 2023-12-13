from core import views
from django.urls import path
from core import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_month_to_cart,
    add_to_cart,
    admin_user,
    order_list,
    remove_month_from_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    aboutUs,
    admin_item,
    user_list,
    pedidos_user, buscador, edit_user, delete_user
    
)

app_name = 'core'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('all-products/', views.products, name='products'),
    path('category/<str:category>/', HomeView.as_view(), name='home-category'),
    path('manufacturer/<str:fabricante>/', HomeView.as_view(), name='home-fabricante'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-month-to-cart/rental/<slug>/', add_month_to_cart, name='add-month-to-cart'),
    path('add-to-cart/purchase/<slug>/', add_to_cart, name='add-to-cart-purchase'),
    path('add-to-cart/rental/<slug>/', add_to_cart, name='add-to-cart-rental'),
    path('admin-item/<slug>/', admin_item, name='admin-item'),
    path('admin-user/<user>/', admin_user, name='admin-user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('user-list/', user_list, name='user-list'),
    path('order-list/', order_list, name='order-list'),
    path('buscador/', buscador, name='buscador'),
    path('pedidos/', pedidos_user, name='pedidos_user'), 
    path('remove-month-from-cart/rental/<slug>/', remove_month_from_cart, name='remove-month-from-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('opinions/' ,views.opinions,name='opinions'),
    path('opinions/<int:opinion_id>/', views.opinions_details,name="opinionDetails"),
    path('opinions/create/<slug>', views.create_opinion,name="opinionCreate"),
    path('opinions/<int:opinion_id>/addResponse/', views.createResponse,name="responseCreate"),
    path('claims/create', views.create_claim, name='create-claim'),
    path('claims/list', views.claims_list, name='claims-list'),
    path('claims/<int:claim_id>', views.claim_details, name='claim-details'),
    path('claims/<int:claim_id>/change', views.change_claim_status, name='change-claim-status'),
    path('profile/',views.profile),
    path('about-us/' ,aboutUs,name='about-us'),
    path('condiciones/' ,views.condiciones,name='condiciones'),
    path('politica/' ,views.politica,name='politica'),
    path('borrar_producto/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add-item', views.add_item, name='add_item'),
    path('', views.escaparate, name='escaparate')
]


