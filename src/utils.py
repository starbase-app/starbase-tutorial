def range_sum(start, end):
    """Return the sum of all integers from start to end (inclusive)."""
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

def clamp(value, min_val, max_val):
    """Clamp a value between min_val and max_val."""
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value
