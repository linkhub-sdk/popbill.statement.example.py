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
"임시저장" 상태의 전자명세서를 발행하여, "발행완료" 상태로 처리합니다.
- 팝빌 사이트 [전자명세서] > [환경설정] > [전자명세서 관리] 메뉴의 발행시 자동승인 옵션 설정을 통해
  전자명세서를 "발행완료" 상태가 아닌 "승인대기" 상태로 발행 처리 할 수 있습니다.
- 전자명세서 발행 함수 호출시 수신자에게 발행 안내 메일이 발송됩니다.
- https://developers.popbill.com/reference/statement/python/api/issue#Issue
"""

try:
    print("=" * 15 + " 전자명세서 발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    # 전자명세서 발행 안내메일 제목
    # ※ 미입력시 팝빌에서 지정한 이메일 제목으로 전송
    EmailSubject = ""

    result = statementService.issue(
        CorpNum, ItemCode, MgtKey, EmailSubject=EmailSubject
    )

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
