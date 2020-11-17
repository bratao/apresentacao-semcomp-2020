import configparser
import datetime

from diskcache import Cache
from peewee import (
    Model,
    CharField,
    IntegerField, DateTimeField, MySQLDatabase, ForeignKeyField, DateField, FloatField, TextField,

)


env_config = configparser.ConfigParser()
env_config.read('env.ini')
dbname = env_config.get('database', 'database')
host = env_config.get('database', 'host')
username = env_config.get('database', 'user')
password = env_config.get('database', 'password')

cache = Cache()

db = MySQLDatabase(
    dbname,
    user=username,
    password=password,
    host=host,
)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        table_name = "user"

    name = CharField(null=False)
    email = CharField(null=False)


class News(BaseModel):
    class Meta:
        table_name = "news"

    user = ForeignKeyField(User)
    title = CharField(null=False)
    date_published = DateField()

    content = TextField()

    @property
    def count_comments(self):

        if self.id in cache:
            return cache[self.id]
        count_post = Comment.select().where(Comment.news == self).count()
        cache.set(self.id, count_post, expire=60*5)  # 5 min timeout
        return count_post


class Comment(BaseModel):
    class Meta:
        table_name = "comment"

    user = ForeignKeyField(User)

    news = ForeignKeyField(News)
    date_published = DateField()
    content = TextField()


def create_database():
    for db_model in [
        User,
        News,
        Comment
    ]:
        if not db_model.table_exists():
            db_model.create_table()


if __name__ == "__main__":
    create_database()
