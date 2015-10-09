def set_bit(x, position):
    mask = 1 << position
    return x | mask
