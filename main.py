from fastapi import FastAPI
import yfinance as yf
import plotly.express as px
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import json

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World! We are ODA!"


@app.get("/{ticker}", response_class=JSONResponse)
async def get_data(ticker):
    data = json.loads(yf.download(tickers=ticker, period='max', interval='1d').to_json())
    return JSONResponse(content=data)


@app.get("/{ticker}/dash/{column}", response_class=HTMLResponse)
async def get_dash(ticker, column):
    df = yf.download(tickers=ticker, period='max', interval='1d')
    fig = px.line(df, x=df.index, y=column, title=column)
    return fig.to_html()
