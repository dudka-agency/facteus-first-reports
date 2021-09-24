from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('views/', include('polls.urls')),
    path('admin/', admin.site.urls),
]