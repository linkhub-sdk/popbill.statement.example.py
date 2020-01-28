# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
전자명세서 관련 메일전송 항목에 대한 전송여부를 수정합니다.
- https://docs.popbill.com/statement/python/api#UpdateEmailConfig

메일전송유형
SMT_ISSUE : 수신자에게 전자명세서가 발행 되었음을 알려주는 메일입니다.
SMT_ACCEPT : 발신자에게 전자명세서가 승인 되었음을 알려주는 메일입니다.
SMT_DENY : 발신자에게 전자명세서가 거부 되었음을 알려주는 메일입니다.
SMT_CANCEL : 수신자에게 전자명세서가 취소 되었음을 알려주는 메일입니다.
SMT_CANCEL_ISSUE : 수신자에게 전자명세서가 발행취소 되었음을 알려주는 메일입니다.
'''

try:
    print("=" * 15 + " 전자명세서 메일전송여부 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 메일 전송 유형
    EmailType = 'SMT_ISSUE'

    # 전송 여부 (True = 전송, False = 미전송)
    SendYN = True

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = statementService.updateEmailConfig(CorpNum, EmailType, SendYN, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
