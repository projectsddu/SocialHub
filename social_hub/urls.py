
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('home',include('home.urls')),
    path('search',include('search.urls')),
    path('chat',include('chat.urls')),
    path('business',include('business_dashboard.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

