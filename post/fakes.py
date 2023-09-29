from accounts.models import User
from faker import Faker
import random
from post.models import Post
images=["post/wallpaperflare.com_wallpaper_1.jpg",
        "post/wallpaperflare.com_wallpaper.jpg"]
def insert_fake_data_in_post():
    fake=Faker()
    users=User.objects.all()
    for i in range(40):
        Post.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(nb_sentences=20),
            image=random.choice(images),
            user=random.choice(users),
        )