import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------------------------------------
# Streamlit Page Setup
# --------------------------------------------------------------------------------
st.set_page_config(
    page_title="Vestas Wind Analytics",
    layout="wide",
    page_icon="🌬️"
)

# --------------------------------------------------------------------------------
# Custom CSS / Theme Setup
# --------------------------------------------------------------------------------
def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f2f6;
        }
        
        .main .block-container {
            padding-top: 2rem;
            max-width: 1200px;
        }
        
        .stHeader {
            background: linear-gradient(45deg, #006699, #0099cc);
            color: white !important;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stButton button {
            background: #0099cc;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            transition: all 0.3s;
        }
        
        .stButton button:hover {
            background: #006699;
            transform: translateY(-2px);
        }
        
        .dataframe {
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .section-divider {
            border-top: 3px solid #0099cc;
            margin: 2rem 0;
            opacity: 0.7;
        }
        
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# --------------------------------------------------------------------------------
# HERO SECTION
# --------------------------------------------------------------------------------
st.markdown("""
<div style="text-align: center; padding: 4rem 0; background: linear-gradient(135deg, #006699, #0099cc); border-radius: 15px; margin-bottom: 2rem;">
    <h1 style="color: white; font-size: 2.5rem; margin-bottom: 1rem;">🌬️ Vestas Wind & LiDAR Analytics</h1>
    <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem;">Advanced Wind Data Analysis Platform for Scotland and Ireland</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------------------------------------
# MESOSCALE DATA ANALYSIS
# --------------------------------------------------------------------------------
with st.expander("🌐 Mesoscale Data Analysis", expanded=True):
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        scotland_meso_file = st.file_uploader(
            "Upload Scotland Mesoscale Data",
            type=["csv"],
            key="scotland_meso"
        )
    with col2:
        ireland_meso_file = st.file_uploader(
            "Upload Ireland Mesoscale Data",
            type=["csv"],
            key="ireland_meso"
        )

    if scotland_meso_file and ireland_meso_file:
        try:
            df_scotland_meso = pd.read_csv(scotland_meso_file)
            df_ireland_meso = pd.read_csv(ireland_meso_file)

            tab1, tab2, tab3 = st.tabs(["📊 Data Previews", "📈 Statistics", "🔍 Comparative Analysis"])
            
            with tab1:
                st.subheader("Data Previews")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Scotland Data Sample**")
                    st.dataframe(df_scotland_meso.head().style.background_gradient(cmap="Blues"), height=200)
                with col2:
                    st.markdown("**Ireland Data Sample**")
                    st.dataframe(df_ireland_meso.head().style.background_gradient(cmap="Greens"), height=200)

            with tab2:
                st.subheader("Descriptive Statistics")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Scotland Summary**")
                    st.dataframe(df_scotland_meso.describe().style.format("{:.2f}").background_gradient(cmap="Blues"))
                with col2:
                    st.markdown("**Ireland Summary**")
                    st.dataframe(df_ireland_meso.describe().style.format("{:.2f}").background_gradient(cmap="Greens"))

            with tab3:
                st.subheader("Comparative Analysis")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f'<div class="metric-card">🌬️ Scot. Avg Speed<br><h2>{df_scotland_meso["wsp_99.0"].mean():.1f} m/s</h2></div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="metric-card">🌬️ Ire. Avg Speed<br><h2>{df_ireland_meso["wsp_99.0"].mean():.1f} m/s</h2></div>', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'<div class="metric-card">🧭 Scot. Avg Dir<br><h2>{df_scotland_meso["wdir_99.0"].mean():.1f}°</h2></div>', unsafe_allow_html=True)
                with col4:
                    st.markdown(f'<div class="metric-card">🧭 Ire. Avg Dir<br><h2>{df_ireland_meso["wdir_99.0"].mean():.1f}°</h2></div>', unsafe_allow_html=True)

                fig = go.Figure()
                fig.add_trace(go.Box(y=df_scotland_meso['wsp_99.0'], name='Scotland', marker_color='#006699'))
                fig.add_trace(go.Box(y=df_ireland_meso['wsp_99.0'], name='Ireland', marker_color='#009933'))
                fig.update_layout(
                    title="Wind Speed Distribution Comparison",
                    template="plotly_white",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error processing mesoscale data: {str(e)}")

# --------------------------------------------------------------------------------
# LIDAR DATA ANALYSIS
# --------------------------------------------------------------------------------
with st.expander("📡 LiDAR Data Analysis", expanded=True):
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        scotland_lidar_file = st.file_uploader(
            "Upload Scotland LiDAR Data",
            type=["csv"],
            key="scotland_lidar"
        )
    with col2:
        ireland_lidar_file = st.file_uploader(
            "Upload Ireland LiDAR Data",
            type=["csv"],
            key="ireland_lidar"
        )

    if scotland_lidar_file and ireland_lidar_file:
        try:
            df_scotland_lidar = pd.read_csv(scotland_lidar_file)
            df_ireland_lidar = pd.read_csv(ireland_lidar_file)

            tab1, tab2, tab3 = st.tabs(["📋 Data Overview", "📐 Vertical Profiles", "📉 Time Series Analysis"])

            with tab1:
                st.subheader("Data Overview")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Scotland LiDAR Metrics**")
                    st.dataframe(df_scotland_lidar.describe().style.format("{:.2f}").background_gradient(cmap="Blues"))
                with col2:
                    st.markdown("**Ireland LiDAR Metrics**")
                    st.dataframe(df_ireland_lidar.describe().style.format("{:.2f}").background_gradient(cmap="Greens"))

            with tab2:
                st.subheader("Vertical Wind Profile Analysis")
                try:
                    fig = go.Figure(data=[
                        go.Scatter3d(
                            x=df_scotland_lidar["Wind Direction (deg) at 99m"],
                            y=df_scotland_lidar["Horizontal Wind Speed (m/s) at 99m"],
                            z=[99]*len(df_scotland_lidar),
                            mode='markers',
                            name='Scotland (99m)',
                            marker=dict(size=4, color='#006699', opacity=0.7)
                        ),
                        go.Scatter3d(
                            x=df_ireland_lidar["Wind Direction (deg) at 99m"],
                            y=df_ireland_lidar["Horizontal Wind Speed (m/s) at 99m"],
                            z=[99]*len(df_ireland_lidar),
                            mode='markers',
                            name='Ireland (99m)',
                            marker=dict(size=4, color='#009933', opacity=0.7)
                        )
                    ])
                    fig.update_layout(
                        scene=dict(
                            xaxis_title='Wind Direction (deg)',
                            yaxis_title='Wind Speed (m/s)',
                            zaxis_title='Height (m)'
                        ),
                        title="3D Wind Profile Comparison at 99m",
                        height=800,
                        template="plotly_dark"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                except KeyError as e:
                    st.error(f"Missing required column in LiDAR data: {str(e)}")

            with tab3:
                st.subheader("Temporal Analysis")
                try:
                    fig = px.line(
                        df_scotland_lidar,
                        x="Time and Date",
                        y="Horizontal Wind Speed (m/s) at 99m",
                        title="Scotland Wind Speed Time Series (99m)",
                        color_discrete_sequence=px.colors.sequential.Blues
                    )
                    fig.update_layout(hovermode="x unified", height=400)
                    st.plotly_chart(fig, use_container_width=True)
                except KeyError as e:
                    st.error(f"Missing required column for time series: {str(e)}")

        except Exception as e:
            st.error(f"Error processing LiDAR data: {str(e)}")

# --------------------------------------------------------------------------------
# Footer Section
# --------------------------------------------------------------------------------
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: #666; margin-top: 3rem;">
    <hr style="border-color: #ddd;">
    <p style="margin-top: 1rem;">© 2024 Vestas Wind Systems A/S | Analytics Platform v2.1</p>
    <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 0.5rem;">
        <a href="#" style="color: #0099cc; text-decoration: none;">Privacy Policy</a>
        <a href="#" style="color: #0099cc; text-decoration: none;">Terms of Service</a>
        <a href="#" style="color: #0099cc; text-decoration: none;">Documentation</a>
    </div>
</div>
""", unsafe_allow_html=True)