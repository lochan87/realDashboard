from fastapi import APIRouter, HTTPException
from models import Dashboard

router = APIRouter(prefix="/dashboards", tags=["Dashboards"])

# In-memory storage for dashboards
dashboards = {}

@router.post("/")
async def create_dashboard(dashboard: Dashboard):
    """Create a new dashboard."""
    dashboard_id = str(len(dashboards) + 1)  # Simple ID generation
    dashboards[dashboard_id] = dashboard.dict()
    return {"id": dashboard_id, "message": "Dashboard created successfully"}

@router.get("/")
async def get_dashboards():
    """Retrieve all dashboards."""
    return dashboards

@router.put("/{id}")
async def update_dashboard(id: str, dashboard: Dashboard):
    """Update an existing dashboard."""
    if id not in dashboards:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    dashboards[id] = dashboard.dict()
    return {"message": "Dashboard updated successfully"}

@router.delete("/{id}")
async def delete_dashboard(id: str):
    """Delete a dashboard."""
    if id not in dashboards:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    del dashboards[id]
    return {"message": "Dashboard deleted successfully"}
