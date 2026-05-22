import streamlit as st
import random
import qrcode
from PIL import Image
import io

# --- Historical Data ---
REAL_4D_FREQUENCIES = {
    "pos1": ['9', '7', '3', '8', '1', '5', '2', '6', '0', '4'],
    "pos2": ['4', '1', '8', '6', '3', '9', '2', '0', '7', '5'],
    "pos3": ['4', '7', '2', '0', '5', '9', '1', '8', '6', '3'],
    "pos4": ['6', '8', '3', '1', '9', '5', '2', '0', '4', '7']
}
REAL_TOTO_HOT = [40, 15, 36, 46, 21, 38, 11, 22, 13, 39, 7, 34, 30, 28, 18]
REAL_TOTO_COLD = [45, 1, 9, 10, 6, 12, 5, 23, 44, 16, 26, 47, 41, 14, 32]

# --- UI Setup ---
st.title("--- YOUR CHOICE, YOUR GAIN ---")

game_choice = st.radio("Your Choice", ["4D", "TOTO"])

year_context = "since 1986 draw results" if game_choice == "4D" else "since 2014 draw results"

strat_choice = st.selectbox("Choose Your Strategy", [
    f"Hot Numbers (Based on {year_context})",
    f"Cold Numbers (Based on {year_context})",
    "Balanced Blend / Surprise Selection"
])

if st.button("Generate Lucky Numbers"):
    if game_choice == "4D":
        if "Hot" in strat_choice:
            res = "".join([random.choice(REAL_4D_FREQUENCIES[f"pos{i+1}"][:4]) for i in range(4)])
        elif "Cold" in strat_choice:
            res = "".join([random.choice(REAL_4D_FREQUENCIES[f"pos{i+1}"][-4:]) for i in range(4)])
        else:
            res = f"{random.randint(0, 9999):04d}"
        st.success(f"Your lucky 4D number is: {res}")
    else:
        if "Hot" in strat_choice:
            nums = sorted(random.sample(REAL_TOTO_HOT, 6))
        elif "Cold" in strat_choice:
            nums = sorted(random.sample(REAL_TOTO_COLD, 6))
        else:
            nums = sorted(random.sample(REAL_TOTO_HOT, 3) + random.sample(REAL_TOTO_COLD, 3))
        st.success(f"Your lucky TOTO numbers are: {' - '.join(map(str, nums))}")

# --- Footer/Donation (Final Robust Version) ---
st.markdown("---")
st.subheader("PLEASE SUPPORT THE DEVELOPER")

# Generate QR
qr_obj = qrcode.make("00020101021126380009SG.PAYNOW010100211+6586789809030115204000053037025802SG5902NA6009Singapore6304ED38")

# Create a BytesIO buffer
buf = io.BytesIO()
qr_obj.save(buf, format='PNG')

# Use seek(0) to ensure the pointer is at the start of the file
buf.seek(0)

# Display using the buffer
st.image(buf, caption="Scan to Donate")
st.write("**Alternatively, donate to PayNow: +65 8678 9809**")
