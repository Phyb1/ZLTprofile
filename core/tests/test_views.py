import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestZLTProfileViews:
    
    def test_home_page_loads(self, client):
        """Home page should return 200 and use correct template"""
        url = reverse('home')
        response = client.get(url)
        assert response.status_code == 200
        assert 'core/home.html' in [t.name for t in response.templates]
        assert 'Zimbabwe Leaf Tobacco' in response.content.decode()

    def test_about_page_loads(self, client):
        """About page should return 200"""
        url = reverse('about')
        response = client.get(url)
        assert response.status_code == 200
        assert 'core/about.html' in [t.name for t in response.templates]
        assert 'Building Zimbabwe' in response.content.decode()

    def test_services_page_loads(self, client):
        """Services page should return 200"""
        url = reverse('services')
        response = client.get(url)
        assert response.status_code == 200
        assert 'core/services.html' in [t.name for t in response.templates]
        assert 'Auction Marketing' in response.content.decode()

    def test_floors_page_loads(self, client):
        """Floors page should return 200"""
        url = reverse('floors')
        response = client.get(url)
        assert response.status_code == 200
        assert 'core/floors.html' in [t.name for t in response.templates]
        assert 'Aspindale Park' in response.content.decode()

    def test_contact_page_loads(self, client):
        """Contact page should return 200"""
        url = reverse('contact')
        response = client.get(url)
        assert response.status_code == 200
        assert 'core/contact.html' in [t.name for t in response.templates]
        assert 'Contact ZLT' in response.content.decode()

    def test_navbar_contains_zlt_branding(self, client):
        """All pages should contain ZLT branding in navbar"""
        url = reverse('home')
        response = client.get(url)
        content = response.content.decode()
        assert 'ZLT' in content
        assert 'data-bs-theme' in content  # dark mode toggle exists

    def test_all_pages_return_ok(self, client):
        """Smoke test - all URLs should work"""
        urls = ['home', 'about', 'services', 'floors', 'contact']
        for url_name in urls:
            response = client.get(reverse(url_name))
            assert response.status_code == 200, f"{url_name} failed"
