# 쓰레드란 
# 프로그램의 실행 흐름 
# 하나의 프로세스 안에 여러개의 쓰래드를 만들수 있다
# 프로세스는 메모리에 할당되어 있는 한 개의 프로그램 의미
# 프로그램 안에서 여러개의 프로세스를 운영할수 없다 --> 프로그램은 하나의 프로세스
# 한 개의 프로세스에서 여러 개의 쓰레드를 가지는 병렬 처리 방식
# 프로세스가 부여된 자원을 이용하면 같은 프로세스 내에서 여러 쓰레드 들 끼리 자원을 공유할수 있다.

# import time

# if __name__ == "__main__":
    
#     increased_num = 0

#     start_time = time.time()
#     for i in range(100000000):
#         increased_num += 1

#     print("--- %s seconds ---" % (time.time() - start_time))

#     print("increased_num=",end=""), print(increased_num)
#     print("end of main") 
# 오초 걸림

# import threading
# import time

# shared_number = 0

# def thread_1(number):
#     global shared_number
#     print("number = ",end=""), print(number)
    
#     for i in range(number):
#         shared_number += 1

# def thread_2(number):
#     global shared_number
#     print("number = ",end=""), print(number)
    
#     for i in range(number):
#         shared_number += 1


# if __name__ == "__main__":

#     threads = [ ]

#     start_time = time.time()
#     t1 = threading.Thread( target= thread_1, args=(50000000,) )
#     t1.start()
#     threads.append(t1)

#     t2 = threading.Thread( target= thread_2, args=(50000000,) )
#     t2.start()
#     threads.append(t2)


#     for t in threads:
#         t.join()

#     print("--- %s seconds ---" % (time.time() - start_time))

#     print("shared_number=",end=""), print(shared_number)
#     print("end of main")
# 속도가 전반적으로 줄었지만(3초), shared_number는 1억이 아닌 이상한 값이 나옴
# 이유 같은 변수를 동시에 접근했기 때문
# 전역 변수로 shared_number가 0으로 초기화 되어 있고 thread_1 과 thread_2가 동시에 shared_number를 늘리는 방식이면
# thread_1 에서 shared_number(0) + 1 로 레지스터 값이 1로 바뀌엇고 이를 shared_number에 저장해서 shared_number가 1로 값이 변경되었습니다.
# 그 다음 thread_2에서 같은 과정을 진행한다고 하면 똑같이 sheard_number(0) + 1로
# 레지스터 값이 1로 바뀌고 다시 shared_number에 저장하니까
# 최종적으로는 shared_number가 1로 유지가 된것입니다.

# # 이를 해결하기 'Lock'을 이용해서 쓰레드를 동기화합니다.
# Lock은 python threading패키지에서 지원합니다.

# lock을 acquire하면 해당 쓰레드만 공유 데이터에 접근할 수 있고, lock을 release 해야만
# 다른 쓰레드에서 공유 데이터에 접근할 수 있습니다.
import threading
import time

shared_number = 0
lock = threading.Lock() # threading에서 Lock 함수 가져오기

def thread_1(number):
    global shared_number
    print("number = ",end=""), print(number)
    
    lock.acquire() # 작업이 끝나기 전까지 다른 쓰레드가 공유데이터 접근을 금지
    for i in range(number):
        shared_number += 1
    lock.release() # lock 해제

def thread_2(number):
    global shared_number
    print("number = ",end=""), print(number)

    lock.acquire() # thread_2 잠금
    for i in range(number):
        shared_number += 1
    lock.release() # thread_2 해제

if __name__ == "__main__":

    threads = [ ]

    start_time = time.time()
    t1 = threading.Thread( target= thread_1, args=(50000000,) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(50000000,) )
    t2.start()
    threads.append(t2)

    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")