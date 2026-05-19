import streamlit as st

st.title("10 AI Business Prompts")
st.subheader("For Restaurants, Clinics & Shops")

category = st.selectbox("Select Business Type", 
                        ["Restaurant", "Clinic", "Shop"])

if category == "Restaurant":
    st.write("**1.** Write a mouth-watering description for Butter Chicken that makes customers want to order immediately. Keep it under 50 words.")
    st.write("**2.** Write a polite WhatsApp reply to a customer complaining about cold food at Royal Spice Restaurant.")
    st.write("**3.** Create a Diwali offer message for Saffron Restaurant offering 20% off on all tandoori items.")
    st.write("**4.** Write 5 engaging Instagram captions for a North Indian restaurant targeting young customers in Jaipur.")

elif category == "Clinic":
    st.write("**1.** Write a professional appointment reminder for patient Rahul Sharma scheduled on 25th May at 10:00 AM.")
    st.write("**2.** Write 5 short daily health tips for a diabetes clinic to post on Instagram.")
    st.write("**3.** Write a polite follow-up message to a patient who missed their appointment on 20th May.")

elif category == "Shop":
    st.write("**1.** Write a compelling product description for Banarasi Silk Saree priced at ₹2,499 for WhatsApp catalogue.")
    st.write("**2.** Create a Diwali sale announcement for Sharma Electronics offering 30% off on all LED TVs.")
    st.write("**3.** Write a thank you message to send customers after purchase from our clothing store in Jaipur.")