import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

class Visualizer:
    def __init__(self):
        self.figures = {}

    def plot_timeline(self, files):

        plt.figure(figsize=(12, 6))
        
        modification_dates = [f['modified'] for f in files]
        file_sizes = [f['size'] for f in files]
        plt.scatter(modification_dates, file_sizes, alpha=0.5)
        plt.title('File Modification Timeline')
        plt.xlabel('Date')
        plt.ylabel('File Size (bytes)')
        plt.xticks(rotation=45) 
        plt.tight_layout()       
        plt.show()

    def plot_file_distribution(self, files):
        plt.figure(figsize=(10, 6))
        sizes = [f['size'] for f in files]
        plt.hist(sizes, bins=50)
        plt.title('File Size Distribution')
        plt.xlabel('File Size (bytes)')
        plt.ylabel('Number of Files')
        plt.show()

    def plot_activity_heatmap(self, files):
        plt.figure(figsize=(12, 8))
        hours = [f['modified'].hour for f in files] 
        days = [f['modified'].weekday() for f in files] 
        activity_map, x_edges, y_edges = np.histogram2d(hours, days, bins=[24, 7])
        plt.imshow(activity_map.T, origin='lower', aspect='auto', cmap='YlOrRd')
        plt.colorbar(label='Activity Count')
        plt.title('File Activity Heatmap')
        plt.xlabel('Hour of Day')
        plt.ylabel('Day of Week')
        plt.show()

    def plot_suspicious_activities(self, analysis_results):
        plt.figure(figsize=(10, 6))
        categories = [
            'Recent Activity',
            'Large Files',
            'Frequent Access',
            'Suspicious Patterns'
        ]
        counts = [
            len(analysis_results['recent_activity']),
            len(analysis_results['large_files']),
            len(analysis_results['frequent_access']),
            len(analysis_results['suspicious_patterns'])
        ]
        plt.bar(categories, counts)

        plt.title('Analysis Results Summary')
        plt.xticks(rotation=45) 
        plt.tight_layout()
        plt.show() 