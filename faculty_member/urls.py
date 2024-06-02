from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('teacher/', views.teacher, name="teacher"),
    path('OfficeStaff/', views.OfficeStaff, name="OfficeStaff"),
    path('detail/<int:teacher_id>/', views.teacherdetails, name="teacherdetails"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
