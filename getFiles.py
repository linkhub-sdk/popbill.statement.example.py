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
전자명세서에 첨부된 파일의 목록을 확인합니다.
- 응답항목 중 파일아이디(AttachedFile) 항목은 파일삭제(DeleteFile API) 호출시 이용할 수 있습니다.
- https://developers.popbill.com/reference/statement/python/api/etc#GetFiles
"""

try:
    print("=" * 15 + " 전자명세서 첨부파일 목록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    fileList = statementService.getFiles(CorpNum, ItemCode, MgtKey)

    i = 1
    for f in fileList:
        print("%d:" % i)
        print("    serialNum(첨부파일 일련번호) : %s" % f.serialNum)
        print("    attachedFile(파일아이디-첨부파일 삭제시 사용) : %s" % f.attachedFile)
        print("    displayName(첨부파일명) : %s" % f.displayName)
        print("    regDT(첨부일시) : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
