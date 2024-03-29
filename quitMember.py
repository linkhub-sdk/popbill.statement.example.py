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
from popbill import StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
가입된 연동회원의 탈퇴를 요청합니다.
- 회원탈퇴 신청과 동시에 팝빌의 모든 서비스 이용이 불가하며, 관리자를 포함한 모든 담당자 계정도 일괄탈퇴 됩니다.
- 회원탈퇴로 삭제된 데이터는 복원이 불가능합니다.
- 관리자 계정만 회원 탈퇴가 가능합니다.
- https://developers.popbill.com/reference/statement/python/api/member#QuitMember
"""

try:
    print("=" * 15 + " 회원 탈퇴 신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 회원 탈퇴 사유
    QuitReason = "회원 탈퇴 예제 입니다."

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    response = statementService.quitMember(CorpNum, QuitReason, UserID)

    print("code (응답 코드) : %s" % response.code)
    print("message (응답 메시지) : %s" % response.message)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
