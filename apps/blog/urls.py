from django.urls import path
from .views import HomeView, BlogView, PostView, PageView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='posts'),
    path('blog/<slug>/', PostView.as_view(), name='post'),
    path('<slug>/', PageView.as_view(), name='page'),
]