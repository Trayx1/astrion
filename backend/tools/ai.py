def summarize_text(text):
    if not text:
        return {"error": "Text is required"}, 400

    try:
        # Dummy-Summarizer: Nimmt die ersten 20 Wörter des Textes
        words = text.split()
        summary = " ".join(words[:20]) + ("..." if len(words) > 20 else "")
        return {"original_text": text, "summary": summary}, 200

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500
    
def analyze_sentiment(text):
    if not text:
        return {"error": "Text is required"}, 400

    try:
        # Simple Sentiment Analysis (Dummy)
        positive_words = ["good", "happy", "great", "excellent", "positive", "love"]
        negative_words = ["bad", "sad", "terrible", "awful", "negative", "hate"]

        sentiment = "neutral"
        for word in positive_words:
            if word in text.lower():
                sentiment = "positive"
                break
        for word in negative_words:
            if word in text.lower():
                sentiment = "negative"
                break

        return {"text": text, "sentiment": sentiment}, 200

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500

