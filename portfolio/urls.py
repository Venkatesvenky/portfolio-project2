from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, SkillViewSet, ProjectViewSet

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
urlpatterns = [
    path('', include(router.urls)),
]