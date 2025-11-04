# -*- coding: utf-8 -*-

"""
reports.py: Plotly kullanarak interaktif görsel raporlar üretir.
Bu fonksiyonlar, Streamlit arayüzünde gösterilmek üzere Plotly Figure nesneleri döndürür.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from parties import REGIONS

def generate_strategic_health_report():
    """
    Stratejik Sağlık Takibi: 4 temel kaynağın zaman içindeki değişimini gösteren
    interaktif bir Plotly çizgi grafiği oluşturur.
    """
    history = st.session_state.history

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=history['turns'], y=history['political_capital'],
                             mode='lines+markers', name='Siyasi Sermaye'))
    fig.add_trace(go.Scatter(x=history['turns'], y=history['cohesion'],
                             mode='lines+markers', name='İdeolojik Tutarlılık'))
    fig.add_trace(go.Scatter(x=history['turns'], y=history['bureaucratic_efficiency'],
                             mode='lines+markers', name='Bürokratik Verimlilik'))
    fig.add_trace(go.Scatter(x=history['turns'], y=history['public_support'],
                             mode='lines+markers', name='Kamuoyu Desteği'))

    fig.update_layout(
        title='Stratejik Sağlık Takibi',
        xaxis_title='Tur',
        yaxis_title='Değer (0-100)',
        yaxis_range=[0,100],
        legend_title="Kaynaklar",
        template="plotly_white"
    )

    return fig

def generate_regional_analysis_report():
    """
    Bölgesel Başarı Haritası Simülasyonu: Bölgelerdeki oy oranını gösteren
    interaktif bir ısı haritası/blok grafiği oluşturur.
    """
    party_name = st.session_state.selected_party_name
    region_names = list(REGIONS.keys())

    # Mevcut oy oranını temsili olarak hesapla
    natural_attraction = [REGIONS[r]['natural_attraction'][party_name] for r in region_names]
    current_vote_share = [na + (st.session_state.resources['public_support'] - 50) / 5 for na in natural_attraction]
    current_vote_share = [max(5, min(95, v)) for v in current_vote_share]

    # Bölgeleri bir ızgaraya yerleştir (2x5 düzeni)
    grid_rows = 2
    grid_cols = 5

    # Verileri ve metinleri ızgara formatına getir
    vote_grid = np.full((grid_rows, grid_cols), np.nan) # Boş hücreler için NaN
    text_grid = np.empty((grid_rows, grid_cols), dtype=object)

    for i, (name, vote) in enumerate(zip(region_names, current_vote_share)):
        row = i // grid_cols
        col = i % grid_cols
        vote_grid[row, col] = vote
        text_grid[row, col] = f"{name}<br>Oy Oranı: {vote:.1f}%"

    fig = go.Figure(data=go.Heatmap(
        z=vote_grid,
        text=text_grid,
        hoverinfo='text',
        colorscale='Viridis', # Renk skalası (Yeşil-Sarı-Mavi)
        showscale=True,
        zmin=0,
        zmax=100,
        colorbar={'title': 'Oy Oranı'}
    ))

    fig.update_layout(
        title='Bölgesel Başarı Haritası',
        xaxis_showgrid=False, yaxis_showgrid=False,
        xaxis_ticks='', yaxis_ticks='',
        xaxis_tickvals=[], yaxis_tickvals=[],
        plot_bgcolor='rgba(0,0,0,0)' # Arka planı transparan yap
    )

    # Eksen etiketlerini kaldır
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)

    return fig
