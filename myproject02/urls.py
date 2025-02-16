from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import student_list, student_detail, student_add, student_edit, student_delete # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('student_records.urls')),
    path('', student_list, name='student_list'),
    path('<int:student_id>/', student_detail, name='student_detail'),
    path('add/', student_add, name='student_add'),
    path('edit/<int:student_id>/', student_edit, name='student_edit'),
    path('delete/<int:student_id>/', student_delete, name='student_delete'),
]
