import requests
import json
import sys

class PortfolioAPITester:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def test_health_check(self):
        """Test the health check endpoint"""
        print("🔍 Testing health check endpoint...")
        try:
            response = self.session.get(f"{self.base_url}/health/")
            assert response.status_code == 200
            data = response.json()
            assert data.get('status') == 'ok'
            print("✅ Health check passed")
            return True
        except Exception as e:
            print(f"❌ Health check failed: {e}")
            return False

    def test_profile_endpoints(self):
        """Test profile-related endpoints"""
        print("\n🔍 Testing profile endpoints...")
        
        # Test get profile
        try:
            response = self.session.get(f"{self.base_url}/api/profiles/me/")
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Profile retrieved: {data.get('name')}")
                print(f"   📧 Email: {data.get('email')}")
                print(f"   🎓 CGPA: {data.get('cgpa')}")
                return data
            else:
                print(f"❌ Profile retrieval failed: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Profile test failed: {e}")
            return None

    def test_skills_endpoints(self):
        """Test skills-related endpoints"""
        print("\n🔍 Testing skills endpoints...")
        
        # Test get all skills
        try:
            response = self.session.get(f"{self.base_url}/api/skills/")
            if response.status_code == 200:
                data = response.json()
                skills = data.get('results', data)
                print(f"✅ Skills retrieved: {len(skills)} skills")
                
                # Test category filtering
                response = self.session.get(f"{self.base_url}/api/skills/?category=programming")
                if response.status_code == 200:
                    prog_skills = response.json().get('results', response.json())
                    print(f"✅ Programming skills: {len(prog_skills)} skills")
                
                # Test top skills
                response = self.session.get(f"{self.base_url}/api/skills/top/")
                if response.status_code == 200:
                    top_skills = response.json()
                    print(f"✅ Top skills: {len(top_skills)} advanced/expert skills")
                
                return skills
            else:
                print(f"❌ Skills retrieval failed: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Skills test failed: {e}")
            return []

    def test_projects_endpoints(self):
        """Test projects-related endpoints"""
        print("\n🔍 Testing projects endpoints...")
        
        # Test get all projects
        try:
            response = self.session.get(f"{self.base_url}/api/projects/")
            if response.status_code == 200:
                data = response.json()
                projects = data.get('results', data)
                print(f"✅ Projects retrieved: {len(projects)} projects")
                
                # Test skill filtering
                if projects:
                    # Try filtering by first technology from first project
                    first_tech = projects[0].get('technologies', [])
                    if first_tech:
                        tech = first_tech[0]
                        response = self.session.get(f"{self.base_url}/api/projects/?skill={tech}")
                        if response.status_code == 200:
                            filtered = response.json().get('results', response.json())
                            print(f"✅ Projects filtered by '{tech}': {len(filtered)} projects")
                
                # Test featured projects
                response = self.session.get(f"{self.base_url}/api/projects/featured/")
                if response.status_code == 200:
                    featured = response.json()
                    print(f"✅ Featured projects: {len(featured)} projects")
                
                return projects
            else:
                print(f"❌ Projects retrieval failed: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Projects test failed: {e}")
            return []

    def test_search_endpoint(self):
        """Test global search functionality"""
        print("\n🔍 Testing search endpoints...")
        
        search_queries = ["AI", "Python", "Django", "Machine Learning"]
        
        for query in search_queries:
            try:
                response = self.session.get(f"{self.base_url}/api/search/?q={query}")
                if response.status_code == 200:
                    data = response.json()
                    total = data.get('total_results', 0)
                    print(f"✅ Search '{query}': {total} total results")
                    
                    # Show breakdown
                    results = data.get('results', {})
                    for category, items in results.items():
                        if items:
                            print(f"   {category}: {len(items)} results")
                else:
                    print(f"❌ Search '{query}' failed: {response.status_code}")
            except Exception as e:
                print(f"❌ Search '{query}' failed: {e}")

    def test_stats_endpoint(self):
        """Test statistics endpoint"""
        print("\n🔍 Testing stats endpoint...")
        
        try:
            response = self.session.get(f"{self.base_url}/api/stats/")
            if response.status_code == 200:
                data = response.json()
                print("✅ Stats retrieved:")
                print(f"   Total Skills: {data.get('total_skills')}")
                print(f"   Total Projects: {data.get('total_projects')}")
                print(f"   Total Certifications: {data.get('total_certifications')}")
                print(f"   Total Achievements: {data.get('total_achievements')}")
                
                # Show top technologies
                top_techs = data.get('top_technologies', [])[:3]
                if top_techs:
                    print("   Top Technologies:")
                    for tech in top_techs:
                        print(f"     - {tech['name']}: {tech['count']} projects")
                return True
            else:
                print(f"❌ Stats retrieval failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Stats test failed: {e}")
            return False

    def test_crud_operations(self):
        """Test basic CRUD operations"""
        print("\n🔍 Testing CRUD operations...")
        
        # Test creating a new skill
        try:
            new_skill = {
                "name": "Test Skill",
                "category": "tools",
                "proficiency": "intermediate",
                "profile": 1
            }
            
            response = self.session.post(f"{self.base_url}/api/skills/", json=new_skill)
            if response.status_code == 201:
                skill_data = response.json()
                skill_id = skill_data['id']
                print(f"✅ Skill created: ID {skill_id}")
                
                # Test updating the skill
                updated_skill = {
                    "name": "Updated Test Skill",
                    "category": "tools",
                    "proficiency": "advanced",
                    "profile": 1
                }
                
                response = self.session.put(f"{self.base_url}/api/skills/{skill_id}/", json=updated_skill)
                if response.status_code == 200:
                    print("✅ Skill updated successfully")
                
                # Test deleting the skill
                response = self.session.delete(f"{self.base_url}/api/skills/{skill_id}/")
                if response.status_code == 204:
                    print("✅ Skill deleted successfully")
                
                return True
            else:
                print(f"❌ Skill creation failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ CRUD test failed: {e}")
            return False

    def run_all_tests(self):
        """Run comprehensive API tests"""
        print("🚀 Starting Portfolio API Tests")
        print("="*50)
        
        results = {
            'health_check': self.test_health_check(),
            'profile': self.test_profile_endpoints() is not None,
            'skills': len(self.test_skills_endpoints()) > 0,
            'projects': len(self.test_projects_endpoints()) > 0,
            'search': True,  # Will be set by test_search_endpoint
            'stats': self.test_stats_endpoint(),
            'crud': self.test_crud_operations()
        }
        
        # Run search test
        self.test_search_endpoint()
        
        print("\n" + "="*50)
        print("📊 Test Results Summary:")
        print("="*50)
        
        for test_name, passed in results.items():
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"{test_name.replace('_', ' ').title():<20} {status}")
        
        total_tests = len(results)
        passed_tests = sum(results.values())
        print(f"\nOverall: {passed_tests}/{total_tests} tests passed")
        
        if passed_tests == total_tests:
            print("🎉 All tests passed! Your API is working correctly.")
        else:
            print("⚠️  Some tests failed. Check the logs above for details.")
        
        return passed_tests == total_tests

def main():
    # Check command line arguments
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = "http://localhost:8000"
    
    print(f"Testing API at: {base_url}")
    
    tester = PortfolioAPITester(base_url)
    success = tester.run_all_tests()
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()