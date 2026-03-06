from fastapi import FastAPI
from app.data_quality_engine import run_quality_check

app = FastAPI(title="Clinical Data Quality Monitor", version="1.0.0")


@app.get("/")
def home():
    return {
        "system": "Clinical Data Quality Monitor",
        "status": "running"
    }


@app.post("/validate")
def validate():

    hl7_message = """
    MSH|^~\\&|LAB|HOSPITAL
    PID|1||12345
    OBR|1
    OBX|1|NM|WBC||35
    """

    lab_results = {
        "WBC": 35,
        "HGB": 5,
        "K": 5.5
    }

    result = run_quality_check(hl7_message, lab_results)

    return result
