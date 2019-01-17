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

'''
전자명세서에 첨부된 파일을 삭제합니다.
- 파일을 식별하는 파일아이디는 첨부파일 목록(GetFileList API) 의 응답항목
  중 파일아이디(AttachedFile) 값을 통해 확인할 수 있습니다.
'''

try:
    print("=" * 15 + " 전자명세서 첨부파일 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서관리번호
    MgtKey = "20190117-001"

    # 삭제할 FileID, 첨부파일목록(getFiles API) 응답 전문의 attachedFile 값
    FileID = "4DB71521-DC61-43EB-A061-DB0987ABACAB.PBF"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = statementService.deleteFile(CorpNum, ItemCode, MgtKey, FileID, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
