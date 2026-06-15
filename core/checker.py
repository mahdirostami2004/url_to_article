import requests


def check_scrapeability(url):
    try:
        r = requests.get(url, timeout=5)

        return {
            "ok": r.status_code == 200,
            "status": r.status_code,
            "reason": "OK" if r.status_code == 200 else "Blocked or error"
        }

    except Exception as e:
        return {
            "ok": False,
            "status": None,
            "reason": str(e)
        }