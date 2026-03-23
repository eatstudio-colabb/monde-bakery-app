import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES med utförliga instruktioner och hydration ---
recipes = {
    "Artisan Levain French Sourdough": {
        "ingredients": {
            "Wheat Flour": 0.4965, 
            "Water": 0.3308, 
            "Sourdough Starter": 0.1613, 
            "Salt": 0.0114
        },
        "hydration_info": "67% (Standard) - Justera efter mjölets förmåga.",
        "default_weight": 800,
        "instructions": """
        1. **Autolyse & Mix**: Blanda mjöl, vatten och ev. torrjäst först. Låt vila i 40 minuter. Tillsätt sedan surdeg och salt. Knåda degen i 10 minuter. Detta säkerställer att mjölet är fullt hydrerat innan saltet stramar åt glutenet.
        
        2. **Stretch and Fold**: Vid 70% hydration behövs ingen aggressiv knådning. Utför 3–4 set 'stretch and folds' under de första 2 timmarna av bulkfermenteringen med 30 minuters mellanrum.
        
        3. **Bulkfermentering**: Håll degen vid 24–26°C. Lita inte bara på timern; titta efter 30-50% ökning i volym och en "jiggly" yta (ca 3-4 timmar).
        
        4. **Kalljäsning (Rekommenderas)**: Låt degen jäsa i kylskåp i 12-14 timmar. Det ger bättre smak och gör det mycket enklare att snitta (skära skåror) i degen.
        
        5. **Gräddning**: Förvärm ugn och baksten till 250°C. Snitta brödet och skjutsa in i ugnen. Sänk till 245°C.
        
        6. **Ånga**: Injicera 15 sekunder ånga direkt vid start. Använd rikligt med ånga de första 15–20 minuterna för att hålla skorpan mjuk så brödet kan expandera maximalt (maximal oven spring). Grädda totalt 25-30 minuter.
        """,
        "tips": "För ett professionellt 'öra', se till att ugnen är riktigt het och att ångan är tät i början!"
    },
    "Focaccia with Sourdough": {
        "ingredients": {"Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough": 0.1817, "Salt": 0.0111, "Olive Oil": 0.0082},
        "hydration_info": "72%",
        "default_weight": 5002,
        "instructions": "Blanda mjöl, vatten och surdeg. Autolys 30 min. Tillsätt salt/olja. 4 folds. Jäs i form med rikligt med olivolja. Dimpla med fingrarna och baka i 230°C.",
        "tips": "Använd fingertopparna för att skapa djupa hål precis innan gräddning."
    },
    "Baguette with Poolish": {
        "ingredients": {"Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2417, "Salt": 0.0089, "Dry Yeast": 0.0001},
        "hydration_info": "65%",
        "default_weight": 350,
        "instructions": "Gör poolish 12h innan. Blanda degen, vila 45 min. Forma långa baguetter. Snitta 5 gånger omlott. Baka med mycket ånga.",
        "tips": "Vila är nyckeln för att kunna rulla ut baguetterna långa utan att de drar ihop sig."
    },
    "Sourdough Ciabatta": {
        "ingredients": {"Wheat Flour": 0.5389, "Water": 0.4001, "Sourdough": 0.0500, "Salt": 0.0110},
        "hydration_info": "80%+",
        "default_weight": 300,
        "instructions": "Knåda till full glutenutveckling. Coil folds var 30:e minut. Hantera extremt varsamt vid delning för att behålla stora hål.",
        "tips": "Använd mycket mjöl på bänken vid utbakning – degen är mycket kladdig."
    }
}

# --- SIDEBAR ---
st.sidebar.header("Receptinställningar")
selected_name = st.sidebar.selectbox("Välj bröd", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Antal enheter (st)", min_value=1, value=1)
target_weight = st.sidebar.number_input("Vikt per styck (g)", value=recipe["default_weight"])

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000

# --- MAIN DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Ingredienser & Procent", "Bakinstruktioner"])
    
    with tab1:
        st.write("### Produktionsblad")
        # Header
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingrediens**")
        h2.write("**Mängd**")
        h3.write("**% av total deg**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 2])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        st.divider()
        st.info(f"Total degvikt: {total_batch_kg:.2f} kg")

    with tab2:
        st.write("### Steg-för-steg")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Bagar-statistik")
    st.metric("Hydration", recipe["hydration_info"])
    
    st.divider()
    st.subheader("Pro Tips")
    st.success(recipe["tips"])
    
    st.divider()
    st.subheader("Snabbkalkyl")
    price_flour = st.number_input("Mjölpris (LKR/kg)", value=224.0)
    est_cost = total_batch_kg * price_flour * 0.6
    st.write(f"Beräknad råvarukostnad: **{est_cost:.0f} LKR**")

st.caption("Monde Bakery Digital Handbook - Skapad för professionella resultat.")
