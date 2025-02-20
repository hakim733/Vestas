# Wind Turbine Data Analysis Dashboard

## Project Overview

This project involves analyzing wind data from two locations: one from southwest Glasgow, Scotland, and one from northeast Galway, Ireland. The data is provided in CSV format, with two types of data sources:

- **LiDAR Data**: A laser-based measurement device used to gather wind data at multiple heights.
- **Mesoscale Data**: An averaged, low-resolution wind model data at 99m height.

The goal is to explore the relationship between the LiDAR and Mesoscale data, perform data analysis, and create a dashboard that visualizes the results.

## Key Features

- **Data Input**: The dashboard allows you to input the `.csv` files via a browse button.
- **Data Analysis**: The dashboard processes the data in the background and displays the results in visual forms (tables, charts, etc.).
- **Analytics**: Analyze the relationship between the LiDAR data at various heights and the Mesoscale data. You can use your analytical creativity to perform additional exploratory analysis.
- **Event Identification (Bonus)**: Optionally, write an algorithm to identify special events from the LiDAR data, cross-referencing them with external news sources to validate the event. This feature can be visualized within the dashboard.

## Data Sources

The project includes two CSV files, one for each data source:

1. **LiDAR Data**: Includes timestamps, wind speed, wind direction, standard deviation, and turbulence, measured at various heights.
2. **Mesoscale Data**: Includes timestamps, wind speed, and wind direction, but only at a 99m height and with lower resolution (1-hour intervals).

## Dashboard Requirements

- **File Upload**: The dashboard must allow the user to upload the `.csv` files.
- **Analysis**: Perform analysis of the data (e.g., comparing LiDAR and Mesoscale data, analyzing LiDAR data at different heights).
- **Visualizations**: Display the results of the analysis in the form of tables and/or charts.
- **Local Hosting**: The dashboard does not need to be hosted on a server and should be executable on the local machine.

## Technical Details

- **Programming Languages**: Python, JavaScript (optional for frontend), or any other suitable tools for creating the dashboard.
- **Data Handling**: Use Python libraries such as Pandas for data manipulation and Matplotlib for visualization.
- **Frameworks**: Flask or similar frameworks for creating the local dashboard if using Python.
  
## Objective

- To explore front-end development for wind turbine data analysis.
- To apply traditional statistical or simple analytical methods for wind analysis.
- To explore and apply creativity in the use of tools and techniques to solve problems.

## Bonus Credits

If you complete the above tasks and have time, you can implement a feature to detect special events in the LiDAR data, verify them by checking news or other online sources, and display the results in the dashboard.

## Timeline

- **Deadline**: All tasks must be completed by **19th February**.
- **Presentation**: The results should be presented in the form of a PowerPoint presentation or via a live demo of the executable dashboard.

## Contact Information

For any doubts or questions regarding this project, feel free to reach out via email.

## Acknowledgements

This project is designed to simulate real-world data analysis tasks in the wind energy sector and aims to provide hands-on experience with wind analysis tools and front-end dashboard development.
