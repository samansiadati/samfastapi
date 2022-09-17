from fastapi import FastAPI
import uvicorn


app = FastAPI(title="The Sam API reporting",
    description=(
        "The various APIs will be used to trigger data extractions from various services. "
    ),
    # root_path=settings.ROOT_PATH,
    root_path="/src/",
)

@app.get("/")
def hello():
    return {"message":"Hello Saman"}
