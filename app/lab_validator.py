def validate_lab_results(results):

    alerts = []

    # Critical lab checks

    if results.get("WBC", 0) > 30:
        alerts.append("Critical WBC level")

    if results.get("HGB", 100) < 6:
        alerts.append("Critical Hemoglobin")

    if results.get("K", 0) > 6:
        alerts.append("Critical Potassium")

    if len(alerts) == 0:
        return {
            "status": "NORMAL",
            "alerts": []
        }

    return {
        "status": "ALERT",
        "alerts": alerts
    }
