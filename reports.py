# -*- coding: utf-8 -*-
"""
reports.py: Plotly kullanarak interaktif görsel raporlar üretir.
Part 4: Gereksiz raporlar kaldırıldı, sadece Bölgesel Analiz Haritası kaldı.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from parties import REGIONS

TEMPLATE = "plotly_dark" # Profesyonel bir görünüm için koyu tema

def generate_regional_analysis_report():
    """Bölgesel Başarı Haritası Simülasyonu."""
    party_name = st.session_state.selected_party_name
    region_names = list(REGIONS.keys())

    # Basit bir oy hesaplama simülasyonu
    # Oy oranı = Bölgedeki doğal çekim + (Partinin genel Kamuoyu Desteği - 50) / 2
    # Bu formül, genel KOD'un bölgesel sonuçları bir miktar etkilemesini sağlar.
    natural_attraction = [REGIONS[r]['natural_attraction'].get(party_name, 10) for r in region_names]
    current_vote_share = [na + (st.session_state.resources['public_support'] - 50) * 0.5 for na in natural_attraction]
    current_vote_share = [max(5, min(95, v)) for v in current_vote_share] # Oy oranını %5-95 arasında tut

    vote_data = pd.DataFrame({'Bölge': region_names, 'Oy Oranı': current_vote_share})

    # Harita görünümü için bölgeleri bir ızgaraya yerleştir
    # Bu sadece görsel bir düzenlemedir, coğrafi doğruluğu yoktur.
    rows = 2
    cols = 5
    vote_data['x'] = [i % cols for i in range(len(region_names))]
    vote_data['y'] = [i // cols for i in range(len(region_names))]

    fig = go.Figure(go.Heatmap(
        z=vote_data['Oy Oranı'],
        x=vote_data['x'],
        y=vote_data['y'],
        customdata=vote_data['Bölge'],
        hovertemplate="<b>%{customdata}</b><br>Tahmini Oy Oranı: %{z:.1f}%<extra></extra>",
        colorscale='Blues',
        showscale=False
    ))

    # Her bir hücreye bölge adını ekle
    annotations = []
    for index, row in vote_data.iterrows():
        annotations.append(
            dict(
                x=row['x'], y=row['y'],
                text=row['Bölge'],
                showarrow=False,
                font=dict(color='white' if row['Oy Oranı'] > 50 else 'black')
            )
        )

    fig.update_layout(
        title='Bölgesel Oy Dağılımı',
        template=TEMPLATE,
        xaxis_showgrid=False, yaxis_showgrid=False,
        xaxis_visible=False, yaxis_visible=False,
        plot_bgcolor='rgba(0,0,0,0)',
        annotations=annotations,
        height=210 # PART 4: Dikey alanı %40 küçült
    )
    return fig
