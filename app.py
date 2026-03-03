import streamlit as st

# Define your grid data from the spreadsheet
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="wide", page_title="Dice Game Reveal")

# Custom CSS for a "Premium" look
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        background-color: #2e2e2e;
        color: white;
    }
    .reveal-box {
        background-color: #28a745;
        color: white;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎲 Dice Game: Reveal the Action")

# Initialize session state to keep track of flipped tiles
if 'flipped_tiles' not in st.session_state:
    st.session_state.flipped_tiles = set()

# Create the headers for Actions
header_cols = st.columns([1] + [2]*6)
for idx, action in enumerate(actions):
    header_cols[idx + 1].markdown(f"### {idx+1}. {action}")

# Create the rows for Body Parts
for row_idx, part in enumerate(body_parts):
    cols = st.columns([1] + [2]*6)
    cols[0].markdown(f"### {row_idx+1}. {part}") # Row Label
    
    for col_idx in range(6):
        tile_id = f"{row_idx}_{col_idx}"
        with cols[col_idx + 1]:
            if tile_id in st.session_state.flipped_tiles:
                # What shows after clicking
                st.markdown(f"<div class='reveal-box'>{actions[col_idx]}<br>{part}</div>", unsafe_allow_html=True)
            else:
                # The hidden tile
                if st.button(f"$75", key=tile_id):
                    st.session_state.flipped_tiles.add(tile_id)
                    st.rerun()