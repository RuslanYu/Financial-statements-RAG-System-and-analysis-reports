# Financial RAG System

## Overview
The Financial RAG System is designed to provide a comprehensive analysis of financial statements using a Red-Amber-Green (RAG) system. This project aims to simplify financial reporting and enhance decision-making by visually representing financial health.

## Features
- Analyze financial statements
- Generate RAG reports
- User-friendly interface
- Customizable thresholds for RAG status

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/RuslanYu/Financial-statments-RAG-System-and-analysis-reports.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Financial-statments-RAG-System-and-analysis-reports
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database** (if applicable) by following the database setup instructions provided in the `DATABASE.md` file.

## Usage Examples
### Basic Analysis
Run the analysis script:
```bash
python analyze.py --input financial_data.csv --output report.pdf
```

### Custom RAG Thresholds
You can customize the RAG thresholds in the configuration file:
```json
{
  "red_threshold": 30,
  "amber_threshold": 70,
  "green_threshold": 100
}
```

### Generating Reports
To generate a report after analysis:
```bash
python generate_report.py --input analysis_results.json --output final_report.pdf
```

## Contributing
Contributions are welcome! Please read the `CONTRIBUTING.md` file for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.