from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
  path("", view=views.home, name="home"),
  path("myAccount/", view=views.myAccount, name="myAccount"),
  path("customerAddress/", view=views.customerAddress, name="customerAddress"),
  path("item/<int:pk>/", views.item, name="item"),
  path("review/", views.review, name="review"),
  path("bookItem/", views.bookItem, name="bookItem"),
  path("cart/", views.cart, name="cart"),
  path("modifyCartItem/", views.modifyCartItem, name="modifyCartItem"),
  path("deleteCartItem/", views.deleteCartItem, name="deleteCartItem"),
  path("payment/", views.payment, name="payment"),
  path("createOrder/", views.createOrder, name="createOrder"),
  path("orderView/", views.orderView, name="orderView"),
  path("search/", views.search, name="search"),
  path("staff_home/", views.staff_home, name="staff_home"),
  path("order_management/<str:status>/", views.order_management, name="order_management"),
  path("order_detail/<int:pk>/", views.order_detail, name="order_detail"),
  path("notification/", views.get_notifycation, name="notification"),
  path("feedback/", views.feedback, name="feedback"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)