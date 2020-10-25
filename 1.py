#우리가 직접 만든 코드 (미완성) - 엑셀 참고
avleadtime = 1
mxleadtime = 2
stock = []
purchase = []
sale = []
purchase_average = []
stock_cycle = []
while True:
    if len(stock) == 0:
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b)
        purchase.append(int(a))
        sale.append(int(b))
        stock.append(c)
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" % (purchase, sale, stock))
        print("최대 판매량 : %s" %(max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))

    elif len(stock) < 3:
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b) + stock[-1]
        stock.append(c)
        purchase.append(int(a))
        sale.append(int(b))
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" %(purchase, sale, stock))
        print("최대 판매량 : %s" % (max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))

    else :
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b) + stock[-1]
        stock.append(c)
        purchase.append(int(a))
        sale.append(int(b))
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" %(purchase, sale, stock))
        #판매량 평균
        d = (sale[-1] + sale[-2] + sale[-3] + sale[-4])/4
        purchase_average.append(d)
        print("판매량 평균 : %s" %purchase_average)

        #재고 주기
        e = stock[-1]/purchase_average[-1]
        stock_cycle.append(round(e,2))
        print("재고주기 : %s" %stock_cycle)
        print("최대 판매량 : %s" % (max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))
        print("안전 재고 주기: %s" %(((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime))/d))