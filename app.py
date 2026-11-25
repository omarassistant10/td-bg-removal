from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session

app = FastAPI()
session = new_session("u2net")

@app.get("/")
def health():
    return {"ok": True, "model": "u2net"}

@app.post("/remove")
async def remove_bg(image: UploadFile = File(...)):
    data = await image.read()
    out = remove(data, session=session)
    return Response(content=out, media_type="image/png")
