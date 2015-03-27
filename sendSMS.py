# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService, PopbillException

statementService =  StatementService(testValue.LinkID,testValue.SecretKey)
statementService.IsTest = testValue.IsTest
  
try:
    print("전자명세서 알림문자 전송")
    
    ItemCode = 121 # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    MgtKey = "20150326-01" # 전자명세서 문서관리번호
    Sender = "07075103710" # 발신번호
    Receiver = "010111222" # 수신번호
    Contents = "전자명세서 API 문자메시지 테스트" # 문자메시지내용, 90Byte 초과시 길이가 조정되어 전송됨
    UserID = testValue.testUserID

    result = statementService.sendSMS(testValue.testCorpNum,ItemCode,MgtKey,Sender,Receiver,Contents,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))