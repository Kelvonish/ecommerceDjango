"""nishsoko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponseRedirect
#from blog.views import blog
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from products.views import index, product, search
from cart.views import add_to_cart
from accounts.views import register
from blogs.views import blog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('product/<int:id>/', product, name='product'),
    path('register/', register, name='register'),
    path('search/', search, name='search'),
    path('cart/<slug>/', add_to_cart, name='cart'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('blog/', blog, name='blog'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=staticfiles_urlpatterns()
