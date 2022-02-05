from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
async def root():
    """ 
    Request for the GET method.
    URL = "/"

    Returns:
        dict: Information regarding "hello world"
    """
    return {"message": "Welcome to My API"}


@app.get("/posts")
def get_posts():
    """
    Request for the GET method.
    URL = "/posts"

    Returns:
        dict: Information regarding posts
    """
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    """
    Request for the POST method.
    URL = "/createposts"

    Args:
        payload (dict, optional): JSON body to send for API

    Returns:
        dict: Succes message
    """
    title = payload["title"]
    content = payload["content"]
    
    new_post = {
        "new_post": f"title: {title}",
        "content": f"content: {content}",
    }
    
    return new_post