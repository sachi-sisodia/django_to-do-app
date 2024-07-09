from django.urls import path
from tasks import views


urlpatterns = [
    path('add/',views.showtaskformdata,name="tasksadd"),
    path('home/',views.showtasksummary, name="tasksummary" ),
    path('<int:id>/', views.update_task, name="taskupdate"),
    path('delete/<int:id>/', views.delete_task, name="taskdelete"),
]
