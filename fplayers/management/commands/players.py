from django.core.management.base import BaseCommand
from fplayers.models import Player
from faker import Faker
import random

class Command(BaseCommand):
    help = "Peuple la base de données avec des joueurs aléatoires"

    def handle(self, *args, **kwargs):
        fake = Faker()
        positions = ["Goalkeeper","Central midfielder","Attacking midfielder","Defensive midfielder"]
        for _ in range(50):
            Player.objects.create(
                firstname=fake.first_name_male(),
                lastname=fake.last_name_male(),
                date_of_birthday=fake.date_of_birth(minimum_age=18, maximum_age=40),
                nationality=fake.country(),
                club=fake.company(),
                salary=random.randint(5000, 200000000),
                goals=random.randint(0, 1000),
                assists=random.randint(0, 2000),
                position = random.choice(positions),
                image =f"https://randomuser.me/api/portraits/men/{fake.random_int(min=1, max=99)}.jpg",
                is_active=fake.boolean(chance_of_getting_true=80)
            )
        self.stdout.write(self.style.SUCCESS("Base de données peuplée avec succès !"))
