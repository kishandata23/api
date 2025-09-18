from fastapi import FastAPI
from routers import social, code

app = FastAPI(title="My API Hub")

app.include_router(social.router)
app.include_router(code.router)

@app.get('/api')
async def root():
    return {'API portfolio':"kishandata.in",
            "available_routes": [
            "/x",
            "/instagram",
            "/linkedin",
            "/resume"
        ]
            }
