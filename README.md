# ForensicTrace

A professional digital forensics analysis tool designed for comprehensive file system analysis, pattern detection, and evidence visualization. ForensicTrace provides a robust platform for analyzing file system activities, detecting suspicious patterns, and visualizing digital evidence in a clear, actionable format.

## Features

### File System Analysis
- Comprehensive file system scanning
- SHA-256 hash generation for file integrity
- Detailed metadata extraction
- File modification tracking
- Access pattern analysis

### Pattern Detection
- Suspicious activity identification
- Statistical analysis of file modifications
- Access pattern recognition
- Anomaly detection
- Trend analysis

### Visualization
- Interactive activity timeline graphs
- File size distribution analysis
- System activity heatmaps
- Analysis summary reports
- Customizable visualization parameters

## Use Cases

### Digital Forensics
- Evidence collection
- Pattern analysis
- Timeline reconstruction
- Activity tracking

### Security Analysis
- Suspicious activity detection
- Access pattern monitoring
- Anomaly identification
- Security incident investigation

### System Administration
- File system monitoring
- Activity tracking
- Performance analysis
- System health assessment

## Technical Requirements

- Python 3.8 or higher
- Required packages:
  - pandas==2.0.0
  - numpy==1.24.0
  - matplotlib==3.7.0
  - seaborn==0.12.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Aditya1z/ForensicTrace.git
cd ForensicTrace
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python main.py
```

The tool will:
1. Scan the specified directory
2. Analyze file patterns
3. Generate visualizations
4. Provide a comprehensive report

## Output Examples

ForensicTrace generates several types of visualizations:

1. Activity Timeline Graph
   - Shows file modifications over time
   - Displays file size distribution
   - Highlights activity patterns

2. File Size Distribution Graph
   - Illustrates file size patterns
   - Identifies size anomalies
   - Shows storage distribution

3. Activity Heatmap
   - Visualizes system activity patterns
   - Shows temporal distribution
   - Highlights peak activity periods

4. Analysis Summary Graph
   - Provides overview of findings
   - Summarizes key metrics
   - Highlights important patterns

## Visualization Details

### 1. Activity Timeline Graph
- **Type**: Scatter Plot
- **Purpose**: Visualize file modifications over time
- **Components**:
  - X-axis: Timestamp of file modifications
  - Y-axis: File size in bytes
  - Each point represents a file
  - Point size: Constant
  - Point opacity: 0.5 for better visibility of overlapping points
- **Interpretation**:
  - Clusters of points indicate periods of high activity
  - Vertical patterns suggest bulk file operations
  - Outliers in file size are easily identifiable
- **Use Cases**:
  - Identify suspicious modification patterns
  - Track system usage patterns
  - Detect unusual file size changes

### 2. File Size Distribution Graph
- **Type**: Histogram
- **Purpose**: Analyze the distribution of file sizes
- **Components**:
  - X-axis: File size ranges (bins)
  - Y-axis: Number of files in each size range
  - Number of bins: 50 (optimized for visibility)
- **Interpretation**:
  - Normal distribution indicates healthy file system
  - Skewed distribution may indicate storage issues
  - Outliers represent unusually large or small files
- **Use Cases**:
  - Storage capacity planning
  - Identify storage anomalies
  - Monitor file size trends

### 3. Activity Heatmap
- **Type**: 2D Heatmap
- **Purpose**: Visualize system activity patterns
- **Components**:
  - X-axis: Hours of the day (0-23)
  - Y-axis: Days of the week (0-6)
  - Color intensity: Number of file activities
  - Color scheme: Yellow-Orange-Red (YlOrRd)
- **Interpretation**:
  - Brighter colors indicate higher activity
  - Patterns show regular system usage
  - Unusual patterns may indicate security issues
- **Use Cases**:
  - Identify peak usage times
  - Detect unusual activity patterns
  - Monitor system usage patterns

### 4. Analysis Summary Graph
- **Type**: Bar Chart
- **Purpose**: Summarize analysis findings
- **Components**:
  - X-axis: Analysis categories
  - Y-axis: Number of files in each category
  - Categories:
    1. Recent Activity (last 7 days)
    2. Large Files (statistically significant)
    3. Frequent Access (high access count)
    4. Suspicious Patterns (potential security issues)
- **Interpretation**:
  - Bar height indicates number of files
  - Higher bars in suspicious patterns need attention
  - Balanced distribution suggests normal operation
- **Use Cases**:
  - Quick overview of system status
  - Identify areas needing attention
  - Track changes over time

## Graph Customization

### Available Parameters
1. **Activity Timeline**
   - Figure size: 12x6 inches
   - Point opacity: 0.5
   - Date rotation: 45 degrees
   - Automatic date formatting

2. **File Size Distribution**
   - Figure size: 10x6 inches
   - Number of bins: 50
   - Automatic bin sizing
   - Logarithmic scale option

3. **Activity Heatmap**
   - Figure size: 12x8 inches
   - Color scheme: YlOrRd
   - 24x7 grid resolution
   - Automatic color scaling

4. **Analysis Summary**
   - Figure size: 10x6 inches
   - Category rotation: 45 degrees
   - Automatic label positioning
   - Consistent color scheme

### Export Options
- All graphs can be saved as:
  - PNG files
  - PDF documents
  - SVG vector graphics
- Resolution: 300 DPI (default)
- Customizable figure sizes
- Adjustable color schemes

## Project Structure

```
forensictrace/
├── main.py
├── file_scanner.py
├── data_analyzer.py
├── visualizer.py
├── requirements.txt
└── README.md
```

## Module Descriptions

### file_scanner.py
- Handles file system scanning
- Generates file hashes
- Extracts metadata
- Tracks file modifications

### data_analyzer.py
- Performs statistical analysis
- Detects patterns
- Identifies anomalies
- Generates analysis reports

### visualizer.py
- Creates interactive visualizations
- Generates analysis graphs
- Produces activity heatmaps
- Formats data for presentation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For issues and feature requests:
1. Check existing issues
2. Create a new issue
3. Provide detailed information
4. Include relevant logs

## License

This project is licensed under the MIT License - see the LICENSE file for details.