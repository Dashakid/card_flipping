# --- UPDATED RIGGED LOGIC (Fixed Population Error) ---
if 'board' not in st.session_state:
    # 1. Full Prize Pools from your image
    jackpots_list = ["✨ Sextape ✨", "🎁 5 minute custom", "👑 6 months free vip"]
    
    high_prizes = [
        "Private live", "Tits flash + play", "Custom pic", "Lush control", 
        "Solo suki choice", "Name on body", "Pussy Flash", "Username Change", 
        "Wet Check + Taste", "Asshole flash", "High Value Spin", "Nipple clamps"
    ]
    
    mid_low_prizes = [
        "Booty bundle", "Lingerie bundle", "Dirty Talk (kink)", "Outfit change", 
        "Camel toe", "15 min sexting", "Toy tour", "7 Raffle tickets", 
        "Red ass spanks", "JOI LIVE", "Lick dildo + dirty talk", "Lingerie vid",
        "Nude pics Suki choice", "Blowjob", "Spit on titties + Shake", "Vibrator", 
        "Rub pussy", "Twerk on dildo", "Custom vm (2 min)", "Titty bundle", 
        "Twerking video", "Shower video", "Moan name + Vibe", "Cum countdown"
    ]

    # 2. Rig the deck: 3 Jackpots + 7 High + 20 Mid/Low = 30 Cards
    final_deck = []
    final_deck += jackpots_list # Adds all 3
    
    # We use random.sample for High Prizes because we have 12 to pick 7 from
    final_deck += random.sample(high_prizes, 7) 
    
    # We use random.sample for Mid/Low because we now have 24 items to pick 20 from
    final_deck += random.sample(mid_low_prizes, 20)
    
    random.shuffle(final_deck)
    st.session_state.board = [{"prize": p, "flipped": False} for p in final_deck]
    