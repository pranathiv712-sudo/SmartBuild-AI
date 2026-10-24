
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="SmartBuild AI",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 SmartBuild AI")
st.caption("Agentic AI for Smart Building Energy Optimization")

st.info(
    "Educational prototype using simulated sensor readings. "
    "It does not control real building equipment."
)

# Session history
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar inputs
st.sidebar.header("Building Sensor Inputs")

temperature = st.sidebar.slider(
    "Room temperature (°C)", 15.0, 35.0, 28.0, 0.5
)
occupancy = st.sidebar.slider(
    "People in room", 0, 100, 12
)
energy = st.sidebar.slider(
    "Current energy use (kW)", 0.0, 20.0, 8.0, 0.5
)
target_temp = st.sidebar.slider(
    "Comfort target (°C)", 20.0, 26.0, 23.0, 0.5
)
outside_temp = st.sidebar.slider(
    "Outside temperature (°C)", 10.0, 45.0, 32.0, 0.5
)

# Decision-making agent
def building_agent(temp, people, power, target, outside):
    actions = []
    reasons = []
    status = "Normal"

    if people == 0:
        actions.append("Recommend energy-saving HVAC mode")
        actions.append("Recommend switching off room lighting")
        reasons.append("The room is unoccupied.")

    else:
        if temp > target + 1:
            actions.append("Recommend increasing cooling")
            reasons.append(
                f"Room temperature ({temp:.1f}°C) is above "
                f"the comfort target ({target:.1f}°C)."
            )
        elif temp < target - 1:
            actions.append("Recommend reducing cooling")
            reasons.append(
                "Room temperature is below the comfort target."
            )
        else:
            actions.append("Maintain current comfort settings")
            reasons.append(
                "Room temperature is close to the comfort target."
            )

        if people >= 40:
            actions.append("Check ventilation for high occupancy")
            reasons.append(
                "High occupancy may require additional ventilation."
            )

    if power >= 12:
        actions.append("Flag high energy consumption for review")
        reasons.append(
            f"Energy use ({power:.1f} kW) exceeds the "
            "demo threshold of 12 kW."
        )
        status = "High energy use"

    if outside >= 35 and temp > target:
        actions.append("Monitor cooling demand during hot weather")
        reasons.append("Outdoor temperature is high.")

    return status, actions, reasons


status, actions, reasons = building_agent(
    temperature, occupancy, energy, target_temp, outside_temp
)

# Demo optimization score: a heuristic, not actual energy savings
score = 100

if occupancy == 0 and energy > 2:
    score -= 25

if energy >= 12:
    score -= 25

if temperature > target_temp + 2:
    score -= 15
elif temperature < target_temp - 2:
    score -= 10

score = max(0, min(100, score))

# Top metrics
st.subheader("Building Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Room Temperature", f"{temperature:.1f} °C")
c2.metric("Occupancy", f"{occupancy} people")
c3.metric("Energy Use", f"{energy:.1f} kW")
c4.metric("Agent Status", status)

# Optimization score
st.subheader("Energy Optimization Readiness")
st.metric("Demo Score", f"{score}/100")
st.progress(score / 100)
st.caption(
    "Illustrative rule-based score. It is not a measured "
    "energy-saving percentage."
)

# Agent recommendations
st.subheader("🤖 Agent Decision")

for reason in reasons:
    st.write(f"**Observation:** {reason}")

st.markdown("**Recommended Actions**")

for number, action in enumerate(actions, start=1):
    st.write(f"{number}. {action}")

# Energy chart
st.subheader("📊 Energy Monitoring")

chart_data = pd.DataFrame({
    "Energy use (kW)": [5.5, 8.0, 13.5, 4.0, energy]
}, index=[
    "Morning",
    "Mid-morning",
    "Peak",
    "Unoccupied example",
    "Current scenario"
])

st.bar_chart(chart_data)

st.caption(
    "The first four readings are illustrative sample values. "
    "The current scenario uses your selected slider value."
)

# Explain the agent
left, right = st.columns(2)

with left:
    st.subheader("How the Agent Works")
    st.write("1. **Observe:** reads building sensor values.")
    st.write("2. **Evaluate:** checks comfort and energy thresholds.")
    st.write("3. **Decide:** selects suitable recommendations.")
    st.write("4. **Explain:** provides reasons for its decisions.")

with right:
    st.subheader("Try These Scenarios")
    st.write("- Set occupancy to 0.")
    st.write("- Increase energy use to 15 kW.")
    st.write("- Set temperature to 30°C.")
    st.write("- Compare the score across scenarios.")

# Save assessment
st.subheader("Assessment History")

if st.button("Save Current Assessment"):
    st.session_state.history.append({
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Temperature (°C)": temperature,
        "Occupancy": occupancy,
        "Energy (kW)": energy,
        "Outside (°C)": outside_temp,
        "Agent Status": status,
        "Optimization Score": score,
        "Recommended Actions": "; ".join(actions)
    })
    st.success("Assessment saved for this session.")

if st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df, use_container_width=True)

    st.download_button(
        "Download Assessment History (CSV)",
        data=history_df.to_csv(index=False).encode("utf-8"),
        file_name="smartbuild_history.csv",
        mime="text/csv"
    )

st.divider()
st.caption(
    "SmartBuild AI | Student project prototype | "
    "Real-world building changes require engineering validation."
)
