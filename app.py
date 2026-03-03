import streamlit as st
import random

# --- CONFIG & THEME ---
st.set_page_config(page_title="Desiwaifu's Gacha", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fff0f5; }
    /* The Unflipped Card Style */
    div.stButton > button:first-child {
        background-color: #ffb6c1;
        color: white;
        border-radius: 15px;
        border: 2px solid #ff69b4;
        height: 80px;
        width: 100%;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff69b4;
        border: 2px solid white;
        transform: scale(1.02);
    }
    /* The Revealed Prize Style */
    .prize-revealed {
        background-color: #ffffff;
        border: 3px dashed #ff1493;
        color: #ff1493;
        border-radius: 15px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-weight: bold;
        font-size: 0.85rem;
        box-shadow: 2px 2px 10px rgba(255, 105, 180, 0.3);
    }
    h1 { color: #ff69b4; text-align: center; font-family: 'Comic Sans MS', cursive; }
    </style>
    """, unsafe_allow_html=True)

# --- UPDATED RIGGED LOGIC (3 JACKPOTS) ---
if 'board' not in st.session_state:
    # 1. Define the pools from your image
    jackpots_list = ["✨ SEXTAPE ✨", "🎁 5 MIN CUSTOM", "👑 6 MONTH VIP"]
    high_prizes = ["Private live", "Tits flash + play", "Custom pic", "Lush control", "Solo choice", "Name on body", "Pussy Flash", "Username Change"]
    mid_low_prizes = ["Booty bundle", "Lingerie bundle", "Dirty Talk", "Outfit change", "Camel toe", "15 min sexting", "Toy tour", "7 Raffle tickets", "Red ass spanks", "JOI LIVE", "Lick dildo", "Lingerie vid", "Nude pics", "Blowjob", "Spit on titties", "Vibrator", "Rub pussy", "Twerk on dildo"]

    # 2. Rig the deck: 3 Jackpots + 7 High + 20 Mid/Low = 30 Cards
    final_deck = []
    final_deck += jackpots_list # Adds all 3 jackpots
    final_deck += random.sample(high_prizes, 7)
    final_deck += random.sample(mid_low_prizes, 20)
    
    random.shuffle(final_deck)
    
    # Store in session state
    st.session_state.board = [{"prize": p, "flipped": False} for p in final_deck]

# --- UI HEADER ---
st.markdown("<h1>✨ Desiwaifu's Lucky Cards ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #db7093;'>30 Cards total | <b>3 JACKPOTS</b> hidden inside! ✨<br>$75 per flip (✿◡‿◡)</p>", unsafe_allow_html=True)

# --- THE GRID ---
# Using 5 columns to make a clean 6-row layout
cols = st.columns(5)
for i, card in enumerate(st.session_state.board):
    with cols[i % 5]:
        if card["flipped"]:
            st.markdown(f"<div class='prize-revealed'>{card['prize']}</div>", unsafe_allow_html=True)
        else:
            if st.button(f"#{i+1}", key=f"btn_{i}"):
                st.session_state.board[i]["flipped"] = True
                st.rerun()

# --- FOOTER / RESET ---
st.write("---")
col_left, col_mid, col_right = st.columns([1,1,1])
with col_mid:
    if st.button("Reset New Board 🎀"):
        del st.session_state.board
        st.rerun()