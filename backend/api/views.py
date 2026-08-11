from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from portfolio.models import Project, Skill, Experience, Education, Service, Resume, SocialLink, ContactMessage
from .serializers import (
    ProjectSerializer, SkillSerializer, ExperienceSerializer,
    EducationSerializer, ServiceSerializer, ResumeSerializer,
    SocialLinkSerializer, ContactMessageSerializer
)

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SocialLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.filter(is_active=True)
    serializer_class = ResumeSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        active_resume = Resume.objects.filter(is_active=True).first()
        if active_resume:
            serializer = self.get_serializer(active_resume)
            return Response(serializer.data)
        return Response({"detail": "No active resume found."}, status=status.HTTP_404_NOT_FOUND)


class ContactMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
