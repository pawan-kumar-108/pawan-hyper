from fastapi import FastAPI, HTTPException
from model.models import Match, Prediction, UserPrediction
from services import predict_match_outcome
from datetime import datetime

app = FastAPI(title="Match Prediction API")

#in memory storage
matches_db = {}
predictions_db = {}

@app.get("/")
async def root():
    return {"message": "Welcome to Match Prediction API"}

@app.post("/matches/")
async def create_match(match: Match):
    matches_db[match.match_id] = match
    return match

@app.get("/matches/{match_id}")
async def get_match(match_id: str):
    if match_id not in matches_db:
        raise HTTPException(status_code=404, detail="Match not found")
    return matches_db[match_id]

@app.post("/predictions/{match_id}")
async def create_prediction(match_id: str, prediction: UserPrediction):
    if match_id not in matches_db:
        raise HTTPException(status_code=404, detail="Match not found")
    
    ml_prediction = predict_match_outcome(matches_db[match_id])
    
    pred_id = f"pred_{len(predictions_db)}"
    full_prediction = Prediction(
        prediction_id=pred_id,
        match_id=match_id,
        user_prediction=prediction.predicted_winner,
        ml_prediction=ml_prediction,
        timestamp=datetime.now()
    )
    predictions_db[pred_id] = full_prediction
    return full_prediction

@app.get("/predictions/{match_id}")
async def get_predictions(match_id: str):
    match_predictions = {k: v for k, v in predictions_db.items() if v.match_id == match_id}
    return match_predictions