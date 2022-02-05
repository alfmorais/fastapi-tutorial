from fastapi import FastAPI

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