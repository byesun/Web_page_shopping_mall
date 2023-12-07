from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from cart.views import add_to_cart,cart,checkout
from core.views import frontpage,shop,signup,login_old
from product.views import product

urlpatterns = [
    path('',include('core.urls')),
    path('cart/',include('cart.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)