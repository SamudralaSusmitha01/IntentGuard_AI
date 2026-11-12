from app.database import create_tables, get_activity_history
from fastapi import HTTPException
from app.gemini_service import analyze_screenshot
from fastapi import FastAPI
from app.schemas import IntentionRequest
from app.screenshot_service import capture_screenshot
from app.monitoring_service import (
    start_monitoring,
    stop_monitoring,
    get_monitoring_status
)
app = FastAPI(
    title="IntentGuard AI",
    description="A context-aware productivity assistant",
    version="1.0.0"
)
create_tables()

current_intention = None


@app.get("/")
def home():
    return {"message": "Welcome to IntentGuard AI!"}


@app.post("/intention")
def set_intention(data: IntentionRequest):
    global current_intention

    current_intention = data.intention

    return {
        "message": "Intention saved successfully",
        "intention": current_intention
    }


@app.get("/intention")
def get_intention():
    return {
        "intention": current_intention
    }
@app.post("/capture-screen")
def capture_screen():

    image_bytes, width, height = capture_screenshot()

    return {
        "message": "Screenshot captured successfully",
        "width": width,
        "height": height,
        "size_bytes": len(image_bytes),
        "storage": "Temporary in-memory processing"
    }


@app.post("/analyze-screen")
def analyze_current_screen():

    if not current_intention:
        raise HTTPException(
            status_code=400,
            detail="Please set your intention first"
        )

    image_bytes = None

    try:
        # Capture screenshot
        image_bytes, width, height = capture_screenshot()

        # Send screenshot and intention to Gemini
        analysis = analyze_screenshot(
            image_bytes,
            current_intention
        )

        return {
            "message": "Screen analysis completed",
            "screen_dimensions": {
                "width": width,
                "height": height
            },
            "analysis": analysis
        }

    except Exception:
        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=502,
            detail="Screen analysis failed. Check the backend logs."
        )

    finally:
        image_bytes = None


@app.post("/start-monitoring")
def start_screen_monitoring():

    if not current_intention:
        raise HTTPException(
            status_code=400,
            detail="Please set your intention first"
        )

    started = start_monitoring(
        intention=current_intention,
        interval=60
    )

    if not started:
        raise HTTPException(
            status_code=409,
            detail="Monitoring is already active"
        )

    return {
        "message": "Automatic monitoring started",
        "interval_seconds": 60,
        "intention": current_intention
    }


@app.post("/stop-monitoring")
def stop_screen_monitoring():

    stopped = stop_monitoring()

    if not stopped:
        raise HTTPException(
            status_code=400,
            detail="Monitoring is not active"
        )

    return {
        "message": "Monitoring stop requested"
    }


@app.get("/monitoring-status")
def screen_monitoring_status():

    return get_monitoring_status()


@app.get("/activity-history")
def activity_history(limit: int = 50):
    if limit < 1 or limit > 500:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 500"
        )

    records = get_activity_history(limit)

    return {
        "count": len(records),
        "activities": records
    }
