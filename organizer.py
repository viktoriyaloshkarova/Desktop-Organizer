import os
from pathlib import Path

DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".gif", ".bmp", ".png", ".psd", ".heic"],
    "Videos": [".mov", ".mp4", ".webm", ".mng", ".mpg", ".mpeg"],
    "Documents": [".doc", ".docx", ".fdf", ".dox"],
    "PDF": [".pdf"]
}

FILE_FORMATS = {
    file_format: directory
    for directory, file_formats in DIRECTORIES.items()
    for file_name in file_formats
}

def organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass

if __name__ == "__main__":
    organizer()