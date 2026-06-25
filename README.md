Visual layout of the file and directory structure for the Python Market Price Monitor project

trade-market-price-monitor/
├── .github/
│   └── workflows/
│       └── monitor.yml        # CI/CD schedule and test automation pipeline
├── data/
│   └── market.db             # Local SQLite database file (automatically created)
├── src/
│   ├── __init__.py           # Makes 'src' an importable Python package
│   ├── tracker.py            # Primary core data injection and monitoring engine
│   └── utils.py              # Precision math calculations & metric helpers
├── tests/
│   ├── __init__.py           # Makes 'tests' an importable package
│   └── test_tracker.py       # Validation and automated unit test suite
├── .gitignore                # Tells Git which local files to ignore (e.g., databases, caches)
├── README.md                 # Project documentation and developer setup instructions
└── requirements.txt          # File containing external project dependencies (requests, pytest)



# Market Price Monitor (Automated CI/CD) ########################

An automated asset price ingestion engine that saves metrics locally using SQLite and triggers data pipeline runs using scheduled task setups.

## Key Features #########################
- **Data Persistence**: Automatic local historical tracking inside an optimized lightweight SQL structure.
- **Precision Validation**: Core math utilities tested to handle margin shifts and errors smoothly.
- **Scheduled Workflows**: Automated pipeline executions running every day via native GitHub infrastructure.

## Installation & Usage Guide

################Prerequisites ###########################
- Python 3.10 or superior runtime installation

### ###########1. Build Environment Layout ########################
```bash
git clone https://github.com/suhas90/trade-trade-market-price-monitor.git
cd trade-market-price-monitor
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

########### 2. Execute Tests Locally############
Validate the database structure and computational accuracy:
```bash
pytest
```

####### 3. Trigger Price Tracker Run ###############
```bash
python src/tracker.py
```
####################################################