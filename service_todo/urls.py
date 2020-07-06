from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from todo_list import views

from todo_list.views import MyLoginView, MySignupView

urlpatterns = [
    path('', views.main_page, name="tasks_list"),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('new_task/', views.new_task, name='new_task'),
    path('save_task/<int:id>/', views.save_task, name='save_task'),
    path('login/', MyLoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('signup/', MySignupView.as_view(), name='signup_view'),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
