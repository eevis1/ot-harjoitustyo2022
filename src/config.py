
import os
"""from dotenv import load_dotenv"""

dirname = os.path.dirname(__file__)

"""try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass"""

COURSES_FILENAME = os.getenv("COURSES_FILENAME") or "courses.csv"
COURSES_FILE_PATH = os.path.join(dirname, "..", "data", COURSES_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
