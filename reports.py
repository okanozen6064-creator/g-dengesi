# -*- coding: utf-8 -*-

"""
reports.py: Plotly kullanarak interaktif görsel raporlar üretir.
Bu fonksiyonlar, Streamlit arayüzünde gösterilmek üzere Plotly Figure nesneleri döndürür.
Koyu tema ve yeni harcama takibi grafiğini içerir.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from parties import REGIONS

TEMPLATE = "plotly_dark" # Profesyonel bir görünüm için koyu tema

def generate_strategic_health_report():
    """Stratejik Sağlık Takibi: 4 temel kaynağın zaman içindeki değişimini gösterir."""
    history = st.session_state.history

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=history['years'], y=history['political_capital'], mode='lines+markers', name='Siyasi Sermaye'))
    fig.add_trace(go.Scatter(x=history['years'], y=history['cohesion'], mode='lines+markers', name='İdeolojik Tutarlılık'))
    fig.add_trace(go.Scatter(x=history['years'], y=history['bureaucratic_efficiency'], mode='lines+markers', name='Bürokratik Verimlilik'))
    fig.add_trace(go.Scatter(x=history['years'], y=history['public_support'], mode='lines+markers', name='Kamuoyu Desteği'))

    fig.update_layout(
        title='Stratejik Sağlık Takibi (Yıllara Göre)',
        xaxis_title='Yıl',
        yaxis_title='Değer (0-100)',
        yaxis_range=[0, 100],
        legend_title="Kaynaklar",
        template=TEMPLATE
    )
    return fig

def generate_regional_analysis_report():
    """Bölgesel Başarı Haritası Simülasyonu."""
    party_name = st.session_state.selected_party_name
    region_names = list(REGIONS.keys())

    natural_attraction = [REGIONS[r]['natural_attraction'][party_name] for r in region_names]
    current_vote_share = [na + (st.session_state.resources['public_support'] - 40) * 0.5 for na in natural_attraction]
    current_vote_share = [max(5, min(95, v)) for v in current_vote_share]

    vote_data = pd.DataFrame({'Bölge': region_names, 'Oy Oranı': current_vote_share})
    vote_data['x'] = [i % 5 for i in range(len(region_names))]
    vote_data['y'] = [i // 5 for i in range(len(region_names))]

    fig = go.Figure(go.Heatmap(
        z=vote_data['Oy Oranı'],
        x=vote_data['x'],
        y=vote_data['y'],
        customdata=vote_data['Bölge'],
        hovertemplate="<b>%{customdata}</b><br>Oy Oranı: %{z:.1f}%<extra></extra>",
        colorscale='Blues',
        showscale=False
    ))

    fig.update_layout(
        title='Bölgesel Oy Dağılımı',
        template=TEMPLATE,
        xaxis_showgrid=False, yaxis_showgrid=False,
        xaxis_visible=False, yaxis_visible=False,
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def generate_spending_report():
    """Yıl içi harcamaları gösteren pasta grafikleri oluşturur."""
    spending = st.session_state.yearly_spending

    ep_labels = list(spending["EP"].keys())
    ep_values = list(spending["EP"].values())

    treasury_labels = list(spending["Treasury"].keys())
    treasury_values = list(spending["Treasury"].values())

    # İki ayrı figür oluştur
    fig_ep = go.Figure(data=[go.Pie(labels=ep_labels, values=ep_values, hole=.3,
                                    hovertemplate="<b>%{label}</b><br>Harcanan EP: %{value}<extra></extra>")])
    fig_ep.update_layout(title_text="Yıllık EP Harcama Dağılımı", template=TEMPLATE)

    fig_treasury = go.Figure(data=[go.Pie(labels=treasury_labels, values=treasury_values, hole=.3,
                                          hovertemplate="<b>%{label}</b><br>Harcanan Bütçe: %{value:,}<extra></extra>")])
    fig_treasury.update_layout(title_text="Yıllık Bütçe Harcama Dağılımı", template=TEMPLATE)

    return fig_ep, fig_treasury
