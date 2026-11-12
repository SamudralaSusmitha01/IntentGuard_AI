
import sqlite3
from pathlib import Path

# Database file location
DATABASE_PATH = Path(__file__).resolve().parent.parent / "intentguard.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    # Return rows as dictionary-like objects
    connection.row_factory = sqlite3.Row

    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intention TEXT NOT NULL,
            activity_summary TEXT NOT NULL,
            category TEXT NOT NULL,
            intent_alignment TEXT NOT NULL,
            reason TEXT NOT NULL,
            confidence REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

    print("IntentGuard database initialized successfully!")


def save_activity(intention, analysis):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO activity_history (
            intention,
            activity_summary,
            category,
            intent_alignment,
            reason,
            confidence
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        intention,
        analysis["activity_summary"],
        analysis["category"],
        analysis["intent_alignment"],
        analysis["reason"],
        analysis["confidence"]
    ))

    connection.commit()
    connection.close()

    print("Activity saved successfully!")

def get_activity_history(limit=50):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM activity_history
            ORDER BY timestamp DESC, id DESC
            LIMIT ?
        """, (limit,))

        records = cursor.fetchall()

        return [dict(record) for record in records]

    finally:
        connection.close()
