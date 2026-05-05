def get_intent(text):
    if "bad" in text:
        return "Complaint"
    elif "good" in text:
        return "Praise"
    else:
        return "Neutral"