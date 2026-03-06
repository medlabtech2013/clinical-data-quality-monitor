def parse_hl7(message):

    segments = message.strip().split("\n")

    parsed = {}

    for segment in segments:

        fields = segment.split("|")

        seg_type = fields[0]

        parsed[seg_type] = fields

    return parsed


def validate_hl7(message):

    parsed = parse_hl7(message)

    errors = []

    required_segments = ["MSH", "PID", "OBR", "OBX"]

    for seg in required_segments:

        if seg not in parsed:
            errors.append(f"Missing {seg} segment")

    if len(errors) == 0:
        return {
            "status": "VALID",
            "errors": [],
            "segments_detected": list(parsed.keys())
        }

    return {
        "status": "INVALID",
        "errors": errors
    }
