import os
import pytest
from src.utils import calculate_percentage_change
from src.tracker import MarketTracker

def test_percentage_calculation():
    assert calculate_percentage_change(100, 110) == 10.0
    assert calculate_percentage_change(200, 150) == -25.0
    assert calculate_percentage_change(0, 50) == 0.0

def test_tracker_database_integration():
    test_db = "data/test_market.db"
    tracker = MarketTracker(db_path=test_db)
    
    result = tracker.track("BTC")
    assert result["ticker"] == "BTC"
    assert result["price"] > 0
    assert "change_percent" in result

    # Cleanup test artifact
    if os.path.exists(test_db):
        os.remove(test_db)
