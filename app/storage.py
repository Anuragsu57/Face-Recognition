import numpy as np
import os

EMBEDDING_DIR = "data/embeddings"


def save_embedding(user_id, embedding):

    path = os.path.join(
        EMBEDDING_DIR,
        f"{user_id}.npy"
    )

    np.save(path, embedding)


def load_embedding(user_id):

    path = os.path.join(
        EMBEDDING_DIR,
        f"{user_id}.npy"
    )

    if not os.path.exists(path):

        return None

    return np.load(path)