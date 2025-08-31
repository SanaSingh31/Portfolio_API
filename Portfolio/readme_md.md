# Portfolio API - Personal Resume Backend System

A comprehensive backend application that serves as a personal API playground for profile management. Built with Django REST Framework and React, featuring a complete database-driven resume system with search capabilities.

## 🚀 Live Demo

- **Frontend URL**: `https://your-app.vercel.app` (Update after deployment)
- **Backend API**: `https://your-api.render.com/api/` (Update after deployment)
- **Health Check**: `https://your-api.render.com/health/`

## 📋 Table of Contents

- [Architecture](#architecture)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Setup Instructions](#setup-instructions)
- [Deployment](#deployment)
- [Known Limitations](#known-limitations)
- [Resume Link](#resume-link)

## 🏗 Architecture

```
Frontend (React)     Backend (Django)     Database (PostgreSQL)
     │                       │                       │
     │── API Calls ──────────│── ORM Queries ───────│
     │                       │                       │
     │── Search UI           │── REST Endpoints      │── Profile Data
     │── Profile Display     │── Authentication      │── Skills & Projects
     │── Filtering           │── Data Validation     │── Work Experience
```

### Technology Stack

**Backend:**
- Django 4.2.7
- Django REST Framework
- PostgreSQL (Production) / SQLite (Development)
- Gunicorn (WSGI Server)

**Frontend:**
- React 18
- Tailwind CSS
- Lucide React (Icons)

**Deployment:**
- Backend: Render/Railway
- Frontend: Vercel/Netlify
- Database: PostgreSQL on Render

## ✨ Features

### Core Functionality
- ✅ Complete CRUD operations for profile data
- ✅ Advanced search across all profile content
- ✅ Skill-based project filtering
- ✅ Categorized skill management
- ✅ Real-time statistics and analytics
- ✅ Health check endpoint
- ✅ Responsive web interface

### API Capabilities
- RESTful API with proper HTTP methods
- Query parameter filtering
- Pagination support
- JSON response format
- CORS enabled for frontend integration

### Database Features
- Normalized schema design
- Foreign key relationships
- Array fields for technologies
- Proper indexing for search performance
- Data validation and constraints

## 📚 API Documentation

### Base URL
```
Production: https://your-api.render.com
Development: http://localhost:8000
```

### Authentication
Currently configured for open access. Add authentication in production.

### Core Endpoints

#### Health Check
```bash
GET /health/
Response: {"status": "ok"}
```

#### Profile Management
```bash
# Get main profile
GET /api/profiles/me/
Response: Complete profile with all related data

# Get profile summary
GET /api/profiles/1/summary/
Response: Profile with statistics

# Update profile
PUT /api/profiles/1/
Content-Type: application/json
Body: {"name": "New Name", "email": "new@email.com"}
```

#### Skills API
```bash
# List all skills
GET /api/skills/
Response: Paginated list of skills

# Filter by category
GET /api/skills/?category=programming
Response: Programming skills only

# Get top skills
GET /api/skills/top/
Response: Advanced and expert level skills

# Get skills by category
GET /api/skills/categories/
Response: Skills grouped by category
```

#### Projects API
```bash
# List all projects
GET /api/projects/
Response: Paginated list of projects

# Filter by technology
GET /api/projects/?skill=python
Response: Projects using Python

# Get featured projects
GET /api/projects/featured/
Response: Projects with achievements

# Get technology statistics
GET /api/projects/technologies/
Response: Technology usage counts
```

#### Global Search
```bash
# Search across all content
GET /api/search/?q=AI
Response: {
  "query": "AI",
  "total_results": 5,
  "results": {
    "skills": [...],
    "projects": [...],
    "education": [...],
    "work_experience": [...]
  }
}
```

#### Statistics
```bash
# Get profile statistics
GET /api/stats/
Response: {
  "total_skills": 25,
  "total_projects": 3,
  "skills_by_category": {...},
  "projects_by_status": {...},
  "top_technologies": [...]
}
```

### Sample cURL Commands

```bash
# Health check
curl -X GET https://your-api.render.com/health/

# Get profile
curl -X GET https://your-api.render.com/api/profiles/me/

# Search for Python projects
curl -X GET "https://your-api.render.com/api/projects/?skill=python"

# Global search
curl -X GET "https://your-api.render.com/api/search/?q=machine%20learning"

# Get top skills
curl -X GET https://your-api.render.com/api/skills/top/
```

## 🗄 Database Schema

### Entity Relationship Diagram

```
Profile (1:N) ── Education
        │
        ├─── Skills
        │
        ├─── Projects
        │
        ├─── Work Experience
        │
        ├─── Certifications
        │
        └─── Achievements
```

### Key Tables

1. **Profile**: Main entity with personal information
2. **Skills**: Technical and soft skills with proficiency levels
3. **Projects**: Project portfolio with technologies and achievements
4. **Education**: Educational background
5. **Work Experience**: Professional experience and leadership roles
6. **Certifications**: Professional certifications and courses
7. **Achievements**: Awards and recognitions

### Database Features
- PostgreSQL array fields for technologies
- Full-text search indexes
- Proper foreign key constraints
- Optimized indexes for common queries

For detailed schema information, see [schema.md](schema.md)

## 🛠 Setup Instructions

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL (for production)

### Backend Setup

1. **Clone and setup virtual environment**
```bash
git clone <your-repo-url>
cd portfolio-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Environment configuration**
Create `.env` file in project root:
```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3  # For development
# For production with PostgreSQL:
# DATABASE_URL=postgresql://username:password@host:port/dbname
```

4. **Database setup**
```bash
python manage.py makemigrations
python manage.py migrate
python seed_data.py  # Seed with your resume data
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Configure API URL**
Update `API_BASE_URL` in `src/App.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000';  // Development
// const API_BASE_URL = 'https://your-api.render.com';  // Production
```

4. **Start development server**
```bash
npm start
```

Frontend will be available at `http://localhost:3000`

## 🚀 Deployment

### Backend Deployment (Render)

1. **Create Render account** and connect GitHub repository

2. **Environment Variables** (Render Dashboard):
```bash
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://...  # Provided by Render PostgreSQL
ALLOWED_HOSTS=your-app-name.onrender.com
```

3. **Build Command**:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

4. **Start Command**:
```bash
gunicorn portfolio_api.wsgi:application
```

### Frontend Deployment (Vercel)

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Deploy**
```bash
cd frontend
vercel
```

3. **Update API URL** in deployed frontend to point to your backend

### Database Setup (PostgreSQL on Render)

1. Create PostgreSQL database on Render
2. Update `DATABASE_URL` in environment variables
3. Run migrations: `python manage.py migrate`
4. Seed data: `python seed_data.py`

## 🔍 Testing the API

### Manual Testing
```bash
# Test health endpoint
curl https://your-api.render.com/health/

# Test profile retrieval
curl https://your-api.render.com/api/profiles/me/

# Test project filtering
curl "https://your-api.render.com/api/projects/?skill=Django"

# Test global search
curl "https://your-api.render.com/api/search/?q=AI"
```

### Using the Frontend
1. Visit your deployed frontend URL
2. Use the search bar to test global search
3. Click on skill tags to filter projects
4. Navigate through different tabs to explore data

## ⚠️ Known Limitations

1. **Authentication**: Currently open access - implement authentication for production use
2. **Rate Limiting**: No rate limiting implemented - add for production
3. **File Uploads**: No file upload functionality for project images/documents
4. **Caching**: No caching layer - consider Redis for better performance
5. **Real-time Updates**: No WebSocket support for real-time notifications
6. **Advanced Search**: Basic text search only - could implement Elasticsearch for better search
7. **API Versioning**: No API versioning implemented
8. **Input Validation**: Basic validation only - could be enhanced

### Security Considerations for Production
- Add proper authentication (JWT/OAuth)
- Implement rate limiting
- Add input sanitization
- Configure proper CORS origins
- Enable HTTPS only
- Add request logging and monitoring

## 🔗 Resume Link

**Sana Singh's Resume**: [View Resume PDF](Resume_Sana.pdf)

## 📞 Contact Information

- **Name**: Sana Singh
- **Email**: sansingh3102@gmail.com
- **Phone**: 947-269-8952
- **LinkedIn**: [LinkedIn Profile](https://linkedin.com/in/sana-singh)
- **GitHub**: [GitHub Profile](https://github.com/sanasingh)

## 🤝 Contributing

This is a personal portfolio project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ by Sana Singh** • *Manipal University Jaipur*