from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('buyproduct/(<name>)', views.buy, name='buy'),
    path('makepayment/', views.makepayment, name='makepayment'),
    path('signin/',views.sign_up,name="signup"),
    path('signup/',views.sign_up,name="signup"),
    path('user_login/',views.user_login,name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('(<name>)',views.add_item,name='add_item'),
     path('contactus',views.contactus,name='contactus'),
    path('cart/',views.goto_cart,name='cart'),
    path('cart/(<name>)',views.del_item,name='del_item'),
    path('thanks_for_order/',views.placed_order,name='placed_order')

]
