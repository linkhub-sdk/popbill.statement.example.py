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
전자명세서 관련 메일전송 항목에 대한 전송여부를 수정합니다.
- https://developers.popbill.com/reference/statement/python/api/etc#UpdateEmailConfig
"""

try:
    print("=" * 15 + " 전자명세서 메일전송여부 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 메일 전송 유형
    EmailType = "SMT_ISSUE"

    # 전송 여부 (True = 전송, False = 미전송)
    SendYN = True

    result = statementService.updateEmailConfig(CorpNum, EmailType, SendYN)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
