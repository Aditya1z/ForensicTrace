import os
import hashlib
from datetime import datetime

class FileScanner:
    def __init__(self):
        self.scanned_files = []
        self.file_hashes = {}
        
    def scan_directory(self, directory_path):
        try:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    file_info = self._get_file_info(full_path)
                    if file_info:
                        self.scanned_files.append(file_info)
            return self.scanned_files
        except Exception as e:
            print(f"Error during directory scan: {e}")
            return []

    def _get_file_info(self, file_path):
        try:
            stats = os.stat(file_path)
            return {
                'path': file_path,
                'size': stats.st_size,
                'created': datetime.fromtimestamp(stats.st_ctime),
                'modified': datetime.fromtimestamp(stats.st_mtime),
                'accessed': datetime.fromtimestamp(stats.st_atime),
                'hash': self._calculate_file_hash(file_path)
            }
        except Exception as e:
            print(f"Error retrieving file information: {e}")
            return None

    def _calculate_file_hash(self, file_path):
        try:
            hash_calculator = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_calculator.update(chunk)
            return hash_calculator.hexdigest()
        except Exception as e:
            print(f"Error calculating file hash: {e}")
            return None 