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

'''
전자명세서 관련 메일전송 항목에 대한 전송여부를 목록으로 반환합니다.
'''

try:
    print("=" * 15 + " 전자명세서 메일전송여부 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    EmailConfig = statementService.listEmailConfig(CorpNum, UserID)

    for info in EmailConfig:
        if info.emailType == "SMT_ISSUE":
            print("%s(공급받는자에게 전자명세서가 발행 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "SMT_ACCEPT":
            print("%s(공급자에게 전자명세서가 승인 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "SMT_DENY":
            print("%s(공급자에게 전자명세서가 거부 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "SMT_CANCEL":
            print("%s(공급받는자에게 전자명세서가 취소 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "SMT_CANCEL_ISSUE":
            print("%s(공급받는자에게 전자명세서가 발행취소 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
