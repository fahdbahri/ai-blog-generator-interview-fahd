import random

def fetch_seo_data(keyword):
    mock_data = {
        "wireless earbuds": {"search_volume": 15000, "keyword_difficulty": 45, "avg_cpc": 2.50},
        "bluetooth headphones": {"search_volume": 12000, "keyword_difficulty": 50, "avg_cpc": 3.00}
    }
    return mock_data.get(keyword, {
        "search_volume": random.randint(1000, 20000),
        "keyword_difficulty": random.randint(10, 80),
        "avg_cpc": round(random.uniform(0.5, 5.0), 2)
    })