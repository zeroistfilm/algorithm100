from multiprocessing import Process, Queue
import time


def addition_operation(work_id, start, end, result):
    print(f'작업단위 : {work_id}')
    total = 0
    for i in range(start, end):
        total += i
    result.put((work_id,total))
    return

def subtraction_operation(work_id, start, end, result):
    print(f'작업단위 : {work_id}')
    total = 0
    for i in range(start, end):
        total -= i
    result.put((work_id,total))
    return


if __name__ == '__main__':
    result_list = Queue()
    process1 = Process(target=addition_operation, args=(1, 0, 10, result_list))
    process2 = Process(target=subtraction_operation, args=(2, 10, 13, result_list))
    start_time = time.perf_counter()  # 스톱워치랑 같은 개념
    start_time5 = time.process_time()  # 코드 효율성비교는 process_time()함수를 사용하는 것이 유용
    process1.start()
    process2.start()



    total = 0
    while result_list.qsize():
        id, value = result_list.get()
        print(id ,value)
        total += value



    process1.join()
    process2.join()

    print(f"덧셈결과: {total}")
    end_time = time.perf_counter()
    end_time5 = time.process_time()
    print("스톱워치 : 쓰레드 작업 실행시간(초):", end_time - start_time)
    print("코드 효율성비교 : 프로세스 실행시간:", end_time5 - start_time5)