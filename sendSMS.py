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
알림문자를 전송합니다. (단문/SMS- 한글 최대 45자)
- 알림문자 전송시 포인트가 차감됩니다. (전송실패시 환불처리)
- 전송내역 확인은 "팝빌 로그인" > [문자 팩스] > [문자] > [전송내역] 탭에서 전송결과를 확인할 수 있습니다
'''

try:
    print("=" * 15 + " 전자명세서 알림문자 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20190117-001"

    # 발신번호
    Sender = "07043042991"

    # 수신번호
    Receiver = "010111222"

    # 문자메시지내용, 90Byte 초과시 길이가 조정되어 전송됨
    Contents = "전자명세서 API 문자메시지 테스트"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = statementService.sendSMS(CorpNum, ItemCode, MgtKey, Sender, Receiver, Contents, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
