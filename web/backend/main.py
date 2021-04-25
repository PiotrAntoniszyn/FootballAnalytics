import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/passes")
def get_passes():
    with open("fixtures/mock_data.json", "r") as f:
        data = json.loads(f.read())
    passes = [
        {
            "playerID": ev["playerId"],
            "minute": ev["minute"],
            "second": ev["second"],
            "x": ev["x"] * 1.2,
            "endX": ev["endX"] * 1.2,
            "y": ev["y"] * 0.8,
            "endY": ev["endY"] * 0.8,
            "playType": ev["type"]["displayName"],
            "outcome": ev["outcomeType"]["displayName"]
        }
        for ev in data["events"]
        if ev["type"]["displayName"] == "Pass"
    ]
    return {"message": "Hello Football Anal!", "passes": passes}
