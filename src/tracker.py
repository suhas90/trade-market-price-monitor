import sqlite3
import requests
from src.utils import calculate_percentage_change

class MarketTracker:
    def __init__(self, db_path="data/market.db"):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker TEXT NOT NULL,
                    price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def fetch_mock_price(self, ticker: str) -> float:
        """Simulates external API data extraction for tracking assets."""
        # Hardcoded fallbacks to keep execution predictable and stable
        mock_data = {"BTC": 92500.00, "ETH": 3100.00, "AAPL": 240.50}
        return mock_data.get(ticker.upper(), 0.0)

    def track(self, ticker: str) -> dict:
        current_price = self.fetch_mock_price(ticker)
        if current_price <= 0:
            return {"status": "error", "message": "Invalid Ticker"}

        # Get the previous closing metric
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT price FROM prices WHERE ticker = ? ORDER BY id DESC LIMIT 1", 
                (ticker,)
            )
            row = cursor.fetchone()
            last_price = row[0] if row else current_price

            # Save the active asset update
            cursor.execute(
                "INSERT INTO prices (ticker, price) VALUES (?, ?)", 
                (ticker, current_price)
            )
            conn.commit()

        change = calculate_percentage_change(last_price, current_price)
        return {"ticker": ticker, "price": current_price, "change_percent": change}

if __name__ == "__main__":
    import os
    os.makedirs("data", exist_ok=True)
    tracker = MarketTracker()
    for token in ["BTC", "ETH"]:
        result = tracker.track(token)
        print(f"Asset: {result['ticker']} | Price: ${result['price']} | Change: {result['change_percent']}%")
