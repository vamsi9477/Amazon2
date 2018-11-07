"""AmazonWebsite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ama import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex),

    path('head/',views.HeadSection),
    path('body/', views.BodySection),

    path('register/',views.Register),
    path('registration/',views.Registration),

    path('login/',views.Login),

    path("accountexist/",views.accountexist),
    path("accountdetails/",views.AccountalreadyExist),
    path("productdetails/",views.ProductDetails),

    path("aboutus/",views.AboutUs),

    path("contactus/",views.ContactUs),

    path("Home/",views.HomePage),

    path("wiki/",views.wikipedia),

    path("proceed1/",views.purchase),
    path("proceed/",views.purchaseItem),


    path("addcart/",views.Addcart),

    path("logout/",views.Logout),

    path("comment/",views.Comments),
    path("comments/",views.CommentsSection),

    path("adminstration/",views.Adminstration),
    path("adminstrationdetails/",views.AdminstrationDetails),

    path("viewproduct/",views.viewProduct),
    path("viewproductDetails/",views.viewProductDetails),

    path("viewpurchase/", views.viewPurchase),
    path("viewpurchasedetails/", views.viewPurchaseDetails),

]
