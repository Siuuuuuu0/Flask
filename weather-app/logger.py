from datetime import datetime
from translations import translations
from time import time


def logger(language, city):
    with open("logs.txt", "a") as f:
        curr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        string = f"Requested city: {city}, in: {translations[language]['full']}, at: {curr}\n"
        f.write(string)

def wrapper (func):
    def time_elapsed(*args, **kwargs):
        with open("logs.txt", "a") as f:
            start = time()
            result = func(*args, **kwargs)
            end = time()
            f.write(f"Request accomplished in: {end - start:.2f} seconds\n")
            return result
    return time_elapsed

if __name__ == "__main__":
    logger()