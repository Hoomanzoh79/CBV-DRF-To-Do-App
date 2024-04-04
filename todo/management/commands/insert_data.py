from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User,Profile
from todo.models import Task


class Command(BaseCommand):
    def __init__(self,*args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),password='Test@123456')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.bio = self.fake.paragraph(nb_sentences=5)
        profile.save()

        # create 5 random tasks
        for _ in range(5):
            fake_verb = self.fake.word(part_of_speech="verb")
            fake_noun = self.fake.word(part_of_speech="noun")
            Task.objects.create(
                author=profile,
                is_done=self.fake.boolean(chance_of_getting_true=50),
                title=fake_verb + ' ' + fake_noun
            )