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
발신자가 발행한 전자명세서를 발행취소합니다.
- "발행취소" 상태의 전자명세서를 삭제(Delete API) 함수를 이용하면, 전자명세서 관리를 위해 할당했던 문서번호를 재사용 할 수 있습니다.
- https://developers.popbill.com/reference/statement/python/api/issue#Cancel
"""

try:
    print("=" * 15 + " 전자명세서 발행취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-002"

    # 메모
    Memo = "발행취소 메모"

    result = statementService.cancel(CorpNum, ItemCode, MgtKey, Memo)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
