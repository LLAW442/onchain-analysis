from src.ingestion.fetch_blocks import fetch_latest_block
from src.processing.clean_transactions import clean_transactions
from src.analytics.whale_detection import detect_whales
from src.utils.config import load_config

def run():
    config = load_config()

    txs = fetch_latest_block()
    df = clean_transactions(txs)

    whales = detect_whales(df, config["thresholds"]["whale_eth"])

    print("🐋 Whale transactions:")
    print(whales.head())

if __name__ == "__main__":
    run()
