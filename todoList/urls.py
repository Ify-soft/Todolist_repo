
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls', namespace='todo')),
    path('member/', include('django.contrib.auth.urls')),
    path('member/', include('member.urls', namespace='member')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
