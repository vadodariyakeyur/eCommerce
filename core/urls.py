from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('product/<slug>/', views.ItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>/', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name="remove-from-cart"),
    path('order-summary/', views.OrderSummaryView.as_view(), name="order-summary"),
    path('checkout/', views.CheckoutView.as_view(), name="checkout"),
    path('add-coupon/', views.AddCoupon.as_view(), name="add-coupon"),
    path('remove-single-item-from-cart/<slug>/', views.remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path('add-single-item-to-cart/<slug>/', views.add_single_item_to_cart, name="add-single-item-to-cart"),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name="payment"),
    path('request-refund/', views.RequestRefundView.as_view(), name="request-refund"),
]
