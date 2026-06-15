import json
import csv
import sqlite3


def export_json(data):
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def export_csv(data):
    if not data:
        return

    keys = data[0].keys()

    with open("output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def export_sqlite(data):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS data (
        url TEXT,
        title TEXT,
        text TEXT,
        links TEXT
    )
    """)

    for d in data:
        cur.execute(
            "INSERT INTO data VALUES (?, ?, ?, ?)",
            (
                d.get("url"),
                d.get("title"),
                d.get("text"),
                str(d.get("links"))
            )
        )

    conn.commit()
    conn.close()