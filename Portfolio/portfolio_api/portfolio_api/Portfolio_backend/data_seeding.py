import os
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_api.settings')
django.setup()

from portfolio.models import Profile, Education, Skill, Project, WorkExperience, Certification, Achievement

def seed_data():
    # Clear existing data
    Profile.objects.all().delete()
    
    # Create main profile
    profile = Profile.objects.create(
        name="Sana Singh",
        email="sansingh3102@gmail.com",
        phone="947-269-8952",
        linkedin="https://linkedin.com/in/sana-singh",  # Update with actual URL
        github="https://github.com/sanasingh",  # Update with actual URL
        summary="An Information Technology undergraduate at Manipal University Jaipur with a growing interest in backend systems, automation, and platform engineering. Skilled in Python, SQL, and Django, with exposure to Power BI, PySpark, and cloud platforms. Currently exploring big data technologies, deep learning, and NLP as part of this semester's coursework. Passionate about practical projects that foster learning, collaboration, and innovation.",
        cgpa=8.69
    )

    # Education
    Education.objects.create(
        profile=profile,
        institution="Manipal University Jaipur",
        degree="Bachelor of Technology",
        field_of_study="Information Technology",
        start_date=date(2022, 9, 1),
        end_date=date(2026, 7, 31),
        cgpa=8.69,
        is_current=True
    )

    # Skills data based on resume
    skills_data = [
        # Programming Languages
        ('Python', 'programming', 'advanced'),
        ('Java', 'programming', 'intermediate'),
        ('C', 'programming', 'intermediate'),
        ('C++', 'programming', 'intermediate'),
        ('SQL', 'programming', 'advanced'),
        
        # Data & ML Tools
        ('Pandas', 'data_ml', 'advanced'),
        ('NumPy', 'data_ml', 'advanced'),
        ('Matplotlib', 'data_ml', 'intermediate'),
        ('Seaborn', 'data_ml', 'intermediate'),
        ('scikit-learn', 'data_ml', 'advanced'),
        ('TensorFlow', 'data_ml', 'intermediate'),
        ('NLTK', 'data_ml', 'intermediate'),
        
        # Data Engineering & Analytics
        ('ETL Pipelines', 'data_engineering', 'intermediate'),
        ('Data Cleaning', 'data_engineering', 'advanced'),
        ('Data Warehousing', 'data_engineering', 'beginner'),
        ('PySpark', 'data_engineering', 'intermediate'),
        ('Power BI', 'data_engineering', 'beginner'),
        ('Streamlit', 'data_engineering', 'intermediate'),
        ('MySQL', 'data_engineering', 'intermediate'),
        ('MongoDB', 'data_engineering', 'beginner'),
        
        # Cloud & Platforms
        ('Google Cloud Platform', 'cloud', 'beginner'),
        
        # ML & AI Techniques
        ('Regression', 'ml_ai', 'advanced'),
        ('Classification', 'ml_ai', 'advanced'),
        ('Clustering', 'ml_ai', 'intermediate'),
        ('Random Forest', 'ml_ai', 'advanced'),
        ('Gradient Boosted Trees', 'ml_ai', 'intermediate'),
        ('ANN', 'ml_ai', 'intermediate'),
        ('CNN', 'ml_ai', 'intermediate'),
        ('Transformers', 'ml_ai', 'beginner'),
        ('NLP', 'ml_ai', 'intermediate'),
        ('Tokenization', 'ml_ai', 'intermediate'),
        ('TF-IDF', 'ml_ai', 'advanced'),
        
        # Web Development
        ('HTML', 'web_dev', 'intermediate'),
        ('CSS', 'web_dev', 'intermediate'),
        ('JavaScript', 'web_dev', 'intermediate'),
        ('REST APIs', 'web_dev', 'advanced'),
        ('Django', 'web_dev', 'advanced'),
        ('React.js', 'web_dev', 'beginner'),
        ('Bootstrap', 'web_dev', 'intermediate'),
        
        # Developer Tools
        ('Git', 'tools', 'advanced'),
        ('GitHub', 'tools', 'advanced'),
        ('VS Code', 'tools', 'advanced'),
        
        # Soft Skills
        ('Problem-Solving', 'soft_skills', 'advanced'),
        ('Analytical Thinking', 'soft_skills', 'advanced'),
        ('Collaboration', 'soft_skills', 'advanced'),
        ('Communication', 'soft_skills', 'advanced'),
    ]

    # Create skills
    for skill_name, category, proficiency in skills_data:
        Skill.objects.create(
            profile=profile,
            name=skill_name,
            category=category,
            proficiency=proficiency
        )

    # Projects based on resume
    projects_data = [
        {
            'title': 'AI-Driven Research Engine for Legal Sector',
            'description': 'Developed a legal research engine using AI to help professionals retrieve and interpret judicial precedents. Engineered Django-based backend modules for intelligent case retrieval, legal query processing, and integrated them with a React-based UI. Collaboratively implemented 3+ automation features, including an automated judge allocation system, timeline tracking, and multilingual support.',
            'technologies': ['Django', 'React', 'MySQL', 'AI', 'NLP', 'REST APIs'],
            'start_date': date(2024, 8, 1),
            'status': 'ongoing',
            'achievements': 'Achieved 2nd Runner-Up position at Startup Conclave 2025 and was selected for incubation by Atal Incubation Center, MUJ'
        },
        {
            'title': 'Sentiment Analysis of User Reviews',
            'description': 'Compiled and processed a custom dataset of 1,000+ user reviews from diverse sources to analyze sentiment trends. Trained classifiers using TF-IDF features, achieving 82% test accuracy with SVM and Logistic Regression models. Applied core NLP techniques using NLTK and scikit-learn. Visualized sentiment distribution to support data-driven content feedback analysis.',
            'technologies': ['Python', 'scikit-learn', 'NLTK', 'TF-IDF', 'SVM', 'Logistic Regression'],
            'start_date': date(2025, 1, 1),
            'end_date': date(2025, 4, 30),
            'status': 'completed',
            'achievements': 'Achieved 82% test accuracy with machine learning models'
        },
        {
            'title': 'Diabetes Prediction using Machine Learning',
            'description': 'Analyzed health indicators of 768 patients from the PIMA dataset to identify key features contributing to diabetes prediction. Demonstrated 85% accuracy using Random Forest and optimized ANN outcomes through tuning of model layers and learning parameters. Enhanced model performance with feature scaling, correlation analysis, and class balancing techniques. Assessed model outputs using ROC-AUC, confusion matrix, and other classification metrics.',
            'technologies': ['Python', 'ANN', 'Random Forest', 'scikit-learn', 'Machine Learning'],
            'start_date': date(2024, 9, 1),
            'end_date': date(2024, 10, 31),
            'status': 'completed',
            'achievements': 'Achieved 85% accuracy using Random Forest and optimized ANN models'
        }
    ]

    # Create projects
    for project_data in projects_data:
        Project.objects.create(
            profile=profile,
            **project_data
        )

    # Certifications
    certifications_data = [
        {
            'name': 'Getting Started with Git and GitHub',
            'issuer': 'IBM',
            'issue_date': date(2024, 6, 1)
        },
        {
            'name': 'Tools for Data Science',
            'issuer': 'IBM',
            'issue_date': date(2024, 7, 1)
        },
        {
            'name': 'Django Web Framework',
            'issuer': 'IBM',
            'issue_date': date(2024, 8, 1)
        },
        {
            'name': 'Data Analysis Using PySpark',
            'issuer': 'Coursera Project Network',
            'issue_date': date(2024, 9, 1)
        }
    ]

    # Create certifications
    for cert_data in certifications_data:
        Certification.objects.create(
            profile=profile,
            **cert_data
        )

    # Achievements
    achievements_data = [
        {
            'title': 'Smart India Hackathon (SIH) 2025 Selection',
            'description': 'Selected among the top 50 teams from 1400+ in the intra-college round at Manipal University Jaipur',
            'date_achieved': date(2025, 1, 15),
            'organization': 'Government of India'
        },
        {
            'title': 'Academic Excellence Recognition',
            'description': 'Recognized twice for achieving the highest grade point average in multiple semesters',
            'date_achieved': date(2024, 12, 1),
            'organization': 'Manipal University Jaipur'
        },
        {
            'title': 'Startup Conclave 2025 - 2nd Runner-Up',
            'description': 'AI-Driven Research Engine for Legal Sector project achieved 2nd Runner-Up position',
            'date_achieved': date(2025, 1, 20),
            'organization': 'Manipal University Jaipur'
        },
        {
            'title': 'Atal Incubation Center Selection',
            'description': 'Legal research engine project selected for incubation by Atal Incubation Center, MUJ',
            'date_achieved': date(2025, 2, 1),
            'organization': 'Atal Incubation Center, MUJ'
        }
    ]

    # Create achievements
    for achievement_data in achievements_data:
        Achievement.objects.create(
            profile=profile,
            **achievement_data
        )

    # Leadership experience as work experience
    WorkExperience.objects.create(
        profile=profile,
        company="LearnIT - Manipal University Jaipur",
        role="President",
        description="Led a team of 25+ members to organize 5+ technical events, enhancing collaboration, peer learning, and overall student engagement",
        start_date=date(2024, 5, 1),
        end_date=date(2025, 5, 1),
        is_current=True,
        location="Jaipur, India"
    )

    print("✅ Data seeded successfully!")
    print(f"Created profile for: {profile.name}")
    print(f"Skills: {profile.skills.count()}")
    print(f"Projects: {profile.projects.count()}")
    print(f"Certifications: {profile.certifications.count()}")
    print(f"Achievements: {profile.achievements.count()}")

if __name__ == '__main__':
    seed_data()