def detect_whales(df, threshold):
    whales = df[df["value"] > threshold]
    return whales
