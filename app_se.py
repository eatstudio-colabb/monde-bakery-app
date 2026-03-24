app_se.pyimport streamlit as st

st.set_page_config(page_title="Monde Bakery Receptmaster", layout="wide")

# --- ANPASSAD CSS ---
st.markdown("""
    <style>
    h1 { 
        font-weight: 800 !important; 
        color: #FF4B4B !important;
        letter-spacing: -0.5px; 
    }
    
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #0066CC;
        border-radius: 10px;
        background-color: #0066CC;
    }
    
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: white !important;
        font-weight: 600 !important;
        text-transform: uppercase;
    }
    
    div[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
        background-color: white;
        color: black;
        border-radius: 0 0 8px 8px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Monde Bakery - Professionell Receptmaster")

# --- RECEPTDATABAS ---
recipes = {
    "Svenska Kanelbullar": {
        "ingredients": {
            "Deg: Vetemjöl": 0.3350, "Deg: Mjölk": 0.2577, "Deg: Surdeg": 0.1289,
            "Deg: Kallt smör (sist)": 0.0805, "Deg: Socker": 0.0548, "Deg: Kardemumma": 0.0064,
            "Deg: Salt": 0.0045, "Fyllning: Smör": 0.0967, "Fyllning: Socker": 0.0290, "Fyllning: Kanel": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Äggstrykning & Pärlsocker",
        "instructions": "1. Autolys mjölk/mjöl/kardemumma. 2. Blanda i surdeg. 3. Tillsätt salt och kallt tärnat smör sist. 4. Kalljäs 12-14h.",
        "pro_tips": "Kallt smör i tärningar ger bäst textur."
    },
    "Focaccia med Surdeg": {
        "ingredients": {
            "Vetemjöl Special": 0.4655, "Vatten": 0.3292, "Surdegsgrund": 0.1587, 
            "Salt": 0.0132, "Olivolja": 0.0333, "Torrjäst": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Saltlake & Rosmarin",
        "instructions": "1. Autolys. 2. Stretch & Fold 4 ggr. 3. Kalljäs i oljad plåt. 4. Tryck hål med saltlake.",
        "pro_tips": "Saltlaken håller brödet saftigt."
    },
    "Surdegsbröd med Valnötter": {
        "ingredients": {
            "Vetemjöl Special": 0.3971, "Rågmjöl": 0.0394, "Surdegsgrund": 0.1765, 
            "Vatten": 0.3088, "Salt": 0.0132, "Valnötter": 0.0650, "Torrjäst": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "30-35 min", "finish": "Ånga",
        "instructions": "1. Rosta nötter. 2. Autolys. 3. Vik in nötterna vid första vikningen. 4. Kalljäs 12h.",
        "pro_tips": "Rostade nötter ger bättre färg och smak."
    },
    "Monde Multi Grain": {
        "ingredients": {
            "Vetemjöl Special": 0.2947, "Fullkornsvete": 0.0810, "Rågmjöl": 0.0357,
            "Vatten": 0.3051, "Surdegsgrund": 0.1620, "Salt": 0.0162, "Fröblandning": 0.1052
        },
        "hydration": 72, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "Ånga",
        "instructions": "1. Skålla frön. 2. Autolys. 3. Blanda surdeg/salt. 4. Vik in frön. 5. Kalljäs 12h.",
        "pro_tips": "Innertemp 98°C för perfekt resultat."
    },
    "Artisan Fullkornsvete": {
        "ingredients": {
            "Fullkornsvete": 0.3500, "Vetemjöl Special": 0.1000, "Vatten": 0.3500, 
            "Surdegsgrund": 0.1800, "Salt": 0.0120, "Honung/Malt": 0.0080
        },
        "hydration": 80, "default_weight": 850, "bake_temp": "240°C", "bake_time": "40 min", "finish": "Mjölad yta",
        "instructions": "1. 2h Autolys. 2. Blanda surdeg/salt. 3. 4 set vikningar. 4. Kalljäs 12-15h.",
        "pro_tips": "Lång autolys mjukar upp kliet."
    }
}

# --- SIDOMENY ---
st.sidebar.header("Produktionskalkylator")
selected_name = st.sidebar.selectbox("Välj Recept", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Antal Enheter", min_value=1, value=24)
target_weight = st.sidebar.number_input("Målvikt per styck (g)", value=recipe["default_weight"])

st.sidebar.divider()

# VALUTAINSTÄLLNINGAR
st.sidebar.header("Valuta & Ekonomi")
lkr_to_sek = st.sidebar.number_input("Växelkurs (100 LKR = X SEK)", value=3.50) / 100
flour_price_lkr = st.sidebar.number_input("Pris mjöl (LKR/kg)", value=224.0)
selling_price_lkr = st.sidebar.number_input("Försäljningspris (LKR/st)", value=900.0)

# SURDEGSGUIDE
with st.sidebar.expander("📖 SURDEGSGUIDE"):
    st.markdown("Mata 1:1:1. Förvara i kyl. Mata 4-6h innan bak.")

# --- BERÄKNINGAR ---
total_dough_kg = (units * target_weight) / 1000
cost_lkr = (total_dough_kg * flour_price_lkr) * 1.25
revenue_lkr = units * selling_price_lkr
profit_lkr = revenue_lkr - cost_lkr

# Omvandling till SEK
cost_sek = cost_lkr * lkr_to_sek
profit_sek = profit_lkr * lkr_to_sek
revenue_sek = revenue_lkr * lkr_to_sek

# --- HUVUDDISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Produktionsblad", "Process", "Bagar-tips"])
    
    with tab1:
        st.subheader("Ingredienser & Vikt")
        st.write(f"Batch: {units} st x {target_weight}g | **Hydrering: {recipe['hydration']}%**")
        st.markdown("---")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_dough_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
        
        st.markdown("---")
        st.metric("Total Batchvikt", f"{total_dough_kg:.2f} kg")

    with tab2:
        st.write(recipe["instructions"])
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Ekonomi")
    
    # Vinst i båda valutorna
    c1, c2 = st.columns(2)
    c1.metric("Vinst (LKR)", f"{profit_lkr:,.0f}")
    c2.metric("Vinst (SEK)", f"{profit_sek:,.0f}")
    
    st.divider()
    st.write(f"**Kostnad:** {cost_lkr:,.0f} LKR ({cost_sek:,.2f} SEK)")
    st.write(f"**Intäkt:** {revenue_lkr:,.0f} LKR ({revenue_sek:,.2f} SEK)")
    
    st.divider()
    st.info(f"Ugn: {recipe['bake_temp']} | Tid: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
