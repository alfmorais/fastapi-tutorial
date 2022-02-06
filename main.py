from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "I dont like fish",
        "content": "I like to eat pizza",
        "published": False,
        "rating": 1,
        "id": 1
    },
    {
        "title": "I dont like frontend",
        "content": "I like to learning Python",
        "published": True,
        "rating": 5,
        "id": 2
    },
]


def find_post(id):
    for post in my_posts:
        post_id = post["id"]
        if post_id == id:
            return {"post_detail": post}


@app.get("/")
def hello_world():
    return {"message": "Welcome to My API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1_000_000_000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post_by_id(id: int, response: Response):
    post = find_post(id)

    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        message = f"not found the id: {id} in our database"
        return {"message": message}

    return {"detail_post": post}
