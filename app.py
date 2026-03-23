import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECEPT ---
recipes = {
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, 
            "Rye Flour": 0.0394,
            "Sourdough Starter": 0.1765, 
            "Water": 0.3088, 
            "Salt": 0.0132,
            "Walnuts (Broken)": 0.0650  # Proportion baserad på din kalkylfil
        },
        "hydration": 70,
        "default_weight": 800,
        "instructions": """
        1. **Autolyse & Blandning**: Blanda mjöl (Vete och Råg), vatten och torrjäst (om använd). Låt vila i **40 minuter**. Detta säkerställer att mjölet är helt hydrerat innan salt och surdeg tillsätts. Tillsätt sedan surdeg och salt. Knåda degen i 10 minuter.
        
        2. **Stretch and Fold**: Vid 70% hydrering behövs ingen aggressiv knådning. Gör **3–4 set** under de första 2 timmarna av bulkfermenteringen (med 30 minuters mellanrum). **Tillsätt valnötterna under de första vikningarna** för att fördela dem jämnt utan att förstöra glutenstrukturerna.
        
        3. **Bulkfermentering**: Håll degen vid stabila 24–26°C. Använd **"Poke Test"**: Degen bör öka 30-50% i volym och ha en "jiggly" yta efter 3–4 timmar.
        
        4. **Kalljäsning**: För bäst resultat, låt brödet jäsa i kylskåp i **12–14 timmar**. Detta utvecklar smaken och gör det betydligt enklare att snitta (skapa "scars") i degen.
        
        5. **Bakning & Ånga**: 
           - **Förvärmning**: Ugn och baksten till 250°C.
           - **Bakning**: Sänk till **245°C** när brödet sätts in.
           - **Ånga**: Injicera **15 sekunder ånga** direkt vid start. Grädda i totalt 25–30 minuter.
        """,
        "tips": "Rosta valnötterna lätt innan de blandas i degen för en djupare och mer nötig smak!"
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "hydration": 70,
        "default_weight": 1000,
        "instructions": "Autolys 40 min, tillsätt starter/salt, knåda 10 min. 4 set folds (tillsätt frön här). Kalljäs 12-14h. Baka med hög initial värme.",
        "tips": "Vik in fröna för att inte punktera degen under knådning."
    }
}

# --- SIDEBAR: INSTÄLLNINGAR & KALKYL ---
st.sidebar.header("Inställningar")
selected_name = st.sidebar.selectbox("Välj brödsort", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Antal bröd (st)", min_value=1, value=5)
target_weight = st.sidebar.number_input("Vikt per bröd (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("Ekonomi & Vinst")
raw_cost_per_kg = st.sidebar.number_input("Råvarukostnad (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Försäljningspris (LKR/st)", value=900.0)

# --- BERÄKNINGAR ---
total_batch_kg = (units * target_weight) / 1000
total_cost = total_batch_kg * raw_cost_per_kg * 1.25 # Inkluderar 25% overhead (el/arbete)
total_revenue = units * selling_price
total_profit = total_revenue - total_cost
margin_pct = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0

# Sidebar sammanfattning
st.sidebar.subheader("Finansiell översikt")
st.sidebar.metric("Beräknad Marginal", f"{margin_pct:.1f}%")
st.sidebar.write(f"**Total Intäkt:** {total_revenue:,.0f} LKR")
st.sidebar.write(f"**Total Kostnad:** {total_cost:,.0f} LKR")
st.sidebar.write(f"**Netto Vinst:** {total_profit:,.0f} LKR")

# --- HUVUDDISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Produktionsblad", "Bageri-instruktioner"])
    
    with tab1:
        st.write("### Ingredienser")
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingrediens**")
        h2.write("**Vikt**")
        h3.write("**Procent**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 2])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.2f}%")
            
        st.divider()
        st.metric("Total degvikt", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.write("### Professionell Guide")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Tekniska specifikationer")
    st.metric("Hydrering", f"{recipe['hydration']}%")
    st.metric("Baktemperatur", "245°C")
    st.metric("Ånga", "15 sek")
    
    st.divider()
    st.subheader("Bagarens Tips")
    st.success(recipe["tips"])
    
    
    st.info("💡 **Happy baking—you’re in for a rewarding baker!**")

st.caption("Monde Bakery Digital Handbook | Precision Management")
