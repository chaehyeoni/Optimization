# 정식 코드
stock_history = []
max_sell = 0
max_lead = 2
average_lead = 1
safe_stock = 0
safe_period = 0

while True:
    buy = int(input("Input buy amount : "))
    sell = int(input("Input sell amount : "))
    remain = 0
    past_stocks = stock_history[-3:]
    item_count = len(past_stocks) + 1
    sell_average = 0
    last_stock = 0
    total_sell = sell
    # 이전값 불러오기
    for past in past_stocks:
        total_sell = total_sell + past['sell']
        last_stock = past['stock']
    # 평균 및 최대 판매량 구하기
    sell_average = total_sell // item_count
    if max_sell < sell:
        max_sell = sell
    # 재고량, 안전 재고 정보 구하기
    if len(stock_history) == 0:
        remain = buy - sell
        last_stock = remain
    else:
        remain = buy - sell + last_stock

    stock_period = remain / sell_average
    safe_stock = round(max_sell* max_lead - sell_average * average_lead)
    safe_period = round(safe_stock / sell_average, 1)
    # 추천 구매량 구하기 (예측) - 음수일때는 0으로 바꿔준다
    buy_recommend = round(safe_period * sell_average - last_stock + sell)
    if buy_recommend < 0:
        buy_recommend = 0
    # 과거 정보 기록하기
    stock = {
        'buy' : buy,
        'sell' : sell,
        'stock' : stock,
        'stock_peroid' : stock_period,
    }
    stock_history.append(stock)
    # 계산 된 결과 출력
    print("구매랑 : %d" % (buy,))
    print("판매 : %d" % (sell,))
    print("평균 판매 : %d" % (sell_average,))
    print("재고 : %d" % (remain,))
    print("재고주기 : %f" % (stock_period,))
    print("안전 재고 : %d" % (safe_stock,))
    print("안전 재고 주기 : %f" % (safe_period,))
    print("추천 구매량 : %d" % (buy_recommend,))