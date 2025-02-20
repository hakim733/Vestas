# Wind Turbine Data Analysis Dashboard for vestas 

## Project Overview

This project involves the analysis of wind data from two locations: southwest Glasgow, Scotland, and northeast Galway, Ireland. The data sources consist of LiDAR measurements and Mesoscale model data, both provided in CSV format. The purpose of this project is to explore the relationship between these data sources, perform various data analysis tasks, and build a dashboard that visualizes the results effectively.

## Key Features

- **Data Input**: The dashboard allows users to upload the `.csv` files through a browse button.
- **Data Analysis**: The dashboard processes the data and performs various analytical tasks in the background, presenting results through tables, charts, and other visualizations.
- **Analytics**: The analysis includes exploring relationships between the LiDAR data at different heights and Mesoscale data. Custom analysis techniques were used to reveal insights and patterns.
- **Event Detection**: A tool has been integrated to identify special events in the LiDAR data. This tool cross-references these events with external news sources to validate whether significant occurrences (e.g., storms or unusual weather patterns) align with the data. The results are visualized within the dashboard.

## Data Sources

The project uses two primary types of data:

1. **LiDAR Data**: Laser-based measurements capturing wind speed, wind direction, standard deviation, turbulence, and timestamps at different heights.
2. **Mesoscale Data**: Averaged model data, provided at a 99m height and with a lower resolution (1-hour intervals). This data includes wind speed, wind direction, and timestamps.

## Dashboard Overview

The dashboard provides an interactive interface where users can upload the data files and visualize various analytical results. It includes:

- **File Upload Functionality**: Users can select and upload the CSV files containing the wind data.
- **Data Processing**: Once the files are uploaded, the dashboard performs background analysis such as comparing the LiDAR data at different heights with Mesoscale data.
- **Visual Results**: The results of the analysis are shown as tables and charts to make the findings easily interpretable.
- **Special Event Detection Tool**: The dashboard includes a feature that identifies special events in the LiDAR data, such as high wind speeds or turbulence. It checks these events against online news sources for verification, which is also displayed in the dashboard for the user to review.

## Technologies Used

- **Python**: The backend is built using Python, utilizing libraries such as Pandas for data processing, and Matplotlib for data visualization.
- **Flask**: The dashboard is powered by the Flask web framework, allowing it to run as a local, executable application.
- **JavaScript**: Used for frontend elements and to enhance interactivity within the dashboard.

## Key Tasks Completed

- **Data Analysis**: Implemented and completed analysis comparing LiDAR and Mesoscale data, including investigating the relationship between the two datasets at various heights.
- **Dashboard Development**: Designed and implemented a local dashboard that enables users to upload CSV files, perform data analysis, and view results in visual formats.
- **Event Detection Algorithm**: Developed a tool to detect special events in the LiDAR data and cross-verify these events with external news sources for validation. This feature provides additional insights into the data, particularly when unusual weather events are detected.
  
## Objective

The objective of this project was to develop a practical, user-friendly tool for analyzing wind turbine data and displaying insights in an interactive dashboard. Additionally, the project explored the use of data analysis and creativity in building tools that leverage both statistical analysis and external data sources for event verification.

## Future Improvements

- **Expanded Event Detection**: Enhancing the event detection algorithm to recognize a broader range of weather phenomena.
- **Data Granularity**: Incorporating higher-resolution Mesoscale data or more detailed LiDAR datasets for more precise analyses.
- **User Interface Enhancements**: Improving the design and user experience for easier interaction with the dashboard and its features.


The application will start running locally and can be accessed through your browser.

## Contact Information

For any questions or suggestions regarding this project, feel free to reach out.

## Acknowledgements

This project simulates real-world data analysis tasks in the wind energy sector and aims to provide a hands-on experience with front-end dashboard development, data analysis, and external data integration.

