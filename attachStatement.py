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
하나의 전자명세서에 다른 전자명세서 1건을 첨부합니다.
- https://developers.popbill.com/reference/statement/python/api/etc#AttachStatement
"""

try:
    print("=" * 15 + " 다른 전자명세서 첨부 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 전자명세서 종류코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = "121"

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    # 첨부할 전자명세서 종류코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    SubItemCode = "121"

    # 첨부할 전자명세서 문서번호
    SubMgtKey = "20220803-002"

    result = statementService.attachStatement(
        CorpNum, ItemCode, MgtKey, SubItemCode, SubMgtKey
    )

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
