from fastapi import FastAPI, UploadFile, File, Form
from app.services import *
from app.storage import *

import json
from datetime import datetime

app = FastAPI()


def log_activity(data):

    with open("data/activity_log.jsonl", "a") as f:

        f.write(json.dumps(data) + "\n")


@app.post("/enroll_face")
async def enroll_face(

    user_id: str = Form(...),
    image: UploadFile = File(...)

):

    image_bytes = await image.read()

    embedding = get_embedding(image_bytes)

    save_embedding(user_id, embedding)

    log_activity({
        "timestamp": str(datetime.now()),
        "event": "ENROLL",
        "user_id": user_id
    })

    return {
        "message": "Face enrolled successfully"
    }


@app.post("/verify_face")
async def verify_face(

    user_id: str = Form(...),
    image: UploadFile = File(...)

):

    stored_embedding = load_embedding(user_id)

    if stored_embedding is None:

        return {
            "error": "User not found"
        }

    image_bytes = await image.read()

    new_embedding = get_embedding(image_bytes)

    score = cosine_similarity(
        stored_embedding,
        new_embedding
    )

    decision = verify_similarity(score)

    log_activity({
        "timestamp": str(datetime.now()),
        "event": "VERIFY",
        "user_id": user_id,
        "score": float(score),
        "decision": decision
    })

    return {
        "score": float(score),
        "decision": decision
    }
import os


@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: str):

    path = f"data/embeddings/{user_id}.npy"

    if os.path.exists(path):

        os.remove(path)

        return {
            "message": f"{user_id} deleted successfully"
        }

    return {
        "error": "User not found"
    }