from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet, SkillViewSet, ExperienceViewSet,
    EducationViewSet, ServiceViewSet, ResumeViewSet,
    SocialLinkViewSet, ContactMessageViewSet
)

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('skills', SkillViewSet, basename='skill')
router.register('experience', ExperienceViewSet, basename='experience')
router.register('education', EducationViewSet, basename='education')
router.register('services', ServiceViewSet, basename='service')
router.register('resume', ResumeViewSet, basename='resume')
router.register('social-links', SocialLinkViewSet, basename='sociallink')
router.register('contact', ContactMessageViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
