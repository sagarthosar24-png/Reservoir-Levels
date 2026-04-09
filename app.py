import streamlit as st
import numpy as np

# --- 1. DATA TABLES ---
# (Dicionaries converted to arrays for fast lookup in the loop)
u_data = {
    90.000: 4.336, 90.025: 4.354, 90.050: 4.371, 90.075: 4.389, 90.100: 4.406,
    90.125: 4.424, 90.150: 4.441, 90.175: 4.459, 90.200: 4.476, 90.225: 4.494,
    90.250: 4.511, 90.275: 4.529, 90.300: 4.546, 90.325: 4.564, 90.350: 4.581,
    90.375: 4.599, 90.400: 4.616, 90.425: 4.634, 90.450: 4.651, 90.475: 4.669,
    90.500: 4.686, 90.525: 4.704, 90.550: 4.721, 90.575: 4.739, 90.600: 4.756,
    90.625: 4.774, 90.650: 4.791, 90.675: 4.809, 90.700: 4.826, 90.725: 4.844,
    90.750: 4.861, 90.775: 4.879, 90.800: 4.896, 90.825: 4.914, 90.850: 4.931,
    90.875: 4.949, 90.900: 4.966, 90.925: 4.984, 90.950: 5.001, 90.975: 5.019,
    91.000: 5.036, 91.025: 5.054, 91.050: 5.071, 91.075: 5.089, 91.100: 5.106,
    91.125: 5.124, 91.150: 5.141, 91.175: 5.159, 91.200: 5.176, 91.225: 5.194,
    91.250: 5.211, 91.275: 5.229, 91.300: 5.246, 91.325: 5.264, 91.350: 5.281,
    91.375: 5.299, 91.400: 5.316, 91.425: 5.334, 91.450: 5.351, 91.475: 5.369,
    91.500: 5.386, 91.525: 5.404, 91.550: 5.421, 91.575: 5.439, 91.600: 5.456,
    91.625: 5.474, 91.650: 5.491, 91.675: 5.509, 91.700: 5.526, 91.725: 5.544,
    91.750: 5.561, 91.775: 5.579, 91.800: 5.596, 91.825: 5.614, 91.850: 5.631,
    91.875: 5.649, 91.900: 5.666, 91.925: 5.684, 91.950: 5.701, 91.975: 5.719,
    92.000: 5.736, 92.025: 5.756, 92.050: 5.776, 92.075: 5.796, 92.100: 5.816,
    92.125: 5.836, 92.150: 5.856, 92.175: 5.876, 92.200: 5.896, 92.225: 5.916,
    92.250: 5.936, 92.275: 5.956, 92.300: 5.976, 92.325: 5.997, 92.350: 6.017,
    92.375: 6.037, 92.400: 6.057, 92.425: 6.077, 92.450: 6.097, 92.475: 6.117,
    92.500: 6.137, 92.525: 6.157, 92.550: 6.177, 92.575: 6.197, 92.600: 6.217,
    92.625: 6.237, 92.650: 6.257, 92.675: 6.278, 92.700: 6.298, 92.725: 6.318,
    92.750: 6.338, 92.775: 6.354, 92.800: 6.370, 92.825: 6.390, 92.850: 6.410,
    92.875: 6.434, 92.900: 6.458, 92.925: 6.478, 92.950: 6.498, 92.975: 6.519,
    93.000: 6.539, 93.025: 6.559, 93.050: 6.579, 93.075: 6.599, 93.100: 6.619,
    93.125: 6.639, 93.150: 6.659, 93.175: 6.679, 93.200: 6.699, 93.225: 6.719,
    93.250: 6.739, 93.275: 6.759, 93.300: 6.779, 93.325: 6.800, 93.350: 6.820,
    93.375: 6.840, 93.400: 6.860, 93.425: 6.880, 93.450: 6.900, 93.475: 6.920,
    93.500: 6.940, 93.525: 6.960, 93.550: 6.980, 93.575: 7.000, 93.600: 7.020,
    93.625: 7.040, 93.650: 7.060, 93.675: 7.081, 93.700: 7.101, 93.725: 7.121,
    93.750: 7.141, 93.775: 7.161, 93.800: 7.181, 93.825: 7.201, 93.850: 7.221,
    93.875: 7.241, 93.900: 7.261, 93.925: 7.281, 93.950: 7.301, 93.975: 7.322,
    94.000: 7.342, 94.025: 7.368, 94.050: 7.394, 94.075: 7.411, 94.100: 7.427,
    94.125: 7.448, 94.150: 7.469, 94.175: 7.491, 94.200: 7.512, 94.225: 7.524,
    94.250: 7.535, 94.275: 7.596, 94.300: 7.657, 94.325: 7.708, 94.350: 7.759,
    94.375: 7.811, 94.400: 7.862, 94.425: 7.913, 94.450: 7.964, 94.475: 8.016,
    94.500: 8.067, 94.525: 8.118, 94.550: 8.169, 94.575: 8.220, 94.600: 8.271,
    94.625: 8.323, 94.650: 8.374, 94.675: 8.425, 94.700: 8.476, 94.725: 8.528,
    94.750: 8.579, 94.775: 8.630, 94.800: 8.681, 94.825: 8.733, 94.850: 8.785,
    94.875: 8.836, 94.900: 8.886, 94.925: 8.937, 94.950: 8.988, 94.975: 9.035,
    95.000: 9.081
}

l_data = {89.0: 2.87, 90.0: 3.29, 91.0: 3.64, 92.0: 4.02, 93.0: 4.48, 94.0: 4.84, 95.0: 5.94} # Simplified for example

u_rl_arr = np.array(list(u_data.keys()))
u_mcm_arr = np.array(list(u_data.values()))

# --- 2. LAYOUT ---
st.set_page_config(page_title="Operational Shift Planner", layout="wide")
st.title("🌊 Multi-Reservoir Generation Planner")

# --- 3. INPUTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Upper Lake Settings")
    curr_u = st.number_input("Current Upper RL (m)", value=94.400, format="%.3f", step=0.025)
    u_rate = 0.820  # MCM/MUS

with col2:
    st.subheader("📍 Gate & Lower Reservoir")
    curr_l = st.number_input("Current Lower RL (m)", value=92.500, format="%.3f", step=0.063)
    gate_is_open = st.toggle("Interconnecting Gate Open?", value=False)
    hours_open = st.number_input("Hours to keep Gate Open", min_value=0.0, value=1.0, step=0.5)

# --- 4. CALCULATION ---
if st.button("Generate Dispatch Report", type="primary"):
    
    # Get Initial Content
    u_idx = (np.abs(u_rl_arr - curr_u)).argmin()
    start_u_mcm = u_mcm_arr[u_idx]
    
    # Iterative Smart Loop for Hydraulic Transfer
    gate_vol_total = 0.0
    temp_u_mcm = start_u_mcm
    temp_l_rl = curr_l # Simplified constant lower level for head calc
    
    if gate_is_open:
        total_minutes = int(hours_open * 60)
        step_min = 10
        
        for m in range(0, total_minutes, step_min):
            # 1. Find Current RL from current volume
            idx_loop = (np.abs(u_mcm_arr - temp_u_mcm)).argmin()
            current_u_rl = u_rl_arr[idx_loop]
            
            # 2. Check head difference
            head_diff = current_u_rl - temp_l_rl
            
            # 3. Get rate
            if head_diff > 3.0: rate = 0.17
            elif 2.0 <= head_diff <= 3.0: rate = 0.15
            elif 1.5 <= head_diff < 2.0: rate = 0.12
            else: rate = 0.08
            
            # 4. Step Volume
            step_vol = rate * (step_min / 60)
            gate_vol_total += step_vol
            temp_u_mcm -= step_vol
            
    # Final Result Math
    final_u_mcm = temp_u_mcm # After gate loss
    final_u_idx = (np.abs(u_mcm_arr - final_u_mcm)).argmin()
    final_u_rl = u_rl_arr[final_u_idx]

    # --- 5. RESULTS ---
    st.divider()
    st.header(f"Final Upper Lake Prediction: {final_u_rl:.3f} m")
    
    r1, r2 = st.columns(2)
    with r1:
        st.subheader("📊 Volume Balance")
        st.write(f"Starting Volume: **{start_u_mcm:.3f} MCM**")
        if gate_is_open:
            st.write(f"Total Water Transferred Out: **{gate_vol_total:.3f} MCM**")
            st.write(f"Final Predicted Volume: **{temp_u_mcm:.3f} MCM**")
            
    with r2:
        st.subheader("💡 Operational Insight")
        if gate_is_open:
            st.info(f"The loop adjusted the flow rate as head dropped from **{curr_u - curr_l:.2f}m**.")
            st.success("Calculations complete using 10-minute time-steps.")
    
