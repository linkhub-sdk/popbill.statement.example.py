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
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
전자명세서 발행시 과금되는 포인트 단가를 확인합니다.
- https://docs.popbill.com/statement/python/api#GetUnitCost
'''

try:
    print("=" * 15 + " 전자명세서 발행단가 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    unitCost = statementService.getUnitCost(CorpNum, ItemCode)

    print("발행단가: %f" % unitCost)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
