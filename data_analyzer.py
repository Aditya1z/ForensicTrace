import numpy as np
from datetime import datetime, timedelta
import os

class DataAnalyzer:
    def __init__(self):
        self.analysis_results = {}
        self.anomalies = []

    def analyze_file_patterns(self, files):
        analysis_results = {
            'recent_activity': self._find_recent_activity(files),
            'large_files': self._find_large_files(files),
            'frequent_access': self._find_frequent_access(files),
            'suspicious_patterns': self._find_suspicious_patterns(files)
        }
        self.analysis_results = analysis_results
        return analysis_results

    def _find_recent_activity(self, files):
        last_week = datetime.now() - timedelta(days=7)
        return [f for f in files if f['modified'] > last_week]

    def _find_large_files(self, files):
        sizes = [f['size'] for f in files]
        mean_size = np.mean(sizes)
        std_size = np.std(sizes)
        return [f for f in files if f['size'] > mean_size + 2*std_size]

    def _find_frequent_access(self, files):
        access_count = {}
        for file in files:
            path = file['path']
            if path in access_count:
                access_count[path] += 1
            else:
                access_count[path] = 1
        return [f for f in files if access_count[f['path']] > 10]

    def _find_suspicious_patterns(self, files):
        suspicious_files = []
        for file in files:
            if os.path.basename(file['path']).startswith('.'):
                suspicious_files.append(file)
            if file['path'].endswith(('.exe', '.bat', '.sh')):
                suspicious_files.append(file)
        return suspicious_files 