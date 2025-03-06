from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.dashboard import router as dashboard_router
from websocket_s.data_stream import websocket_data
import uvicorn

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(dashboard_router)
app.add_api_websocket_route("/ws/data", websocket_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
