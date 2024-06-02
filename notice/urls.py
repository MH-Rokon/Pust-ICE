from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('notice/', views.notice, name="notice"),
    path('event/', views.event, name="event"),
    path('programoffered/', views.programoffered, name="programoffered"),
    path('admissionnotice/', views.admissionnotice, name="admissionnotice"),
    path('research/', views.research, name="research"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
