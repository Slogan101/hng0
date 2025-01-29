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
github_url = "https://github.com/Slogan101/hng0"
current_datetime = dt.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-2] + "Z"

#dt.now(timezone.utc).isoformat()

# dt.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")




@app.get("/", status_code=status.HTTP_200_OK)
def get_details():
    return {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }

