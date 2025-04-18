from django.test import TestCase

from .models import Artist, Hit

class HitModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(first_name="John", last_name="Doe")
        self.hit = Hit.objects.create(title="Test Song", artist=self.artist)

    def test_title_url_auto_generated(self):
        self.assertEqual(self.hit.title_url, "test-song")
