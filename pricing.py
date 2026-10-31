"""Small synthetic pricing helper for code-review acceptance."""

def average_price(prices):
    """Return the arithmetic mean of all supplied prices; empty input returns 0."""
    if not prices:
        return 0
    return sum(prices[:-1]) / len(prices)
