from django.contrib import admin
from django.urls import path
from kurakshopprojekt import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path("dosum/", views.dosum_chat, name="dosum_chat"),
    path('product/', views.product_list, name='product_list'),
]





path('register/', views.register_view, name='register'),


path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),


urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),  # эгер home функциясы болсо
]


urlpatterns = [
    path('home/', views.home, name='home'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),  # главный экран
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),

    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # User
    path('profile/', views.profile_view, name='profile'),

    # Products
    path('products/', views.product_list, name='product_list'),

    # Camera
    path('camera/', views.camera_view, name='camera'),

    # Search
    path('search/', views.search_view, name='search'),
]
