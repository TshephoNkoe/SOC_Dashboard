# SOC Dashboard 🛡️📊

Access the most Updated Version on this URL : https://drive.google.com/drive/folders/1uGZEjLNVrKZl-1wR45b_dCRzWS_dSw2W?usp=drive_link

**A Python-based Security Operations Center Dashboard for real-time monitoring, log analysis, and incident management**

![Dashboard Preview](background.png) <!-- Use your actual screenshot -->

## Features

### Core Modules
- **Network Monitoring** (`network.py`)  
  Real-time network traffic analysis and visualization
- **System Monitoring** (`monitoring.py`)  
  Host resource tracking (CPU, memory, disk usage)
- **Log Management** (`logs_window.py`)  
  Centralized log viewer with filtering capabilities
- **Incident Management** (`incidents_window.py`)  
  Case tracking and investigation workflows
- **Compliance Reporting** (`compliance_window.py`)  
  Pre-built templates for regulatory standards
- **Splunk Integration** (`splunk_features_window.py`)  
  SIEM data visualization and query interface

### Technical Specifications
- **Database**: SQLite (`database.db`) for persistent storage
- **Data Visualization**: Custom graphing utilities (`graphing.py`)
- **UI Framework**: Tkinter-based interface
- **Log Storage**: Rotating log files in `logs/` directory

## Installation

### Prerequisites
- Python 3.8+
- Tkinter (usually included with Python)
- Required packages:
  ```bash
  pip install matplotlib numpy python-dateutil

## Clone repository:
  git clone https://github.com/TshephoNkoe/SOC_Dashboard.git
cd SOC_Dashboard


## Create a Virtual Environment 
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

## Install dependencies:
pip install -r requirements.txt  # Create this file with your dependencies

## Usage
python main.py

## Key Interface Elements:

Left Navigation: Module selection

Central Dashboard: Data visualization

Bottom Panel: System alerts and notifications

## Project Structure

.
├── venv/                 # Python virtual environment
├── logs/                 # System and application logs
├── __pycache__/          # Python bytecode cache
├── database.db           # SQLite database storage
├── database.py           # Database interaction logic
├── main.py               # Main application entry point
├── network.py            # Network monitoring module
├── monitoring.py         # System health monitoring
├── incidents_window.py   # Incident management UI
├── compliance_window.py  # Compliance reporting
└── graphing.py           # Data visualization utilities

## Development
## Enable virtual environment
source venv/bin/activate

## Modify components:

Add new features to respective modules

Update database schema in database.py

## Test changes:
python -m unittest discover  # Create tests as needed

License
MIT License - see LICENSE file for details

Note: Replace background.png with an actual screenshot of your dashboard in action. Consider adding:

Configuration instructions for network monitoring

Screenshots of different modules

Alert workflow diagrams

Compliance standard documentation


To create the `requirements.txt` file:
```bash
pip freeze > requirements.txt

This README template provides:

Clear feature breakdown

Installation/usage instructions

Project structure overview

Development guidelines

Expandable sections for future enhancements


