# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import PopbillException, StatementService

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
전자명세서 관련 메일 항목에 대한 발송설정을 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/etc#ListEmailConfig
"""

try:
    print("=" * 15 + " 전자명세서 메일전송여부 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    EmailConfig = statementService.listEmailConfig(CorpNum)

    for info in EmailConfig:
        if info.emailType == "SMT_ISSUE":
            print(
                "%s(수신자에게 전자명세서가 발행 되었음을 알려주는 메일 전송 여부) : %s"
                % (info.emailType, info.sendYN)
            )
        if info.emailType == "SMT_ACCEPT":
            print(
                "%s(발신자에게 전자명세서가 승인 되었음을 알려주는 메일 전송 여부) : %s"
                % (info.emailType, info.sendYN)
            )
        if info.emailType == "SMT_DENY":
            print(
                "%s(발신자에게 전자명세서가 거부 되었음을 알려주는 메일 전송 여부) : %s"
                % (info.emailType, info.sendYN)
            )
        if info.emailType == "SMT_CANCEL":
            print(
                "%s(수신자에게 전자명세서가 취소 되었음을 알려주는 메일 전송 여부) : %s"
                % (info.emailType, info.sendYN)
            )
        if info.emailType == "SMT_CANCEL_ISSUE":
            print(
                "%s(수신자에게 전자명세서가 발행취소 되었음을 알려주는 메일 전송 여부) : %s"
                % (info.emailType, info.sendYN)
            )

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
