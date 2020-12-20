from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *
from PyQt5.QtTest import *
from config.kiwoomType import *
from config.log_class import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.realType = RealType()
        self.logging = Logging()

        self.logging.logger.debug("Kiwoom() class start.")

        ####### event loop를 실행하기 위한 변수모음
        self.login_event_loop = None #로그인을 이벤트 루프 안에서 실행하도록 만들기 위해 선언한 변수
        #########################################

        ########### 전체 종목 관리
        self.all_stock_dict = {}
        ###########################


        ####### 계좌 관련된 변수
        self.account_stock_dict = {}
        self.not_account_stock_dict = {}
        ########################################

        ######## 종목 정보 가져오기
        self.portfolio_stock_dict = {}
        self.jango_dict = {}
        ########################

        ########### 종목 분석 용
        self.calcul_data = []
        ##########################################


        ####### 요청 스크린 번호
        self.screen_start_stop_real = "1000" #장 시작/종료 실시간 스크린번호
        ########################################

        ######### 초기 셋팅 함수들 바로 실행
        self.get_ocx_instance() #Ocx 방식을 파이썬에 사용할 수 있게 변환해 주는 함수 실행
        self.event_slots() #키움과 연결하기 위한 signal / slot 모음 함수 실행
        self.signal_login_commConnect() #로그인 시도 함수 실행

        self.condition_event_slot()
        self.condition_signal()
        #########################################

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")


    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveMsg.connect(self.msg_slot)


    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def login_slot(self, err_code):

        self.logging.logger.debug(errors(err_code)[1])

        self.login_event_loop.exit()


    def stop_screen_cancel(self, sScrNo=None):
        self.dynamicCall("DisconnectRealData(QString)", sScrNo)

    #송수신 메세지 get
    def msg_slot(self, sScrNo, sRQName, sTrCode, msg):
        self.logging.logger.debug("스크린: %s, 요청이름: %s, tr코드: %s --- %s" %(sScrNo, sRQName, sTrCode, msg))

    #조건검색식 이벤트 모음
    def condition_event_slot(self):
        self.OnReceiveConditionVer.connect(self.condition_slot)
        self.OnReceiveTrCondition.connect(self.condition_tr_slot)
        self.OnReceiveRealCondition.connect(self.condition_real_slot)


    # 어떤 조건식이 있는지 확인
    def condition_slot(self, lRet, sMsg):
        self.logging.logger.debug("호출 성공 여부 %s, 호출결과 메시지 %s" % (lRet, sMsg))

        condition_name_list = self.dynamicCall("GetConditionNameList()")
        self.logging.logger.debug("HTS의 조건검색식 이름 가져오기 %s" % condition_name_list)

        condition_name_list = condition_name_list.split(";")[:-1]

        for unit_condition in condition_name_list:
            index = unit_condition.split("^")[0]
            index = int(index)
            condition_name = unit_condition.split("^")[1]

            self.logging.logger.debug("조건식 분리 번호: %s, 이름: %s" % (index, condition_name))

            ok  = self.dynamicCall("SendCondition(QString, QString, int, int)", "0156", condition_name, index, 1) #조회요청 + 실시간 조회
            self.logging.logger.debug("조회 성공여부 %s " % ok)



    # 조건식 로딩 하기
    def condition_signal(self):
        self.dynamicCall("GetConditionLoad()")

    # 나의 조건식에 해당하는 종목코드 받기
    def condition_tr_slot(self, sScrNo, strCodeList, strConditionName, index, nNext):
        self.logging.logger.debug("화면번호: %s, 종목코드 리스트: %s, 조건식 이름: %s, 조건식 인덱스: %s, 연속조회: %s" % (sScrNo, strCodeList, strConditionName, index, nNext))

        code_list = strCodeList.split(";")[:-1]
        self.logging.logger.debug("코드 종목 \n %s" % code_list)

    # 조건식 실시간으로 받기
    def condition_real_slot(self, strCode, strType, strConditionName, strConditionIndex):
        self.logging.logger.debug("종목코드: %s, 이벤트종류: %s, 조건식이름: %s, 조건명인덱스: %s" % (strCode, strType, strConditionName, strConditionIndex))

        if strType == "I":
            self.logging.logger.debug("종목코드: %s, 종목편입: %s" % (strCode, strType))

        elif strType == "D":
            self.logging.logger.debug("종목코드: %s, 종목이탈: %s" % (strCode, strType))

