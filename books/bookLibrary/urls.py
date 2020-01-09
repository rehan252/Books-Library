from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'BookLibrary'
"""
router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
"""

urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='home'),
    path('upload/', views.upload, name='upload-book'),
    path('delete/<int:id>', views.book_delete, name='delete-book'),
    path('details/<int:id>', views.details, name='details'),
    path('edit/<int:id>', views.edit, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
