from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import social, code

app = FastAPI(title="My API Hub")

app.include_router(social.router)
app.include_router(code.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
