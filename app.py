import streamlit as st
import random
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="Desiwaifu's Gacha", page_icon="🌸", layout="wide")

# --- RIGGED PRIZE LOGIC ---
if 'board' not in st.session_state:
    # Pool definitions
    jackpots = ["Sextape", "5 min Custom", "6 Month VIP"]
    high_prizes = ["Private Live", "Tits Flash", "Username Change", "Nipple Clamps"]
    others = ["Nude Pics", "Twerk Vid", "Lingerie Pic", "JOI", "Sexting", "Toy Tour", "Outfit Change"]

    # Rigging: Pick exactly 1 Jackpot, 5 High Prizes, and 24 Others = 30 total
    game_prizes = [random.choice(jackpots)] 
    game_prizes += random.sample(high_prizes * 3, 5) # Mix of high
    game_prizes += [random.choice(others) for _ in range(24)]
    
    random.shuffle(game_prizes)
    st.session_state.board = game_prizes

# --- STYLING ---
st.markdown("""
    <style>
    .main { background-color: #fff0f5; }
    .title { color: #ff69b4; text-align: center; font-family: 'Comic Sans MS'; text-shadow: 2px 2px #ffc0cb; font-size: 50px; }
    .prize-list { background: white; padding: 15px; border-radius: 15px; border: 2px solid #ff69b4; margin-bottom: 20px; }
    </style>
    <div class="title">✨ Desiwaifu's Lucky Scratch ✨</div>
    """, unsafe_allow_html=True)

# Display the "Big Prizes" to entice viewers
st.markdown(f"""
<div class="prize-list">
    <h3 style='color: #ff1493; margin:0;'>💎 BIG PRIZES AVAILABLE:</h3>
    <p style='color: #db7093;'>Jackpot: {", ".join(["Sextape", "5 min Custom", "VIP"])} | $75 per scratch (✿◡‿◡)</p>
</div>
""", unsafe_allow_html=True)

# --- SCRATCH CARD COMPONENT ---
def scratch_card(label, prize, key):
    # This is a JavaScript/HTML Canvas bridge
    html_code = f"""
    <div id="wrapper_{key}" style="position: relative; width: 150px; height: 100px; user-select: none;">
        <div style="position: absolute; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: white; border: 2px solid #ff69b4; border-radius: 10px; color: #ff1493; font-weight: bold; text-align: center; font-family: sans-serif; font-size: 14px; padding: 5px;">
            {prize}
        </div>
        <canvas id="canvas_{key}" width="150" height="100" style="position: absolute; cursor: crosshair; border-radius: 10px;"></canvas>
    </div>

    <script>
        (function() {{
            const canvas = document.getElementById('canvas_{key}');
            const ctx = canvas.getContext('2d');
            let isDrawing = false;

            // Fill with "Scratch" layer (Pink Glitter style)
            ctx.fillStyle = '#ffb6c1';
            ctx.fillRect(0, 0, 150, 100);
            ctx.fillStyle = '#ff69b4';
            ctx.font = 'bold 16px sans-serif';
            ctx.fillText('{label}', 45, 55);

            function scratch(e) {{
                if (!isDrawing) return;
                const rect = canvas.getBoundingClientRect();
                const x = (e.clientX || e.touches[0].clientX) - rect.left;
                const y = (e.clientY || e.touches[0].clientY) - rect.top;
                
                ctx.globalCompositeOperation = 'destination-out';
                ctx.beginPath();
                ctx.arc(x, y, 15, 0, Math.PI * 2);
                ctx.fill();
            }}

            canvas.addEventListener('mousedown', () => isDrawing = true);
            canvas.addEventListener('mouseup', () => isDrawing = false);
            canvas.addEventListener('mousemove', scratch);
            canvas.addEventListener('touchstart', () => isDrawing = true);
            canvas.addEventListener('touchmove', scratch);
            canvas.addEventListener('touchend', () => isDrawing = false);
        }})();
    </script>
    """
    components.html(html_code, height=110)

# Render Grid
cols = st.columns(5)
for i, prize in enumerate(st.session_state.board):
    with cols[i % 5]:
        scratch_card(f"#{i+1}", prize, f"card_{i}")

if st.button("Reset New Batch 🎀"):
    del st.session_state.board
    st.rerun()