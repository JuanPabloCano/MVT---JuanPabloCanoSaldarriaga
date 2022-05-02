from django.urls import path
from my_first_mvt_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('relatives', views.relatives),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)