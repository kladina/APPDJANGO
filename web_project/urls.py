from django.contrib import admin
from django.urls import path
from hello import views  # Stellen Sie sicher, dass Sie Ihre App importieren
from hello.views import home, blog_posts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('blog/', blog_posts, name='blog_posts'),
    path('hello/<str:name>/', views.hello_there, name='hello_there'),
    #path("<name>", views.hello_there, name="hello_there"),
    path("it_is_me", views.it_is_me, name="hello_it_is_me"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# Leitet die Root-URL zu Ihrer View um

