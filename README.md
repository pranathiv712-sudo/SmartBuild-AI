# SmartBuild AI — Smart Building Energy Optimization

## Project Overview
SmartBuild AI is a Python-based prototype that demonstrates how an intelligent agent can analyze simulated building sensor readings and recommend actions to improve energy efficiency and occupant comfort.

## Features
- Interactive building sensor dashboard
- Temperature and occupancy monitoring
- Energy consumption alerts
- Rule-based agent decision-making
- Explainable maintenance and optimization recommendations
- Energy monitoring chart
- Illustrative energy optimization score
- Assessment history with CSV export

## Technologies Used
- Python
- Streamlit
- Pandas

## How It Works
1. Observe: collect the current simulated sensor readings.
2. Evaluate: compare the readings with comfort and energy thresholds.
3. Decide: select suitable recommendations.
4. Explain: display the reasons behind each recommendation.
5. Record: save assessments for later review.

## Run the Project
Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the dashboard:

```bash
python -m streamlit run app.py
```

## Limitations
This is an educational prototype using simulated data and transparent rule-based decision logic. The optimization score is illustrative, not a measured energy-saving percentage. The application does not control real building equipment.

## Future Improvements
- Integrate real sensor data in a safe test environment.
- Add historical trend analysis and anomaly detection.
- Evaluate energy consumption against a defined baseline.
- Add human approval before any real-world control action.

## Author
Student project — Smart Building Automation and Agentic AI Concepts.