from django.contrib import admin
from .models import Profile, Education, Skill, Project, WorkExperience, Certification, Achievement

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'cgpa', 'created_at']
    search_fields = ['name', 'email']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'profile']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'profile']
    list_filter = ['status', 'start_date']
    search_fields = ['title', 'description']

admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Certification)
admin.site.register(Achievement)