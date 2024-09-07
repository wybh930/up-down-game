import random

min_try = 0

while True:
    answer_number = random.randint(1, 100)

    count = 0

    
    print('Up & Down 게임을 시작하겠습니다. 1~100 사이의 숫자를 맞춰주세요! ==>>')
    
    while True:
        count = count + 1
      
        print(f"# {count}번째 시도")

        try:
            my_guess = int(input('숫자 입력 : '))
            if my_guess > 100 or my_guess < 1:
                print('입력 범위가 아닙니다.')
                continue
            if answer_number == my_guess:
                print('---------------------------------------')
                print("정답입니다.")
                print(f"{count}번 만에 맞췄습니다!")
                if count <= min_try:
                    min_try = count
                    print('---------------------------------------')
                    print(f"최저 시도 기록 : {min_try}번")
                else:
                    print('---------------------------------------')
                    print(f"최저 시도 기록 : {count}번")
                break
            elif answer_number > my_guess:
                print("UP!!!!")
            else:
                print("DOWN!!!!")
        except ValueError:
            print('정수로 입력해주세요.')
    
    will_continue = input('한 판 더 하시겠습니까? (YES/NO) ')

    if will_continue.upper() == 'YES':
        continue
    else:
        print('---------------------------------------')
        print(f"최저 시도 기록 : {count}번")
        break


