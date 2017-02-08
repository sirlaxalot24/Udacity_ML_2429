

def feature_scaling(arr):
    scaled = []
    min_a = float(min(arr))
    spread = float(max(arr)) - min_a
    for val in arr:
        scaled.append((float(val) - min_a)/spread)
    return scaled


if __name__ == "__main__":
    data = [115, 140, 175]
    print feature_scaling(data)
