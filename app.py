
from flask import Flask, request, jsonify

app = Flask(__name__)

# 종목 리스트를 저장하는 간단한 메모리 구조 (운영시 파일저장 또는 DB확장 가능)
watchlist = []

@app.route('/add_stock', methods=['POST'])
def add_stock():
    data = request.get_json()
    stock_info = {
        "name": data.get("name"),
        "buy_price": data.get("buy_price"),
        "cut_loss_price": data.get("cut_loss_price"),
        "target_price": data.get("target_price"),
        "entry_date": data.get("entry_date")
    }
    watchlist.append(stock_info)
    return jsonify({"message": "Stock added successfully", "current_watchlist": watchlist})

@app.route('/')
def home():
    return "혼합투자 감시 서버 정상 작동 중!"


    
