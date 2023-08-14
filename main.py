import base64

# import uvicorn
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def page():
    return FileResponse(path="index.html", media_type="text/html")

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/to_base64/{url:path}")
async def to_base64(url: str, APIKey: str, APIToken: str):
    response = requests.get(
        url,
        headers={
            "Authorization": f'OAuth oauth_consumer_key="{APIKey}", oauth_token="{APIToken}"'
        },
    )

    encoded = b"data:image/png;base64," + base64.b64encode(response.content)
    return encoded.decode("utf-8")


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")
