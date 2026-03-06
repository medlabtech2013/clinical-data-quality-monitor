def validate_hl7(message):

    errors = []

    # Check required HL7 segments

    if "MSH" not in message:
        errors.append("Missing MSH segment")

    if "PID" not in message:
        errors.append("Missing PID segment")

    if "OBR" not in message:
        errors.append("Missing OBR segment")

    if "OBX" not in message:
        errors.append("Missing OBX segment")

    # If no issues found
    if len(errors) == 0:
        return {
            "status": "VALID",
            "errors": []
        }

    return {
        "status": "INVALID",
        "errors": errors
    }
