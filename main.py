import os
from file_scanner import FileScanner
from data_analyzer import DataAnalyzer
from visualizer import Visualizer

def main():
    print("ForensicTrace (GitHub - Aditya1z)")
    print("A Digital Forensics Analysis Tool\n")
    
    scanner = FileScanner()
    analyzer = DataAnalyzer()
    visualizer = Visualizer()
    
    print("Which directory would you like to analyze?")
    print("(Leave blank to scan the current directory)")
    target_dir = input("> ").strip()
    
    if not target_dir:
        target_dir = os.getcwd()
        print(f"\nOkay, analyzing the current directory: {target_dir}")
    
    print("\nStarting the scan...")
    found_files = scanner.scan_directory(target_dir)
    
    if not found_files:
        print("\nCould not find any files in that directory. Please check the path.")
        return
        
    print(f"\nScan finished. Found {len(found_files)} files.")
    
    print("\nAnalyzing files for patterns...")
    analysis_results = analyzer.analyze_file_patterns(found_files)
    
    print("\nHere's a summary of the analysis:")
    print(f"- Found {len(analysis_results['recent_activity'])} recently modified files.")
    print(f"- Found {len(analysis_results['large_files'])} unusually large files.")
    print(f"- Found {len(analysis_results['frequent_access'])} frequently accessed files.")
    print(f"- Found {len(analysis_results['suspicious_patterns'])} potentially suspicious files.")
    
    print("\nGenerating visualizations...")
    print("(Charts will open in new windows)\n")
    
    print("1. Plotting file activity timeline...")
    visualizer.plot_timeline(found_files)
    
    print("2. Plotting file size distribution...")
    visualizer.plot_file_distribution(found_files)
    
    print("3. Plotting activity heatmap...")
    visualizer.plot_activity_heatmap(found_files)
    
    print("4. Plotting summary of findings...")
    visualizer.plot_suspicious_activities(analysis_results)
    
    print("\nAnalysis complete. Visualizations have been generated.")

if __name__ == "__main__":
    main() 