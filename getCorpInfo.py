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
연동회원의 회사정보를 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/member#GetCorpInfo
"""

try:
    print("=" * 15 + " 회사정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    response = statementService.getCorpInfo(CorpNum)

    tmp = "ceoname(대표자성명) : " + response.ceoname + "\n"
    tmp += "corpName(상호) : " + response.corpName + "\n"
    tmp += "addr(주소) : " + response.addr + "\n"
    tmp += "bizType(업태) : " + response.bizType + "\n"
    tmp += "bizClass(종목) : " + response.bizClass

    print(tmp)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
