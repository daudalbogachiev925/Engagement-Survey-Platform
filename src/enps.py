def compute_enps(scores):
    """scores: 0-10"""
    promoters = sum(1 for s in scores if s >= 9)
    detractors = sum(1 for s in scores if s <= 6)
    total = len(scores)
    if total == 0:
        return 0
    return round((promoters - detractors) / total * 100, 1)

def categorize(scores):
    return {
        "promoters": sum(1 for s in scores if s >= 9),
        "passives": sum(1 for s in scores if 7 <= s <= 8),
        "detractors": sum(1 for s in scores if s <= 6),
    }
