
import streamlit as st
import pandas as pd
from datetime import datetime

# Asetetaan sovelluksen otsikko
st.title("Treeniseuranta & Hyvinvointisovellus")

# Välilehdet: Treenit, Ravinto, Kehonkoostumus
tab1, tab2, tab3 = st.tabs(["Treenipäiväkirja", "Ravintopäiväkirja", "Kehon seuranta"])

# --- TREENIPÄIVÄKIRJA ---
with tab1:
    st.header("Treeniseuranta")

    treenipäivät = ["Työntävät", "Vetävät", "Jalat", "Extra"]
    liikkeet = {
        "Työntävät": ["Penkkipunnerrus", "Vinopenkkipunnerrus käsipainoilla", "Pystypunnerrus käsipainoilla", 
                      "Sivuviparit", "Ranskalainen punnerrus tangolla", "Kapea penkkipunnerrus tai dipit", "Vatsarutistukset"],
        "Vetävät": ["Leuanvedot", "Kulmasoutu tangolla", "Ylätalja tai leuanveto avustuksella", 
                    "Face pull -taljaharjoitus", "Hauiskääntö tangolla", "Hauiskääntö käsipainoilla", "Vatsarutistukset"],
        "Jalat": ["Kyykky", "Suorin jaloin maastaveto", "Reiden ojennus", "Reiden koukistus", 
                  "Pohjenousut seisten", "Vatsarutistukset"],
        "Extra": ["Penkki tai vinopenkki käsipainoilla", "Arnold-punnerrus", "Sivuviparit", 
                  "Hauiskääntö tangolla/käsipainoilla", "Ranskalainen punnerrus taljassa/käsipainolla", 
                  "Dippi tai ojentajapunnerrus taljassa", "Vatsalihasliike"]
    }

    treenipaiva = st.selectbox("Valitse treenipäivä", treenipäivät)
    liike = st.selectbox("Valitse liike", liikkeet[treenipaiva])
    paino = st.number_input("Syötä käytetty paino (kg)", min_value=0.0, step=0.5)
    toistot = st.number_input("Syötä toistojen määrä", min_value=1, step=1)

    if st.button("Tallenna treeni"):
        st.success(f"Tallennettu: {treenipaiva} - {liike} - {paino} kg x {toistot}")

# --- RAVINTOPÄIVÄKIRJA ---
with tab2:
    st.header("Ravintopäiväkirja")
    ateriat = ["Aamiainen", "Lounas", "Päivällinen", "Iltapala", "Välipala"]
    ateria = st.selectbox("Valitse ateria", ateriat)
    ruoka = st.text_input("Syötä syöty ruoka")
    kalorimäärä = st.number_input("Syötä kalorit", min_value=0, step=10)

    if st.button("Tallenna ateria"):
        st.success(f"Tallennettu: {ateria} - {ruoka} - {kalorimäärä} kcal")

# --- KEHON SEURANTA ---
with tab3:
    st.header("Kehon seuranta")
    paino_nyt = st.number_input("Syötä nykyinen paino (kg)", min_value=30.0, step=0.1)
    rasvaprosentti = st.number_input("Syötä rasvaprosentti (%)", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Tallenna kehon tiedot"):
        st.success(f"Tallennettu: Paino {paino_nyt} kg, Rasvaprosentti {rasvaprosentti}%")

# Vinkki käyttäjälle
st.info("Tallenna tiedot ja seuraa kehitystäsi ajan myötä!")
