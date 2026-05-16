# 🎮 Super Smash Bros. Ultimate Optimizer

A comprehensive tool for Super Smash Bros. Ultimate players to analyze character matchups and follow structured learning paths from beginner to pro. 

The project features a Streamlit-based web dashboard.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

* **⚔️ Matchup Analyzer:** View detailed advantage, even, and disadvantage spreads for every character, utilizing a scoring system based on competitive matchup charts. Includes a stat radar chart for a quick overview.
* **🛡️ Counterpicker:** Find the best characters to counter an opponent you are struggling against, featuring overlapping radar charts to directly compare stats.
* **📚 Learning Path:** Track your progress through character-specific skills separated by difficulty (Basics, Intermediate, Advanced, Pro).
* **📊 Overall Stats:** A full roster overview showing every character's tier, difficulty, playstyle, and average matchup score.
* **🎖️ Tier List:** Official SSBU Tier List reference.
* **👤 My Roster & 📈 My Progress:** Manage the characters you play and track your learning progress across the roster.
* **📱 Mobile Optimized:** Includes UI and navigation optimizations for proper functionality and a seamless experience on mobile devices.

## Prerequisites

* Python 3.8+
* Pip (Python package manager)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kmist70/ssbu-optimizer
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
* `data/`: Contains the compiled JSON datasets (`characters.json`, `matchups.json`) and user tracking data (`progress.json`, `roster.json`).
* `media/`: Contains the app icon and character portraits.
* `scripts/`: Utility scripts for data gathering and management.
* `requirements.txt`: Python package dependencies.