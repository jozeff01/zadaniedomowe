from django.urls import path
from .views import root_view, HitListCreateView, HitDetailView

urlpatterns = [
    path('', root_view),  # ← корневая страница
    path('api/v1/hits', HitListCreateView.as_view()),
    path('api/v1/hits/<slug:title_url>', HitDetailView.as_view()),
]