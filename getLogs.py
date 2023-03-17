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
전자명세서의 상태에 대한 변경이력을 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/info#GetLogs
"""

try:
    print("=" * 15 + " 전자명세서 상태변경 이력 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    LogList = statementService.getLogs(CorpNum, ItemCode, MgtKey)

    i = 1
    for f in LogList:
        print("상태변경 로그 [%d]" % i)
        print("    docLogType(로그타입) : %s" % f.docLogType)
        print("    log(이력정보) : %s" % f.log)
        print("    procType(처리형태) : %s" % f.procType)
        print("    procCorpName(처리담당자) : %s" % f.procCorpName)
        print("    procMemo(처리메모) : %s" % f.procMemo)
        print("    regDT(등록일시) : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
