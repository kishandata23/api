from fastapi import APIRouter
import pandas as pd
from datetime import datetime, timedelta
import uvicorn


router = APIRouter(prefix="/api/code", tags=["Code Projects"])


G_EXCEL_CSV_URL = 'https://docs.google.com/spreadsheets/d/1jWR62AXQeg6md4ATca-w2T82zZ88Mr1c5HcWty2vX3Y/export?format=csv'

@router.get('')
async def root():
    return {
        "message": "Welcome to the Project CODE API",
        "base_url": "www.kishandata.in/api/code",
        "status": "running"
            }

@router.get("/data")
def read_excel_data():
    df = pd.read_csv(G_EXCEL_CSV_URL)
    return df.to_dict('records')

@router.get("/problems/{date}")
async def get_problems_by_date(date: str):
    df = read_excel_data()
    selected_date = pd.to_datetime(date)
    daily_problems = df[df['Date'].dt.date == selected_date.date()]
    return daily_problems.to_dict('records')

@router.get("/recent-submissions")
async def get_recent_submissions():
    df = read_excel_data()
    last_7_days = datetime.now() - timedelta(days=7)
    recent = df[df['Date'] >= last_7_days]
    return recent.to_dict('records')

@router.get("/problem-stats")
async def get_problem_stats():
    df = read_excel_data()
    stats = {
        "total": len(df)-1,
        "easy": len(df[df['Difficult'] == 'Easy']),
        "medium": len(df[df['Difficult'] == 'Medium']),
        "hard": len(df[df['Difficult'] == 'Hard'])
    }
    return stats

@router.get("/heatmap-data")
async def get_heatmap_data():
    df = read_excel_data()
    daily_counts = df.groupby(df['Date'].dt.date).size().to_dict()
    return daily_counts
