from faker import Faker

import db
fake = Faker('en_US')


user_autor = db.User.create(name="Bruno")

for _ in range(200):
    fake_news = db.News()
    fake_news.user = user_autor
    fake_news.title = fake.text(max_nb_chars=100)
    fake_news.content = fake.text(max_nb_chars=1000)
    fake_news.date_published = fake.date_this_decade()
    fake_news.save()

    for _ in range(1000):
        fake_comment = db.Comment()
        fake_comment.user = user_autor
        fake_comment.date_published = fake_news.date_published = fake.date_this_decade()
        fake_comment.content = fake.text(max_nb_chars=100)
        fake_comment.news = fake_news
        fake_comment.save()

