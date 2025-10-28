import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Setup ---
st.set_page_config(page_title="Smart Medical Waste Dashboard", page_icon="♻️", layout="wide")

st.title("🧭 Smart Medical Waste Monitoring Dashboard")
st.markdown("### Real-time data from AI-powered Smart Bin System")

# --- Summary Metrics ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Detection Accuracy", "93.4%", "↑ 2.1%")
col2.metric("Total Waste Today", "32.5 kg", "+4.8 kg")
col3.metric("System Status", "☀️ Solar Active")
col4.metric("Last Sterilization", "5 min ago", "99% Germ Reduction")

st.divider()

# --- Waste Compartment Data ---
data = {
    "Waste Type": ["Sharp", "Chemical", "Anatomical", "Plastic"],
    "Fill Level (%)": [82, 67, 44, 79],
    "Auto Sterilized": ["✅ Yes", "✅ Yes", "✅ Yes", "⚠️ Scheduled"],
    "AI Detection (%)": [95, 91, 93, 90],
    "Emission Impact": ["Low", "Medium", "Low", "High"]
}
df = pd.DataFrame(data)

st.subheader("🗑️ Waste Segregation Analysis")
st.dataframe(df, use_container_width=True)

# --- Fill Level Bar Chart ---
st.subheader("📊 Fill Level by Waste Type")
fig_bar = px.bar(
    df,
    x="Waste Type",
    y="Fill Level (%)",
    color="Waste Type",
    text="Fill Level (%)",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig_bar.update_traces(textposition="outside")
fig_bar.update_yaxes(range=[0, 100])
st.plotly_chart(fig_bar, use_container_width=True)

# --- Pie Chart for Waste Distribution ---
st.subheader("🥧 Waste Type Distribution (%)")
waste_distribution = pd.DataFrame({
    "Type": ["Sharp", "Chemical", "Anatomical", "Plastic"],
    "Percentage": [25, 20, 15, 40]
})
fig_pie = px.pie(waste_distribution, names="Type", values="Percentage", hole=0.4)
st.plotly_chart(fig_pie, use_container_width=True)

# --- Solar & Battery Panel ---
st.subheader("🔋 Solar & Battery Status")
col1, col2, col3 = st.columns(3)
col1.metric("Battery Level", "92%")
col2.metric("Solar Panel", "Active")
col3.metric("Uptime", "24 hrs continuous")

# --- Emission Data ---
st.subheader("🌫️ Emission Data (Today)")
emission_data = pd.DataFrame({
    "Bin": ["Sharp", "Chemical", "Anatomical", "Plastic"],
    "CO₂ Saved (g)": [120, 95, 105, 135],
})
fig_emission = px.line(emission_data, x="Bin", y="CO₂ Saved (g)", markers=True)
st.plotly_chart(fig_emission, use_container_width=True)

# --- AI Insights ---
st.subheader("🤖 AI Insights")
st.info("""
- Waste detection confidence stable at **93%**  
- Plastic waste increased by **15%** over last 3 days  
- Solar system performing optimally under current conditions  
- Auto sterilization successful in **9/9 cycles today**
""")

# --- Reward System Section ---
st.subheader("🏅 Reward System (QR Scan Logs)")
reward_data = pd.DataFrame({
    "User": ["U-145", "U-157", "U-101", "U-167", "U-192"],
    "QR ID": ["QR098", "QR113", "QR076", "QR142", "QR189"],
    "Waste Dropped": ["Plastic", "Sharp", "Chemical", "Plastic", "Anatomical"],
    "Points Earned": [10, 12, 8, 15, 11]
})
st.dataframe(reward_data, use_container_width=True)

total_points = reward_data["Points Earned"].sum()
avg_points = reward_data["Points Earned"].mean()

col1, col2 = st.columns(2)
col1.metric("Total Users Rewarded Today", len(reward_data))
col2.metric("Average Points / User", f"{avg_points:.1f}")

# --- Footer ---
st.markdown("---")
st.caption("Developed by **Team GreenMind | Smart Waste Management Initiative** 🌿 | Powered by **AI + IoT + Solar** ☀️")
