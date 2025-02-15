# Match Prediction API

This is a fun system where users can predict sports match outcomes and compete against our ML model's predictions.

This API lets us:

- Record matches and their details
- Make your own predictions
- Get predictions from our ML model
- Track how good your predictions are compared to the AI

#  Match Prediction API

A FastAPI-based sports match prediction system that combines user predictions with machine learning insights. Compare your match predictions against AI-generated forecasts!

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


##  Features

- 🏏 Create and manage sports matches
- 🤖 Get AI-powered match predictions
- 👥 Submit and track user predictions
- 📊 Compare prediction accuracy
- 🔄 Real-time updates via FastAPI

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/match-prediction-api.git
   cd match-prediction-api
   ```

2. **Set up the environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```


5. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - API Endpoints: http://localhost:8000/api/v1/

## API Endpoints

### Create a Match
```http
POST /matches
```
```json
{
    "match_id": "M1",
    "team1": {
        "team_id": "CSK",
        "name": "Chennai Super Kings",
        "recent_form": 0.8
    },
    "team2": {
        "team_id": "MI",
        "name": "Mumbai Indians",
        "recent_form": 0.7
    },
    "match_date": "2024-02-13T14:00:00",
    "venue": "Chennai"
}
```

### Make a Prediction
```http
POST /predictions/{match_id}
```
```json
{
    "predicted_winner": "CSK"
}
```


## 🛠 Technical Details

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **ML Integration**: Modular design for easy ML model integration



<div align="center">


</div>
