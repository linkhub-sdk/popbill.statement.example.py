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
사업자번호를 조회하여 연동회원 가입여부를 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/member#CheckIsMember
"""

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 조회할 사업자번호
    CorpNum = "1234567890"

    result = statementService.checkIsMember(CorpNum)

    print("가입여부 확인 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
