import streamlit as st
import random

# --- 1. THEME & STYLE ---
st.set_page_config(page_title="Desiwaifu's Gacha", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fff0f5; }
    div.stButton > button:first-child {
        background-color: #ffb6c1;
        color: white;
        border-radius: 15px;
        border: 2px solid #ff69b4;
        height: 80px;
        width: 100%;
        font-weight: bold;
        font-size: 18px;
    }
    div.stButton > button:hover {
        background-color: #ff69b4;
        border: 2px solid white;
    }
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
    }
    h1 { color: #ff69b4; text-align: center; font-family: 'Comic Sans MS', cursive; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. RIGGED LOGIC (30 CARDS) ---
if 'board' not in st.session_state:
    # Prizes pulled directly from your sheet
    jackpots = ["✨ Sextape ✨", "🎁 5 minute custom", "👑 6 months free vip"]
    
    high = [
        "Private live", "Tits flash + play", "Custom pic", "Lush control", 
        "Solo suki choice", "Name on body", "Pussy Flash", 
        "Wet Check + Taste", "Asshole flash", "High Value Spin",
    ]
    
    mid_low = [
        "Booty bundle", "Lingerie bundle", "Dirty Talk (kink)", "Outfit change", 
        "Camel toe", "15 min sexting", "Toy tour", "7 Raffle tickets", 
        "Red ass spanks", "JOI LIVE", "Lick dildo + dirty talk", "Lingerie vid",
        "Nude pics Suki choice", "Blowjob", "Spit on titties + Shake", "Vibrator", 
        "Rub pussy", "Twerk on dildo", "Custom vm (2 min)", "Titty bundle", 
        "Twerking video", "Shower video", "Moan name + Vibe", "Cum countdown"
    ]

    # Rigging: 3 Jackpots + 7 High + 20 Mid/Low = 30 Cards total
    deck = jackpots + random.sample(high, 7) + random.sample(mid_low, 20)
    random.shuffle(deck)
    st.session_state.board = [{"prize": p, "flipped": False} for p in deck]

# --- 3. UI DISPLAY ---
st.markdown("<h1>✨ Desiwaifu's Lucky Cards ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #db7093;'>$75 per flip | 3 Jackpots Hidden! (✿◡‿◡)</p>", unsafe_allow_html=True)

cols = st.columns(5)
for i, card in enumerate(st.session_state.board):
    with cols[i % 5]:
        if card["flipped"]:
            st.markdown(f"<div class='prize-revealed'>{card['prize']}</div>", unsafe_allow_html=True)
        else:
            if st.button(f"#{i+1}", key=f"btn_{i}"):
                st.session_state.board[i]["flipped"] = True
                st.rerun()

st.write("---")
if st.button("Reset New Board 🎀"):
    del st.session_state.board
    st.rerun()