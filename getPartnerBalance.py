# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
파트너의 잔여포인트를 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/point#GetPartnerBalance
"""

try:
    print("=" * 15 + " 파트너 잔여포인트 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    balance = statementService.getPartnerBalance(CorpNum)

    print("파트너 잔여포인트 : %d" % balance)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
