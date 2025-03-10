from django.contrib import admin
from django.urls import path, include  # Added include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Added this line
]