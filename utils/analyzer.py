from textblob import TextBlob

def analyze_data(data):
    insights = {
        "total_profiles": len(data),
        "average_followers": sum([p['followers'] for p in data]) / len(data),
        "sentiment_scores": []
    }

    for profile in data:
        text = profile.get("bio", "")
        sentiment = TextBlob(text).sentiment.polarity
        insights["sentiment_scores"].append({
            "username": profile["username"],
            "sentiment": sentiment
        })

    return insights
