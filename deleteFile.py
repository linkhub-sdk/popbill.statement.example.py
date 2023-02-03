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
"임시저장" 상태의 전자명세서에 첨부된 1개의 파일을 삭제합니다.
- 파일 식별을 위해 첨부시 부여되는 'FileID'는 첨부파일 목록 확인(GetFiles API) 함수를 호출하여 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/etc#DeleteFile
'''

try:
    print("=" * 15 + " 전자명세서 첨부파일 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    # 삭제할 FileID, 첨부파일목록(getFiles API) 응답 전문의 attachedFile 값
    FileID = "E16A6B30-9C3D-4A8B-80EC-E7B72D2B7AEE.PBF"

    result = statementService.deleteFile(CorpNum, ItemCode, MgtKey, FileID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
