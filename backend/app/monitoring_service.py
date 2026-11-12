
import threading
import logging
from app.database import save_activity
from app.screenshot_service import capture_screenshot
from app.gemini_service import analyze_screenshot

logger = logging.getLogger(__name__)

monitoring_active = False
monitoring_thread = None

stop_event = threading.Event()
monitoring_lock = threading.Lock()

last_analysis = None



def monitoring_loop(intention, interval):

    global monitoring_active, last_analysis

    try:
        while not stop_event.is_set():

            image_bytes = None

            try:
                # Capture screenshot temporarily
                image_bytes, width, height = capture_screenshot()

                # Analyse screenshot using Gemini
                analysis = analyze_screenshot(
                    image_bytes,
                    intention
                )

                # Save analysis results in SQLite
                try:
                    save_activity(intention, analysis)
                    logger.info("Activity saved to database")

                except Exception:
                    logger.exception("Failed to save activity to database")

                result = {
                    "screen_dimensions": {
                        "width": width,
                        "height": height
                    },
                    "analysis": analysis
                }

                with monitoring_lock:
                    last_analysis = result

                logger.info("Screen analysis completed")

            except Exception as e:
                logger.exception("Screen analysis failed")

                error_message = str(e)

                if (
                    "RESOURCE_EXHAUSTED" in error_message
                    or "429" in error_message
                ):
                    logger.error(
                        "Gemini quota exhausted. Stopping monitoring."
                    )
                    stop_event.set()
                    break

            finally:
                image_bytes = None

            # Wait before the next capture
            if stop_event.wait(interval):
                break

    finally:
        with monitoring_lock:
            monitoring_active = False

        logger.info("Monitoring thread stopped")



def start_monitoring(intention, interval=60):

    global monitoring_active, monitoring_thread

    if interval <= 0:
        raise ValueError("Monitoring interval must be greater than zero")

    with monitoring_lock:

        # Prevent multiple monitoring threads
        if monitoring_thread is not None and monitoring_thread.is_alive():
            return False

        stop_event.clear()
        monitoring_active = True

        monitoring_thread = threading.Thread(
            target=monitoring_loop,
            args=(intention, interval),
            daemon=True
        )

        monitoring_thread.start()

        return True


def stop_monitoring():

    with monitoring_lock:

        if not monitoring_active:
            return False

        # Request the background thread to stop
        stop_event.set()

        return True


def get_monitoring_status():

    with monitoring_lock:

        return {
            "monitoring": monitoring_active,
            "stopping": monitoring_active and stop_event.is_set(),
            "last_analysis": last_analysis
        }
