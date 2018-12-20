from love_calculator import love_calculator
from people_name import people_name

if __name__ == "__main__":
    print("영어 이름을 대문자로 입력하시오")
    while (1):  ## 무한 루프를 돌린다
        user_name = input()  ## 사용자의 영어이름을 받는다.
        if len(user_name) <= 20 and user_name.isupper() == True:  ## 사용자의 영어이름이 20글자 이하고 전부 대문자면 무한루프를 빠져나간다
            break;
        print("영어 이름을 다시 입력하시오")  ## 만약 20글자초과나 소문자가 포함될 경우 다시 입력을 받는다.
    user = people_name(user_name, len(user_name))  ## user라는 변수에 오민식의 이름과 이름 길이를 넣는다

    print("당신의 이름은", user.name, "입니다")  ## 영어이름 출력
    print("이성의 수를 입력하시오")

    while (1):  ## 무한루프를 돌린다
        other_number = int(input())  ##이성의 수 입력을 받는다
        if other_number <= 50:  ##이성의 수 입력이 50이하면 빠져나가고 50초과면 다시 입력을 받는다
            break;
        print("이성의 수를 다시 입력하시오")

    array = []  ## 이성들을 넣을 빈 배열을 만든다
    for i in range(0, other_number):  ## 이성들의 수만큼 for문을 돌린다
        print("{0} 번째 이성의 이름을 대문자로 입력하시오".format(i + 1))  ## 문자열 안에 변수를 사용하기 위해 format을 사용
        other_name = input()  ## 이성 이름 입력
        while (len(other_name) >= 20 or other_name.isupper() == False):  ##  이름 길이가 20초과 나 소문자가 있을경우
            print("{0} 번째 이성의 이름을 다시 입력하시오".format(i + 1))  ## 재입력을 받는다
            other_name = input()
        other_name = people_name(other_name, len(other_name))  ## 이성의 이름과 길이를 other_name변수에 넣는다
        array.append(other_name)  ## 배열에 이성들을 하나씩 차곡차곡 넣는다
    Max = 0  ## 궁합이 가장 좋은 값을 넣을 변수
    Max_other = 0  ## 궁합이 가장 좋은 이성의 배열 인덱스 번호가 들어갈 변수
    for i in range(0, len(array)):  ## 이성의 수만큼 for문을 돌린다
        L = user.L() + array[i].L()  ## L O V E에는 함수를 사용하여 각 이름의 L O V E를 구하여 나와 이성의 갯수를 더한다.
        O = user.O() + array[i].O()
        V = user.V() + array[i].V()
        E = user.E() + array[i].E()
        love_amount = love_calculator(L, O, V, E)  ## 둘의 LOVE 구한 값을 love_calculator 함수에 넣어 계산을 한다.
        if Max <= love_amount:  ## 만약  love_amount 가 MAX 보다 크거나 같으면 이름을 비교해서 이름이 앞인 것을 배열 인덱스 번호로 해준다
            if (array[Max_other].name > array[i].name):
                Max_otherl = i  ## 궁합이 가장좋은 이성의 배열 인덱스 갱신
            Max = love_amount  ## 궁합이 가장 높은값 갱신
    print(user.name, "는", array[Max_other].name, "와 가장 성공할 확률이 높습니다")  ##가장 궁합이 좋은 이성 출력