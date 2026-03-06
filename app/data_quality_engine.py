from app.hl7_validator import validate_hl7
from app.lab_validator import validate_lab_results


def run_quality_check(hl7_message, lab_results):

    # Run HL7 validation
    hl7_result = validate_hl7(hl7_message)

    # Run lab result validation
    lab_result = validate_lab_results(lab_results)

    # Start with a perfect score
    quality_score = 100

    # Deduct points if HL7 is invalid
    if hl7_result["status"] == "INVALID":
        quality_score -= 40

    # Deduct points if lab alerts exist
    if lab_result["status"] == "ALERT":
        quality_score -= 30

    return {
        "hl7_validation": hl7_result,
        "lab_validation": lab_result,
        "data_quality_score": quality_score
    }
