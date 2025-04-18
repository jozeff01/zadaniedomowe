from django.core.management.base import BaseCommand
from hits.models import Artist, Hit
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with demo artists and hits"

    def handle(self, *args, **kwargs):
        artists = []
        for _ in range(3):
            artist = Artist.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            artists.append(artist)

        for _ in range(20):
            title = fake.sentence(nb_words=3)
            Hit.objects.create(
                title=title,
                artist=random.choice(artists)
            )
        self.stdout.write(self.style.SUCCESS("Seed data created!"))