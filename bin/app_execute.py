import os
import file_reader as fr
import settings

def get_tittle():
    path_file = os.path.join(settings.PATH_FILE, settings.FILE_NAME)
    data = fr.get_data(path_file)
    for url in data:
        print(url.get_tittle())


if __name__ == "__main__":
    get_tittle()
