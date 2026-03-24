import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

st.title("Monde Bakery - Professional Recipe Master")

# --- NY SEKTION: SKÖTSEL AV SURDEG ---
with st.expander("KLICKA HÄR: Hur du sköter om din surdeg (Sourdough Care Guide)"):
    st.subheader("Professional Sourdough Care Guide")
    st.write("""
    **1. Vad är en surdegsstart?**
    En surdeg är en levande kultur av vildjäst (som får brödet att höja sig) och mjölksyrabakterier (som ger smak och syra). Den hålls vid liv genom att man regelbundet "matar" den med färskt mjöl och vatten.

    **2. Daglig skötsel (Om du bakar ofta)**
    Mata din start 1-2 gånger per dag vid rumstemperatur. 
    * *Exempel:* 50g start + 50g vatten + 50g mjöl.
    * Den är redo när den fördubblat sin volym, bubblar aktivt och doftar friskt syrligt (ca 4-8 timmar).

    **3. Förvaring i kylskåp (Om du bakar sällan)**
    * Förvara starten i kylskåp och mata den en gång i veckan.
    * *Veckomatning:* Ta ut starten, släng allt utom ca 1 kg. Mata med 2 kg vatten och 2 kg mjöl. Låt stå framme 1-2 timmar innan den åker in i kylen igen.

    **4. Innan bakning**
    Ta ut starten från kylen och mata den (t.ex. 1kg vatten + 1kg mjöl). Låt stå 4-6 timmar tills den når sin topp. För extra styrka, mata den två gånger innan bakning.

    **5. Vilket mjöl ska jag använda?**
    Vete, fullkornsvete eller rågmjöl fungerar. En liten mängd råg- eller fullkornsmjöl gör ofta starten mer aktiv tack vare mer näring.

    **6. Tecken på en hälsosam surdeg**
    * Doftar fruktigt, som yoghurt eller behagligt surt.
    * Bubblar aktivt och fördubblar sin volym.

    **7. Problem & Lösningar**
    * *Doftar aceton/alkohol:* Starten är hungrig, mata den oftare.
    * *Vätska på toppen (Hooch):* Normalt när den är hungrig. Häll av eller rör ner och mata direkt.
    * *Svag jäsning:* Mata den flera gånger i rad i rumstemperatur.

    **8. Temperatur**
    * 24-26°C är idealiskt för vetesurdeg. Vid 28°C+ går det väldigt snabbt och blir surare.
    """)

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            # Deg (Baserat på originalfilens proportioner)
            "Dough: Wheat Flour": 0.3350,
            "Dough: Milk": 0.2577,
            "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter": 0.0805,
            "Dough: Sugar": 0.0548,
            "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045,
            # Fyllning
            "Filling: Butter": 0.0967,
            "Filling: Sugar": 0.0290,
            "Filling: Cinnamon": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": """
        1. Autolyse: Mix milk, cardamom, sugar and flour. Knead 2-3 min. Rest 30 min.
        2. Mix: Add sourdough starter and knead 10 min. 
        3. Salt: Add salt and knead 3 more min.
        4. Filling: Mix softened butter, sugar, and cinnamon.
        5. Shape: Roll, spread filling, fold in three. Cut strips and twist into knots.
        6. Proof: Cold proof in fridge for 12 hours.
        7. Bake: Brush with egg wash + milk. Sprinkle pearl sugar.
        """,
        "pro_tips": """
        ### Deep Dive: Professional Cinnamon Bun Tips
        * **The Cold Milk Secret:** Always use cold milk. The friction during long kneading generates heat; cold milk prevents the dough from getting too warm and weakening the gluten.
        * **Knot Tension:** Do not pull too hard when twisting. If the knot is too tight, the center will pop out like a volcano in the oven instead of expanding evenly.
        * **Fermentation Peak:** The 12-hour cold proof develops lactic acid, resulting in superior caramelization and crust color.
        * **The Egg Wash Shine:** Whisk egg with a pinch of salt and milk. Let it sit for 10 min before brushing to break down proteins for a smoother, professional shine.
        * **Internal Temp:** Take them out at 92-94°C internal temperature to ensure they stay moist.
        """
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt (10m). 3-4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "The Brine Secret: Mix water, olive oil, and salt. Pour into dimples before baking."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt. Stretch & Fold. Cold proof 12-14h.",
        "pro_tips": "Bake until internal temp reaches 98°C."
    }
}

# --- SIDEBAR: CALCULATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Ingredient Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Amount (g per unit)", min_value=0, value=0)

st.sidebar.divider()
st.sidebar.header("Economics (LKR)")
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (per kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
total_custom_kg = (units * custom_ing_amount) / 1000
total_dough_mass = total_batch_kg + total_custom_kg

# --- MAIN DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Core Process", "Pro Tips"])
    
    with tab1:
        st.subheader("Full Ingredients Breakdown")
        st.write(f"Calculating for {units} units at {target_weight}g each.")
        
        st.markdown("---")
        c1, c2, c3 = st.columns([3, 2, 1])
        c1.write("**Ingredient Name**")
        c2.write("**Required Weight**")
        c3.write("**Ratio**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(ing)
            r2.write(f"**{display_val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        if custom_ing_amount > 0:
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(custom_ing_name)
            c_unit = "kg" if total_custom_kg >= 1 else "g"
            c_val = total_custom_kg if c_unit == "kg" else total_custom_kg * 1000
            r2.write(f"**{c_val:.2f} {c_unit}**")
            r3.write("Extra")

        st.markdown("---")
        st.metric("Total Batch Dough Weight", f"{total_dough_mass:.2f} kg")

    with tab2:
        st.subheader("Step-by-Step Guide")
        st.write(recipe["instructions"])
        
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"Oven Temp: {recipe['bake_temp']}")
    st.info(f"Time: {recipe['bake_time']}")
    st.info(f"Steam/Finish: {recipe['steam']}")
    
    st.divider()
    total_cost = total_dough_mass * raw_cost_per_kg * 1.25
    total_revenue = units * selling_price
    total_profit = total_revenue - total_cost
    
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Total Revenue: {total_revenue:,.0f} LKR")
    st.write(f"Est. Production Cost: {total_cost:,.0f} LKR")

st.caption("Monde Bakery Digital Handbook | 2026")
