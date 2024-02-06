from django.urls import path
from . import views 
from .views import SignupView,Login,PostUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index,name="Index"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('gallery/', views.gallery,name="gallery"),
    path("upload-image/",views.UploadImage, name="upload-image"),
    path('edit-image/<int:pk>',PostUpdateView.as_view(), name='edit-image'),
    path("delete-image/<int:id>/",views.delete_image,name='delete-image'),
]