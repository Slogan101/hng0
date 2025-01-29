from fastapi import FastAPI, status
from datetime import datetime as dt, timezone
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

email = "newson190@gmail.com"
github_url = "https://github.com/Slogan101/hng0.git"
current_datetime = dt.now(timezone.utc).isoformat()


@app.get("/home", status_code=status.HTTP_200_OK)
def get_details():
    return {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }

