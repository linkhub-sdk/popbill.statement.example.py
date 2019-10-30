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

'''
전자명세서에 첨부파일을 등록합니다.
- 첨부파일 등록은 전자명세서가 [임시저장] 상태인 경우에만 가능합니다.
- 첨부파일은 최대 5개까지 등록할 수 있습니다.
'''

try:
    print("=" * 15 + " 전자명세서 첨부파일 등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20190124-01"

    # 첨부할 파일의 파일 경로
    FilePath = "test.jpeg"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = statementService.attachFile(CorpNum, ItemCode, MgtKey, FilePath, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
