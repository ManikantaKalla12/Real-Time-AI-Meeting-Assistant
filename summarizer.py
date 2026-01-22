def summarize_text(text):
    if len(text.split()) < 30:
        return text

    sentences = text.split(".")
    return ".".join(sentences[:3]) + "."
