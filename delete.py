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

'''
1건의 전자명세서를 삭제합니다.
- 전자명세서를 삭제하면 사용된 문서번호(mgtKey)를 재사용할 수 있습니다.
- https://docs.popbill.com/statement/python/api#Delete
'''

try:
    print("=" * 15 + " 전자명세서 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20190117-001"

    result = statementService.delete(CorpNum, ItemCode, MgtKey)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
