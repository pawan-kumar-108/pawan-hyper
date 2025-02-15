from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Team(BaseModel):
    team_id: str
    name: str
    recent_form: Optional[float] = None  # Win rate in last fewmatches

class Match(BaseModel):
    match_id: str
    team1: Team
    team2: Team
    match_date: datetime
    venue: str
    match_type: str = "T20"  #Default is T20

class UserPrediction(BaseModel):
    predicted_winner: str  # Team id of predicted winner

class Prediction(BaseModel):
    prediction_id: str
    match_id: str
    user_prediction: str
    ml_prediction: dict  
    timestamp: datetime