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
