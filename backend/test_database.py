
from app.database import save_activity, get_connection

sample_analysis = {
    "activity_summary": "Studying Java programming",
    "category": "Education",
    "intent_alignment": "aligned",
    "reason": "The visible activity matches the declared intention.",
    "confidence": 0.95
}

save_activity("I am studying Java programming", sample_analysis)

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM activity_history ORDER BY id DESC LIMIT 1")
record = cursor.fetchone()

print("\nLatest database record:")
print(dict(record) if record else "No record found")

connection.close()
