import glob
import os
from dataclasses import dataclass
from pathlib import Path
import shutil

@dataclass
class Deleter:

    def clear_files(self, data_path: Path, type: str = "*.mp4") -> None:
        for filepath in glob.glob(os.path.join(str(data_path), type)):
            os.remove(filepath)

    def clear_directory(self, directory_path: Path) -> None:
        if Path(directory_path).exists():
            shutil.rmtree(directory_path)
