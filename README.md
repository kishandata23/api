    uv init <project-name>

create virtual env.

    uv run main.py 

select virtual env. 
- windows : .\.venv\Scripts\activate

.

    uv add fastapi uvicorn

run

    uv run main.py

build to export as .tar.gz files
    
    uv build


for vercel: pyproject.toml dependencies are not considered defaultly so create  requirements.txt

    pip freeze > requirements.txt