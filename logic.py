def calculate_score(d):
    score = 100

    if d["sleep"] < 6:
        score -= 20
    elif d["sleep"] > 8:
        score -= 5

    if d["water"] < 1.5:
        score -= 15

    if d["steps"] < 5000:
        score -= 10

    if d["mood"] <= 2:
        score -= 15

    return max(score, 0)


def get_insight(d):
    if d["sleep"] < 6:
        return "Low sleep is reducing your recovery."
    if d["water"] < 1.5:
        return "Dehydration is affecting your energy."
    if d["mood"] <= 2:
        return "Your mental state needs attention."
    return "You are in a stable condition."


def get_tips(d):
    tips = []

    if d["sleep"] < 6:
        tips.append("• Sleep at least 7 hours")

    if d["water"] < 1.5:
        tips.append("• Drink 2L water")

    if d["steps"] < 5000:
        tips.append("• Walk 15 minutes")

    if d["mood"] <= 2:
        tips.append("• Take mental rest")

    return tips[:3]