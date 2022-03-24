import logging

if __name__ == "__main__":
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO) # DEBUG 출력 안함

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_hander = logging.StreamHandler() # 핸들러 내가 로깅한 정보가 출력되는 위치를 설정
                                            # 콘솔을 통해 설정 했지만 파일, DB, 소켓, 큐등에 다 가능

    stream_hander.setFormatter(formatter) # asctime : 시간
                                          # name : 로거 이름
                                          # levelname : 로깅레벨
                                          # message : 메세지

    mylogger.addHandler(stream_hander)

    file_handler = logging.FileHandler("my.log")
    mylogger.addHandler(file_handler)   # filehandler는 a 모드가 디폴트
                                        # 같은 이름의 파일이 있다면 파일 끝에 추가하여 쓰고, 없으면 쓰기용 파일 만들기

    mylogger.info("server start")