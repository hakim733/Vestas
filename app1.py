import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats as stats

# ------------------------------------------------------------------------------
# Set page configuration
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Analytics Suite", layout="wide", initial_sidebar_state="expanded")

# ------------------------------------------------------------------------------
# Custom CSS for modern styling
# ------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Overall page background and text styling */
    .stApp {
        background-color: #f7f8f9;
    }

    h1 {
        color: #1D3557;
        font-family: 'Roboto', sans-serif;
        font-size: 3rem;
        text-align: center;
    }
    h2, h3 {
        color: #457B9D;
        font-family: 'Roboto', sans-serif;
        font-weight: bold;
    }

    /* Rubric headers with improved design */
    .rubric-header {
        background-color: #457B9D;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-size: 1.8rem;
        font-weight: bold;
        padding: 1.2rem 2rem;
        border-radius: 8px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }

    /* Align Mesoscale and LiDAR sections symmetrically horizontally */
    .upload-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 2rem;
    }
    .upload-section > div {
        width: 48%;
    }

    /* Button and input styling */
    .stButton button {
        background-color: #1D3557;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 10px;
        padding: 14px 26px;
        transition: all 0.3s ease-in-out;
    }
    .stButton button:hover {
        background-color: #457B9D;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# Page Header: Banner, Title, and Logo
# ------------------------------------------------------------------------------
st.image("https://vestas.scene7.com/is/image/vestas/Offshore_header_1600x570_option3?qlt=85&wid=1600&ts=1648456975506&dpr=off", use_container_width=True)
st.title("Analytics Suite")
st.image("https://upload.wikimedia.org/wikipedia/commons/6/66/Vestas.svg", width=150, caption="", use_container_width=False)

# ------------------------------------------------------------------------------
# MESOSCALE DATA ANALYSIS
# ------------------------------------------------------------------------------
st.markdown('<div class="rubric-header">Mesoscale Data </div>', unsafe_allow_html=True)

# Styled file uploaders for Mesoscale data (horizontal layout)
col1, col2 = st.columns([1, 1])
with col1:
    scotland_meso_file = st.file_uploader("Scotland  ", type=["csv"], key="scotland_meso")
with col2:
    ireland_meso_file = st.file_uploader("Ireland  ", type=["csv"], key="ireland_meso")

if scotland_meso_file and ireland_meso_file:
    # Load CSV data
    df_scotland_meso = pd.read_csv(scotland_meso_file, header=0)
    df_ireland_meso = pd.read_csv(ireland_meso_file, header=0)

    # Data Previews
    st.subheader("Data Previews")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Scotland Mesoscale Data**")
        st.dataframe(df_scotland_meso.head())
    with col2:
        st.write("**Ireland Mesoscale Data**")
        st.dataframe(df_ireland_meso.head())

    # Descriptive Statistics
    st.subheader("Descriptive Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Scotland**")
        st.dataframe(df_scotland_meso.describe())
    with col2:
        st.write("**Ireland**")
        st.dataframe(df_ireland_meso.describe())

    # Comparative Histograms for Wind Speed and Direction
    st.subheader("Comparative Distributions")
    if "wsp_99.0" in df_scotland_meso.columns and "wsp_99.0" in df_ireland_meso.columns:
        fig_wsp = go.Figure()
        fig_wsp.add_trace(go.Histogram(x=df_scotland_meso["wsp_99.0"], name="Scotland", opacity=0.7, marker_color="blue"))
        fig_wsp.add_trace(go.Histogram(x=df_ireland_meso["wsp_99.0"], name="Ireland", opacity=0.7, marker_color="green"))
        fig_wsp.update_layout(barmode="overlay", title="Wind Speed (wsp_99.0) Distribution")
        st.plotly_chart(fig_wsp, use_container_width=True)

    if "wdir_99.0" in df_scotland_meso.columns and "wdir_99.0" in df_ireland_meso.columns:
        fig_wdir = go.Figure()
        fig_wdir.add_trace(go.Histogram(x=df_scotland_meso["wdir_99.0"], name="Scotland", opacity=0.7, marker_color="blue"))
        fig_wdir.add_trace(go.Histogram(x=df_ireland_meso["wdir_99.0"], name="Ireland", opacity=0.7, marker_color="green"))
        fig_wdir.update_layout(barmode="overlay", title="Wind Direction (wdir_99.0) Distribution")
        st.plotly_chart(fig_wdir, use_container_width=True)

    # Statistical Comparison (KS test and T-test)
    st.subheader("Statistical Comparison (Scotland vs Ireland)")

    def compare_distributions(df1, df2, name1, name2):
        results = []
        for col in df1.select_dtypes(include="number").columns:
            if col not in df2.columns:
                continue
            series1 = df1[col].dropna()
            series2 = df2[col].dropna()
            if len(series1) == 0 or len(series2) == 0:
                continue
            ks_stat, ks_p = stats.ks_2samp(series1, series2)
            t_stat, t_p = stats.ttest_ind(series1, series2, equal_var=False)
            results.append({
                "Variable": col,
                f"{name1} Mean": series1.mean(),
                f"{name1} Std": series1.std(),
                f"{name2} Mean": series2.mean(),
                f"{name2} Std": series2.std(),
                "KS Statistic": ks_stat,
                "KS P-Value": ks_p,
                "T-Test Statistic": t_stat,
                "T-Test P-Value": t_p
            })
        return pd.DataFrame(results)
    
    comparison_df = compare_distributions(df_scotland_meso, df_ireland_meso, "Scotland", "Ireland")
    st.dataframe(comparison_df)

    # Mean Comparison Bar Chart
    st.subheader("Mean Comparison")
    if not comparison_df.empty and "Variable" in comparison_df.columns:
        var_values = comparison_df["Variable"].values
        if "wsp_99.0" in var_values and "wdir_99.0" in var_values:
            wsp_mean = comparison_df[comparison_df["Variable"] == "wsp_99.0"]
            wdir_mean = comparison_df[comparison_df["Variable"] == "wdir_99.0"]
            fig_mean_comp = go.Figure()
            fig_mean_comp.add_trace(
                go.Bar(
                    x=["Wind Speed", "Wind Direction"],
                    y=[wsp_mean["Scotland Mean"].values[0], wdir_mean["Scotland Mean"].values[0]],
                    name="Scotland",
                    marker_color="blue"
                )
            )
            fig_mean_comp.add_trace(
                go.Bar(
                    x=["Wind Speed", "Wind Direction"],
                    y=[wsp_mean["Ireland Mean"].values[0], wdir_mean["Ireland Mean"].values[0]],
                    name="Ireland",
                    marker_color="green"
                )
            )
            fig_mean_comp.update_layout(barmode="group", title="Mean Values Comparison")
            st.plotly_chart(fig_mean_comp, use_container_width=True)
        else:
            st.info("Wind Speed or Wind Direction variables not found in the comparison data for mean comparison.")
    else:
        st.info("No valid comparison data available for mean comparison.")

    # Boxplots for Wind Speed and Wind Direction
    st.subheader("Boxplot Comparison")
    if "wsp_99.0" in df_scotland_meso.columns and "wsp_99.0" in df_ireland_meso.columns:
        fig_wsp_box = px.box(
            pd.concat([
                df_scotland_meso[["wsp_99.0"]].assign(Location="Scotland"),
                df_ireland_meso[["wsp_99.0"]].assign(Location="Ireland")
            ]),
            x="Location", y="wsp_99.0", color="Location",
            color_discrete_map={"Scotland": "blue", "Ireland": "green"},
            title="Wind Speed (wsp_99.0) Boxplot"
        )
        st.plotly_chart(fig_wsp_box, use_container_width=True)
    
    if "wdir_99.0" in df_scotland_meso.columns and "wdir_99.0" in df_ireland_meso.columns:
        fig_wdir_box = px.box(
            pd.concat([
                df_scotland_meso[["wdir_99.0"]].assign(Location="Scotland"),
                df_ireland_meso[["wdir_99.0"]].assign(Location="Ireland")
            ]),
            x="Location", y="wdir_99.0", color="Location",
            color_discrete_map={"Scotland": "blue", "Ireland": "green"},
            title="Wind Direction (wdir_99.0) Boxplot"
        )
        st.plotly_chart(fig_wdir_box, use_container_width=True)

# ------------------------------------------------------------------------------
# LiDAR DATA ANALYSIS
# ------------------------------------------------------------------------------
st.markdown('<div class="rubric-header">LiDAR Data </div>', unsafe_allow_html=True)

# Styled file uploaders for LiDAR data (horizontal layout)
col1, col2 = st.columns([1, 1])
with col1:
    scotland_lidar_file = st.file_uploader("Scotland  ", type=["csv"], key="scotland_lidar")
with col2:
    ireland_lidar_file = st.file_uploader("Ireland ", type=["csv"], key="ireland_lidar")

if scotland_lidar_file and ireland_lidar_file:
    df_scotland_lidar = pd.read_csv(scotland_lidar_file, header=0)
    df_ireland_lidar = pd.read_csv(ireland_lidar_file, header=0)

    def preprocess_lidar(df):
        df.columns = df.columns.str.strip()
        for col in df.columns:
            sample_vals = df[col].astype(str).values[:10]
            if any(" m/s" in val for val in sample_vals):
                df[col] = df[col].str.replace(" m/s", "", regex=False)
        for col in df.select_dtypes(include="object").columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df.dropna(how='all', inplace=True)
        return df
    
    df_scotland_lidar = preprocess_lidar(df_scotland_lidar)
    df_ireland_lidar = preprocess_lidar(df_ireland_lidar)

    st.subheader("Data Previews")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Scotland LiDAR Data**")
        st.dataframe(df_scotland_lidar.head(10))
    with col2:
        st.write("**Ireland LiDAR Data**")
        st.dataframe(df_ireland_lidar.head(10))

    st.subheader("Descriptive Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Scotland**")
        st.dataframe(df_scotland_lidar.describe())
    with col2:
        st.write("**Ireland**")
        st.dataframe(df_ireland_lidar.describe())

    st.subheader("Correlation Analysis")
    # Updated correlation heatmaps: include all numeric attributes, larger size, and annotations
    if not df_scotland_lidar.empty:
        corr_scotland = df_scotland_lidar.corr()
        fig_scot = px.imshow(corr_scotland,
                             color_continuous_scale="RdBu",
                             title="Scotland LiDAR Correlation",
                             width=1200,
                             height=800,
                             text_auto=True)
        st.plotly_chart(fig_scot, use_container_width=True)
    if not df_ireland_lidar.empty:
        corr_ireland = df_ireland_lidar.corr()
        fig_ire = px.imshow(corr_ireland,
                            color_continuous_scale="RdBu",
                            title="Ireland LiDAR Correlation",
                            width=1200,
                            height=800,
                            text_auto=True)
        st.plotly_chart(fig_ire, use_container_width=True)

    st.subheader("Wind Speed at Different Heights")
    scotland_speed_cols = [col for col in df_scotland_lidar.columns if "horizontal wind speed" in col.lower()]
    ireland_speed_cols = [col for col in df_ireland_lidar.columns if "horizontal wind speed" in col.lower()]
    common_cols = list(set(scotland_speed_cols) & set(ireland_speed_cols))
    if not common_cols:
        st.warning("No common 'Horizontal Wind Speed' columns found. Check your CSV column names!")
    else:
        for col in common_cols:
            scotland_data = df_scotland_lidar[col].dropna()
            ireland_data = df_ireland_lidar[col].dropna()
            combined_data = pd.concat([scotland_data, ireland_data])
            q1 = combined_data.quantile(0.25)
            q3 = combined_data.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            fig = go.Figure()
            fig.add_trace(go.Box(y=scotland_data, name=f"Scotland {col}", marker_color="blue", boxpoints="outliers"))
            fig.add_trace(go.Box(y=ireland_data, name=f"Ireland {col}", marker_color="green", boxpoints="outliers"))
            fig.update_layout(title=f"{col} Comparison",
                              yaxis_range=[max(lower_bound, combined_data.min()), min(upper_bound, combined_data.max())],
                              height=600)
            st.plotly_chart(fig, use_container_width=True)

#EVENT DETECTION
# ------------------------------------------------------------------------------
st.markdown('<div class="rubric-header">Event Detection</div>', unsafe_allow_html=True)

# LiDAR Event Detection Logic
import pandas as pd
import requests
from datetime import datetime

# Load LiDAR Data (Use your actual URLs or file paths here)
scotland_lidar_data = pd.read_csv("https://drive.google.com/uc?id=1qphhcsLxFOHE84021L1_5h2riKwnYTWn", skiprows=2)  # Skipping metadata rows
ireland_lidar_data = pd.read_csv("https://drive.google.com/uc?id=19-uDnkdPrdBKhhHMAWADQql8Ik8x1tiw", skiprows=2)  # Skipping metadata rows

# Ensure that the wind speed and wind direction columns are numeric (convert to float, invalid values become NaN)
scotland_lidar_data['Horizontal Wind Speed (m/s) at 99m'] = pd.to_numeric(scotland_lidar_data['Horizontal Wind Speed (m/s) at 99m'], errors='coerce')
scotland_lidar_data['Wind Direction (deg) at 99m'] = pd.to_numeric(scotland_lidar_data['Wind Direction (deg) at 99m'], errors='coerce')

ireland_lidar_data['Horizontal Wind Speed (m/s) at 99m'] = pd.to_numeric(ireland_lidar_data['Horizontal Wind Speed (m/s) at 99m'], errors='coerce')
ireland_lidar_data['Wind Direction (deg) at 99m'] = pd.to_numeric(ireland_lidar_data['Wind Direction (deg) at 99m'], errors='coerce')

# Detect events from LiDAR data
def detect_events_from_lidar(lidar_data):
    events = []
    previous_wind_direction = None  # To store the previous wind direction for comparison
    
    for index, row in lidar_data.iterrows():
        # Skip rows with invalid wind speed (e.g., 9999.0 m/s) or missing wind speed
        if row['Horizontal Wind Speed (m/s) at 99m'] in [None, 9999.0]:
            continue
        
        # Detect High Wind Speed event based on wind speed at 99m
        if 'Horizontal Wind Speed (m/s) at 99m' in row and row['Horizontal Wind Speed (m/s) at 99m'] > 10:
            events.append({
                'Event': 'High Wind Speed',
                'Time': row['Time and Date'],
                'Wind Speed': row['Horizontal Wind Speed (m/s) at 99m']
            })
        
        # Detect Wind Direction Change event based on the threshold change in degrees
        if 'Wind Direction (deg) at 99m' in row and previous_wind_direction is not None:
            wind_direction_change = abs(row['Wind Direction (deg) at 99m'] - previous_wind_direction)
            if wind_direction_change > 30:  # Threshold for wind direction change
                events.append({
                    'Event': 'Wind Direction Change',
                    'Time': row['Time and Date'],
                    'Wind Direction Change': wind_direction_change
                })
        
        # Update the previous wind direction for the next row comparison
        previous_wind_direction = row['Wind Direction (deg) at 99m']
        
    return events

# LiDAR event detection for Scotland and Ireland
scotland_events = detect_events_from_lidar(scotland_lidar_data)
ireland_events = detect_events_from_lidar(ireland_lidar_data)

# Open-Meteo API URL (we'll use hourly temperature data)
OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"

# Function to query Open-Meteo for weather data based on event time
def get_weather_data(lat, lon, time):
    event_time = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
    iso_time = event_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,wind_speed_10m,precipitation,wind_direction_10m",
        "start": iso_time,
        "end": iso_time,
        "timezone": "Europe/London",
    }

    response = requests.get(OPEN_METEO_API_URL, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# ------------------------------------------------------------------------------
# Check for weather data for each LiDAR event
# ------------------------------------------------------------------------------
def check_weather_for_event(event, location_coords):
    event_time = event['Time']
    event_type = event['Event']
    
    weather_data = get_weather_data(location_coords['lat'], location_coords['lon'], event_time)
    
    if weather_data:
        hourly_data = weather_data.get('hourly', {})
        wind_speed = hourly_data.get('wind_speed_10m', [None])[0]
        wind_direction = hourly_data.get('wind_direction_10m', [None])[0]
        temperature = hourly_data.get('temperature_2m', [None])[0]
        precipitation = hourly_data.get('precipitation', [None])[0]
        
        if event_type == 'High Wind Speed' and wind_speed and wind_speed > 20:
            return f"Event: {event_type} at {event['Time']} aligns with weather: Wind speed {wind_speed} m/s."
        
        if event_type == 'Wind Direction Change' and wind_direction is not None:
            return f"Event: {event_type} at {event['Time']} aligns with weather: Wind direction change {wind_direction}°."
        
        return f"Event: {event_type} at {event['Time']} does not align with weather data."
    
    return f"Weather data not available for event at {event['Time']}."

# Example coordinates for Scotland and Ireland (can be dynamic or extracted from the data)
scotland_coords = {'lat': 56.4907, 'lon': -4.2026}  # Scotland latitude, longitude
ireland_coords = {'lat': 53.1424, 'lon': -7.6921}  # Ireland latitude, longitude

# Check for weather data for each LiDAR event (Scotland)
for event in scotland_events:
    result = check_weather_for_event(event, scotland_coords)
    st.write(f"Event: {event['Event']} at {event['Time']}")
    # Print wind speed only for "High Wind Speed" events
    if 'Wind Speed' in event:
        st.write(f"Detected Wind Speed: {event['Wind Speed']} m/s")
    st.write(result)
    st.write("------")  # Separate results for each event for easier analysis

# Optionally, you can also check for Ireland events as well
for event in ireland_events:
    result = check_weather_for_event(event, ireland_coords)
    st.write(f"Event: {event['Event']} at {event['Time']}")
    # Print wind speed only for "High Wind Speed" events
    if 'Wind Speed' in event:
        st.write(f"Detected Wind Speed: {event['Wind Speed']} m/s")
    st.write(result)
    st.write("------")  # Separate results for each event for easier analysis