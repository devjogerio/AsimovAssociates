import dash
import plotly.express as px
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd

from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from app import app

# ========= Layout ========= #
layout = dbc.Container([
        modal_novo_processo.layout,
        modal_novo_advogado.layout,
        modal_advogados.layout,
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Img(src='/assets/logo.svg', style={'width': '60px', 'marginBottom': '10px'}),
                        html.H1("ADVOG", style={'color': 'var(--primary-color)', 'fontSize': '2.5rem', 'fontWeight': '600', 'marginBottom': '5px'}),
                        html.H3("ASSOCIATES", style={'color': 'var(--text-color)', 'fontSize': '1.2rem', 'fontWeight': '400', 'opacity': '0.8'})
                    ], className='text-center')
                ])
            ])
        ], style={'paddingTop': '30px', 'marginBottom': '20px'}),
        # Theme Switch
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Switch(
                        id='theme-toggle',
                        label=False,
                        value=False,
                        className='custom-switch'
                    ),
                    html.Div([
                        html.I(className="fas fa-sun"),
                        html.I(className="fas fa-moon")
                    ], className='theme-icons')
                ], className='theme-switch text-center')
            ])
        ], style={'marginBottom': '20px'}),
        html.Hr(style={'margin': '20px 0', 'opacity': '0.2'}),
        dbc.Row([
            dbc.Col([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink([
                        html.I(className='fa fa-home', style={'marginRight': '10px'}),
                        "Início"
                    ], href="/home", active=True, className='nav-link-custom')),
                    dbc.NavItem(dbc.NavLink([
                        html.I(className='fa fa-plus-circle', style={'marginRight': '10px'}),
                        "Processos"
                    ], id='processo_button', active=True, className='nav-link-custom')),
                    dbc.NavItem(dbc.NavLink([
                        html.I(className='fa fa-user-plus', style={'marginRight': '10px'}),
                        "Advogados"
                    ], id='lawyers_button', active=True, className='nav-link-custom'))
                ], vertical=True, pills=True, fill=True, className='custom-nav')
            ])
        ]),
        html.Div([
            html.P("© 2025 Advog Associates", style={'color': 'var(--text-color)', 'opacity': '0.6', 'fontSize': '0.8rem'})
        ], className='text-center', style={'position': 'absolute', 'bottom': '20px', 'width': '100%', 'left': '0'})
], style={'height': '100vh', 'padding': '20px', 'position': 'sticky', 'top': 0, 'backgroundColor': 'var(--card-background)', 'boxShadow': '2px 0 10px rgba(0,0,0,0.1)'})    

# ======= Callbacks ======== #
# Toggle Theme
@app.callback(
    Output('body', 'data-theme'),
    Input('theme-toggle', 'value')
)
def toggle_theme(is_dark):
    if is_dark:
        return 'dark'
    return ''

# Abrir Modal New Lawyer
@app.callback(
    Output('modal_new_lawyer', "is_open"),
    Input('new_adv_button', 'n_clicks'),
    Input("cancel_button_novo_advogado", 'n_clicks'),
    State('modal_new_lawyer', "is_open")
)
def toggle_modal(n, n2, is_open):
    if n or n2:
        return not is_open
    return is_open

# Abrir Modal Lawyers
@app.callback(
    Output('modal_lawyers', "is_open"),
    Input('lawyers_button', 'n_clicks'),
    Input('quit_button', 'n_clicks'),
    Input('new_adv_button', 'n_clicks'),
    State('modal_lawyers', "is_open")
)
def toggle_modal(n, n2, n3, is_open):
    if n or n2 or n3:
        return not is_open
    return is_open
