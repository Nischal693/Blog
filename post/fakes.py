from faker import Faker
import random
from post.models import Post
images=["post/wallpaperflare.com_wallpaper_1.jpg",
        "post/wallpaperflare.com_wallpaper.jpg"]
def insert_fake_data_in_post():
    fake=Faker()
    for i in range(40):
        Post.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(),
            image=random.choice(images)
        )