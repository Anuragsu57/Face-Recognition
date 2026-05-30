from deepface import DeepFace
import numpy as np
from numpy.linalg import norm
import tempfile

UPPER_THRESHOLD = 0.85
LOWER_THRESHOLD = 0.60


def get_embedding(image_bytes):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:

        temp.write(image_bytes)

        temp_path = temp.name

    embedding = DeepFace.represent(
        img_path=temp_path,
        model_name="Facenet",
        enforce_detection=False
    )

    return np.array(embedding[0]["embedding"])


def cosine_similarity(a, b):

    return np.dot(a, b) / (norm(a) * norm(b))


def verify_similarity(score):

    if score >= UPPER_THRESHOLD:

        return "PASS"

    elif score < LOWER_THRESHOLD:

        return "FAIL"

    else:

        return "INCONCLUSIVE"