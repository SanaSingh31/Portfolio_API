from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'work-experience', views.WorkExperienceViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'achievements', views.AchievementViewSet)

urlpatterns = [
    # Health check endpoint
    path('health/', views.health_check, name='health_check'),
    
    # API endpoints
    path('api/', include(router.urls)),
    
    # Custom endpoints
    path('api/search/', views.search, name='search'),
    path('api/stats/', views.stats, name='stats'),
]

# URL Patterns Documentation:
"""
Available API Endpoints:

1. Health Check:
   GET /health/ - Returns {"status": "ok"}

2. Profile Management:
   GET /api/profiles/ - List all profiles
   GET /api/profiles/{id}/ - Get specific profile
   POST /api/profiles/ - Create new profile
   PUT /api/profiles/{id}/ - Update profile
   DELETE /api/profiles/{id}/ - Delete profile
   GET /api/profiles/{id}/summary/ - Get profile summary with stats
   GET /api/profiles/me/ - Get main profile

3. Skills:
   GET /api/skills/ - List all skills
   GET /api/skills/?category={category} - Filter by category
   GET /api/skills/?proficiency={level} - Filter by proficiency
   GET /api/skills/top/ - Get top skills (advanced/expert)
   GET /api/skills/categories/ - Get skills grouped by category
   POST /api/skills/ - Create new skill
   PUT /api/skills/{id}/ - Update skill
   DELETE /api/skills/{id}/ - Delete skill

4. Projects:
   GET /api/projects/ - List all projects
   GET /api/projects/?skill={technology} - Filter by technology
   GET /api/projects/?status={status} - Filter by status
   GET /api/projects/featured/ - Get featured projects
   GET /api/projects/technologies/ - Get technology usage stats
   POST /api/projects/ - Create new project
   PUT /api/projects/{id}/ - Update project
   DELETE /api/projects/{id}/ - Delete project

5. Education:
   GET /api/education/ - List education records
   POST /api/education/ - Create education record
   PUT /api/education/{id}/ - Update education record
   DELETE /api/education/{id}/ - Delete education record

6. Work Experience:
   GET /api/work-experience/ - List work experience
   POST /api/work-experience/ - Create work experience
   PUT /api/work-experience/{id}/ - Update work experience
   DELETE /api/work-experience/{id}/ - Delete work experience

7. Certifications:
   GET /api/certifications/ - List certifications
   POST /api/certifications/ - Create certification
   PUT /api/certifications/{id}/ - Update certification
   DELETE /api/certifications/{id}/ - Delete certification

8. Achievements:
   GET /api/achievements/ - List achievements
   POST /api/achievements/ - Create achievement
   PUT /api/achievements/{id}/ - Update achievement
   DELETE /api/achievements/{id}/ - Delete achievement

9. Search & Analytics:
   GET /api/search/?q={query} - Global search across all content
   GET /api/stats/ - Get overall profile statistics

Example Queries:
- /api/projects?skill=python
- /api/skills/top
- /api/search?q=AI
- /api/projects/technologies
- /api/skills?category=programming
"""