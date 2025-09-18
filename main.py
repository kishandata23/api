from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from datetime import datetime, timedelta
import uvicorn


app = FastAPI()

origins = [
    "http://localhost:3000"
]
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

G_EXCEL_CSV_URL = 'https://docs.google.com/spreadsheets/d/1jWR62AXQeg6md4ATca-w2T82zZ88Mr1c5HcWty2vX3Y/export?format=csv'


def read_excel_data():
    # df = pd.read_excel(BytesIO(response.content))
    df = pd.read_csv(G_EXCEL_CSV_URL)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

@app.get("/api/code/problems/{date}")
async def get_problems_by_date(date: str):
    df = read_excel_data()
    selected_date = pd.to_datetime(date)
    daily_problems = df[df['Date'].dt.date == selected_date.date()]
    return daily_problems.to_dict('records')

@app.get("/api/code/recent-submissions")
async def get_recent_submissions():
    df = read_excel_data()
    last_7_days = datetime.now() - timedelta(days=7)
    recent = df[df['Date'] >= last_7_days]
    return recent.to_dict('records')

@app.get("/api/code/problem-stats")
async def get_problem_stats():
    df = read_excel_data()
    stats = {
        "total": len(df)-1,
        "easy": len(df[df['Difficult'] == 'Easy']),
        "medium": len(df[df['Difficult'] == 'Medium']),
        "hard": len(df[df['Difficult'] == 'Hard'])
    }
    return stats

@app.get("/api/code/heatmap-data")
async def get_heatmap_data():
    df = read_excel_data()
    daily_counts = df.groupby(df['Date'].dt.date).size().to_dict()
    return daily_counts


@app.get('/api')
async def root():
    return {'API portfolio':"kishandata.in"}

@app.get('/api/code')
async def root():
    return {'API for project CODE':"kishandata.in/code"}

# local testing
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)