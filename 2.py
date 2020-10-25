import csv
import matplotlib.pyplot as plt

sale_data = [] # 파일을 한번만 읽게 하기 위해서 저장해놓을려고 필요
optimal_weight = 0
min_difference = -1

# 아스키코드의 문제점을 보완하기 위해 유니 코드를 만들었고, 유니 코드를 줄여놓은 것이 유티에프..
with open("sample_data.csv", encoding='utf-8-sig') as data:
    reader = csv.DictReader(data)
    # for row in reader:
    #     price = int(row['price'])
    #     sale_qty = int(row['sale_qty'])
    #     print("sale: %d, price: %d" % (sale_qty, price,))

    # 시각화 그래프로 나타내기
    # for row in reader:
    #     price = int(row['price'])
    #     sale_qty = int(row['sale_qty'])
    #     plt.scatter(price, sale_qty)
    # plt.show()

    # 예측치(판매량) = 입력한 가격 * 가중치
    # 분모의 값이 0이 되는 것을 피해야 함

    # 실행 결과 확인을 위한 데이터 만들기 (가격을 x, 가중치로 구한 값을 y)
    for row in reader:
        price = int(row['price'])
        sale_qty = int(row['sale_qty'])
        sale_data.append({'price': price, 'qty': sale_qty})
        plt.scatter(price, sale_qty)

    for denominator in range(-100,101):
        if denominator == 0:
            continue
        for numerator in range(1, 101):
            weight = numerator / (denominator * 1000)

            sum_difference = 0
            for sale in sale_data:
                estimate_qty = abs(weight * sale.get('price')) # 기울기가 음수가 나오면 안되기 때문에 abs로 감싸줌
                difference = abs(estimate_qty - sale.get('qty'))
                sum_difference += difference

            # min_difference 는 절대로 음수가 나올 수 없음 ( 최적의 값은 무조건 0 이상이 나옴)
            # 하지만 초깃값으로 음수로 넣은 이유는 절대적으로 양수가 나올 것 이기 때문에 음수를 초깃값으로 설정
            # 현재 내가 가지고 있는 값보다 작은 경우 교체를 해주면서 최적의 가중치인것을 판단함
            if min_difference < 0 or min_difference > sum_difference:
                min_difference = sum_difference
                optimal_weight = weight

    # 최적의 값을 구한것을 정확하게 판단하기 위해 시각화로 표현하기 위한 차트 코드 구현
    optimal_xaxis = []
    optimal_yaxis = []
    for price in range(10000, 100000, 1000):
        optimal_xaxis.append(price)
        optimal_yaxis.append(optimal_weight * price)
    print(optimal_weight)

    plt.plot(optimal_xaxis, optimal_yaxis)
    plt.show()