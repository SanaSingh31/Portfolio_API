from rest_framework import serializers
from .models import Profile, Education, Skill, Project, WorkExperience, Certification, Achievement

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        extra_kwargs = {'profile': {'write_only': True}}

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        extra_kwargs = {'profile': {'write_only': True}}

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {'profile': {'write_only': True}}

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'
        extra_kwargs = {'profile': {'write_only': True}}

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'
        extra_kwargs = {'profile': {'write_only': True}}

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
        extra_kwargs = {'profile': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    work_experience = WorkExperienceSerializer(many=True, read_only=True)
    certifications = CertificationSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileSummarySerializer(serializers.ModelSerializer):
    total_projects = serializers.SerializerMethodField()
    total_skills = serializers.SerializerMethodField()
    top_skills = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'summary', 'total_projects', 'total_skills', 'top_skills']

    def get_total_projects(self, obj):
        return obj.projects.count()

    def get_total_skills(self, obj):
        return obj.skills.count()

    def get_top_skills(self, obj):
        return obj.skills.filter(proficiency__in=['advanced', 'expert'])[:5].values_list('name', flat=True)