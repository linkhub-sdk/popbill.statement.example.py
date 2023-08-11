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
"임시저장" 상태의 명세서에 1개의 파일을 첨부합니다. (최대 5개)
- https://developers.popbill.com/reference/statement/python/api/etc#AttachFile
"""

try:
    print("=" * 15 + " 전자명세서 첨부파일 등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    # 첨부할 파일의 파일 경로
    FilePath = "test.jpeg"

    # 첨부파일명
    DisplayName = "Dispay.jpeg"

    result = statementService.attachFile(CorpNum, ItemCode, MgtKey, FilePath, None, DisplayName)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
