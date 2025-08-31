from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db.models import Q, Count
from django.http import JsonResponse
from .models import Profile, Education, Skill, Project, WorkExperience, Certification, Achievement
from .serializers import (
    ProfileSerializer, ProfileSummarySerializer, EducationSerializer,
    SkillSerializer, ProjectSerializer, WorkExperienceSerializer,
    CertificationSerializer, AchievementSerializer
)

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        """Get profile summary with stats"""
        profile = self.get_object()
        serializer = ProfileSummarySerializer(profile)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get the main profile (assuming single user system)"""
        try:
            profile = Profile.objects.first()
            if not profile:
                return Response({"error": "Profile not found"}, status=404)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.all()
        category = self.request.query_params.get('category')
        proficiency = self.request.query_params.get('proficiency')
        
        if category:
            queryset = queryset.filter(category=category)
        if proficiency:
            queryset = queryset.filter(proficiency=proficiency)
            
        return queryset

    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top skills (advanced/expert level)"""
        top_skills = Skill.objects.filter(proficiency__in=['advanced', 'expert'])
        serializer = SkillSerializer(top_skills, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get skills grouped by category"""
        categories = {}
        for choice in Skill.CATEGORY_CHOICES:
            category_key, category_name = choice
            skills = Skill.objects.filter(category=category_key)
            categories[category_key] = {
                'name': category_name,
                'skills': SkillSerializer(skills, many=True).data
            }
        return Response(categories)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        skill = self.request.query_params.get('skill')
        status_filter = self.request.query_params.get('status')
        
        if skill:
            queryset = queryset.filter(technologies__icontains=skill)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured projects (those with achievements)"""
        featured = Project.objects.exclude(achievements='')
        serializer = ProjectSerializer(featured, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def technologies(self, request):
        """Get all technologies used across projects"""
        projects = Project.objects.all()
        all_technologies = []
        for project in projects:
            all_technologies.extend(project.technologies)
        
        # Count occurrences and return sorted list
        tech_counts = {}
        for tech in all_technologies:
            tech_counts[tech] = tech_counts.get(tech, 0) + 1
        
        sorted_techs = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)
        return Response([{"name": tech, "count": count} for tech, count in sorted_techs])

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

@api_view(['GET'])
def search(request):
    """Global search across skills, projects, and education"""
    query = request.GET.get('q', '').strip()
    
    if not query:
        return Response({"error": "Query parameter 'q' is required"}, status=400)
    
    # Search across multiple models
    results = {
        'skills': [],
        'projects': [],
        'education': [],
        'work_experience': []
    }
    
    # Search skills
    skills = Skill.objects.filter(
        Q(name__icontains=query) | 
        Q(category__icontains=query)
    )
    results['skills'] = SkillSerializer(skills, many=True).data
    
    # Search projects
    projects = Project.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(technologies__icontains=query)
    )
    results['projects'] = ProjectSerializer(projects, many=True).data
    
    # Search education
    education = Education.objects.filter(
        Q(institution__icontains=query) |
        Q(degree__icontains=query) |
        Q(field_of_study__icontains=query)
    )
    results['education'] = EducationSerializer(education, many=True).data
    
    # Search work experience
    work = WorkExperience.objects.filter(
        Q(company__icontains=query) |
        Q(role__icontains=query) |
        Q(description__icontains=query)
    )
    results['work_experience'] = WorkExperienceSerializer(work, many=True).data
    
    # Add metadata
    total_results = sum(len(results[key]) for key in results.keys())
    
    return Response({
        'query': query,
        'total_results': total_results,
        'results': results
    })

@api_view(['GET'])
def stats(request):
    """Get overall profile statistics"""
    try:
        profile = Profile.objects.first()
        if not profile:
            return Response({"error": "Profile not found"}, status=404)
            
        stats_data = {
            'total_skills': profile.skills.count(),
            'total_projects': profile.projects.count(),
            'total_certifications': profile.certifications.count(),
            'total_achievements': profile.achievements.count(),
            'skills_by_category': {},
            'projects_by_status': {},
            'top_technologies': []
        }
        
        # Skills by category
        for choice in Skill.CATEGORY_CHOICES:
            category_key, category_name = choice
            count = profile.skills.filter(category=category_key).count()
            if count > 0:
                stats_data['skills_by_category'][category_key] = {
                    'name': category_name,
                    'count': count
                }
        
        # Projects by status
        for choice in Project.STATUS_CHOICES:
            status_key, status_name = choice
            count = profile.projects.filter(status=status_key).count()
            if count > 0:
                stats_data['projects_by_status'][status_key] = {
                    'name': status_name,
                    'count': count
                }
        
        # Top technologies
        projects = profile.projects.all()
        tech_counts = {}
        for project in projects:
            for tech in project.technologies:
                tech_counts[tech] = tech_counts.get(tech, 0) + 1
        
        sorted_techs = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        stats_data['top_technologies'] = [
            {"name": tech, "count": count} for tech, count in sorted_techs
        ]
        
        return Response(stats_data)
        
    except Exception as e:
        return Response({"error": str(e)}, status=500)