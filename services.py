import random
from model.models import Match

def predict_match_outcome(match: Match) -> dict:
    
    #generating random probabilities for demo purposes
    team1_prob = random.uniform(0.3, 0.7)
    team2_prob = 1 - team1_prob
    
    return {
        match.team1.team_id: round(team1_prob, 3),
        match.team2.team_id: round(team2_prob, 3)
    }
