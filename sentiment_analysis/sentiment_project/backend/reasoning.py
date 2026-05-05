def get_issue(text):
    if "late" in text:
        return "Logistics Issue"
    elif "damaged" in text:
        return "Product Issue"
    else:
        return "General"