import base64

# import uvicorn
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://0.0.0.0:5000",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def page():
    return FileResponse(path="index.html", media_type="text/html")


@app.get("/to_base64/{url:path}")
async def to_base64(url: str, APIKey: str, APIToken: str):
    print(url)
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




# import base64

# # import uvicorn
# import requests
# from fastapi import FastAPI
# from fastapi.responses import FileResponse
# from fastapi.middleware.cors import CORSMiddleware


# app = FastAPI()

# origins = [
#     "http://localhost:5000",
#     "http://127.0.0.1:5000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# async def page():
#     return FileResponse(path="index.html", media_type="text/html")

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


# @app.get("/to_base64/{url:path}")
# async def to_base64(url: str, APIKey: str, APIToken: str):
#     response = requests.get(
#         url,
#         headers={
#             "Access-Control-Allow-Origin": "*",
#             "Authorization": f'OAuth oauth_consumer_key="{APIKey}", oauth_token="{APIToken}"'
#         },
#     )

#     encoded = b"data:image/png;base64," + base64.b64encode(response.content)
#     return encoded.decode("utf-8")


# # if __name__ == "__main__":
# #     uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")
