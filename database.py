import datetime
import os
import typing
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, select, Session

import dotenv

dotenv.load_dotenv()

DB_NAME = os.getenv('DB_NAME')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
MAIN_USER = os.getenv('MAIN_USER')
MAIN_PASSWORD = os.getenv('MAIN_PASSWORD')


class MyTable(SQLModel, table=True):
    """
    Создание таблицы Blog для проекта "Мое резюме"
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    body: str
    creation_data: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)

    # creation_data: datetime.datetime = Field(default_factory=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
    # print(creation_data.utcnow.replace(microsecond=0))


engine = create_engine(f"postgresql+psycopg2://{MAIN_USER}:{MAIN_PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

SQLModel.metadata.create_all(engine)


def create_post_blog(title, body) -> None:
    """
    Создание поста в блоге

    :param title: объект типа str
    :param body: объект типа str
    :return: None
    """
    new_post = MyTable(title=title, body=body)

    with Session(engine) as session:
        session.add(new_post)

        session.commit()


def get_posts_labels() -> typing.Union[list]:
    """
    Получение списка названий постов из БД

    :return: объект типа list
    """

    with Session(engine) as session:
        result = []
        statement = select(MyTable.id, MyTable.title)
        results = session.exec(statement)
        for post in results:
            result.append(": ".join(str(i) for i in post))
    return result


def del_post(post_id) -> None:
    """
    Удаление поста из БД

    :param post_id: int
    :return: None
    """

    with Session(engine) as session:
        statement = select(MyTable).where(MyTable.id == post_id)
        results = session.exec(statement)
        post = results.one()
        print("Post: ", post)

        session.delete(post)
        session.commit()


def load_post(post_id) -> typing.Union["post"]:
    """
    Загрузка поста в БД

    :param post_id: Int
    :return: объект типа post
    """
    with Session(engine) as session:
        statement = select(MyTable).where(MyTable.id == post_id)
        results = session.exec(statement)
        post = results.one()
        print("Post: ", post)
        return post


def update_post(post_id, title, body) -> int:
    """
    Изменение поста в БД

    :param post_id: Int
    :return: None
    """
    with Session(engine) as session:
        statement = select(MyTable).where(MyTable.id == post_id)
        results = session.exec(statement)
        post = results.one()
        print("Post:", post)

        # post = post.title, post.body
        post.title = title
        post.body = body

        session.add(post)
        session.commit()

        session.refresh(post)

# changer_post()

# get_posts_labels()
# create_post_blog()
