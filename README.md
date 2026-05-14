# 🎮 Super Smash Bros. Ultimate Optimizer

A comprehensive tool for Super Smash Bros. Ultimate players to analyze character matchups and follow structured learning paths from beginner to pro. 

The project features a Streamlit-based web dashboard.

## Features

* **⚔️ Matchup Analyzer:** View detailed advantage, even, and disadvantage spreads for every character, utilizing a scoring system based on competitive matchup charts.
* **📚 Learning Path:** Track your progress through character-specific skills separated by difficulty (Basics, Intermediate, Advanced, Pro).

## Prerequisites

* Python 3.8+
* Pip (Python package manager)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd ssbu-optimizer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Dashboard
Launch the Streamlit app to view matchups and track your learning paths:
```bash
streamlit run app.py
```

## Project Structure

* `app.py`: The main Streamlit web application.
* `data/`: Contains the compiled JSON datasets (`characters.json`, `matchups.json`).
* `scripts/`: Utility scripts for data gathering and management.
  * `scrape_data.py`: Playwright scraper for pulling game data.
  * `reorder_matchups.py`: Script to maintain consistent character sorting across JSON files.
* `requirements.txt`: Python package dependencies.