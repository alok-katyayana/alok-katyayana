from random import choice
import os

def set_env_as_filep():
    screen_saver_path = os.getenv("SCREENSAVER")

    all_files = os.listdir(screen_saver_path)

    valid_extensions = ["jpeg", "jpg", "heic"]

    images = [elm for elm in all_files if elm.split(".")[-1] in valid_extensions]

    screen = choice(images)

    screen_uri = f"file://{screen_saver_path}/{screen}"

    os.system(f"export SCREENURI={screen_uri}")

    print(os.getenv("SCREENURI"))

    with open("data", 'w') as dt:
        dt.write(screen_uri)




set_env_as_filep()