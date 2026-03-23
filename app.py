import streamlit as st

# Grundinställningar
st.set_page_config(page_title="Monde Bakery Calc", page_icon="🥖")

st.title("🥖 Monde Bakery - Focaccia Kalkylator")

# --- SIDOPANEL ---
st.sidebar.header("Bakningsinställningar")
antal = st.sidebar.number_input("Antal bröd", min_value=1, value=1)
vikt_per_st = st.sidebar.number_input("Vikt per bröd (gram)", min_value=100, value=5002)
pris_per_st = st.sidebar.number_input("Försäljningspris per st (LKR)", value=9000)

st.sidebar.header("Råvarupriser (LKR/kg)")
p_mjol = st.sidebar.number_input("Vetemjöl", value=224.0)
p_salt = st.sidebar.number_input("Salt", value=100.0)
p_olja = st.sidebar.number_input("Olivolja", value=1500.0)

# --- BERÄKNINGAR ---
total_vikt_kg = (antal * vikt_per_st) / 1000

# Recept baserat på Excel-filen
ingredienser = {
    "Vetemjöl": {"%": 0.4655, "pris": p_mjol},
    "Vatten": {"%": 0.3335, "pris": 0.0},
    "Surdeg": {"%": 0.1817, "pris": 0.0},
    "Salt": {"%": 0.0111, "pris": p_salt},
    "Olivolja": {"%": 0.0082, "pris": p_olja}
}

# --- VISA RESULTAT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚖️ Recept")
    total_kostnad = 0
    for namn, info in ingredienser.items():
        vikt = total_vikt_kg * info["%"]
        kostnad = vikt * info["pris"]
        total_kostnad += kostnad
        enhet = "kg" if vikt >= 1 else "g"
        v_visning = vikt if enhet == "kg" else vikt * 1000
        st.write(f"**{namn}:** {v_visning:.2f} {enhet}")

with col2:
    st.subheader("💰 Ekonomi")
    intakt = antal * pris_per_st
    vinst = intakt - total_kostnad
    marginal = (vinst / intakt) * 100 if intakt > 0 else 0
    
    st.metric("Kostnad (Totalt)", f"{total_kostnad:.0f} LKR")
    st.metric("Vinst", f"{vinst:.0f} LKR")
    st.metric("Marginal", f"{marginal:.1f}%")

st.divider()
st.info(f"Degvikt totalt: {total_vikt_kg:.2f} kg")
