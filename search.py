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
검색조건을 사용하여 전자명세서 목록을 조회합니다. (조회기간 단위 : 최대 6개월)
- https://developers.popbill.com/reference/statement/python/api/info#Search
"""

try:
    print("=" * 15 + " 문서 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 일자유형, R-등록일시, W-작성일자, I-발행일시 중 택 1
    DType = "W"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20220701"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20220731"

    # 전자명세서 상태코드 배열 (2,3번째 자리에 와일드카드(*) 사용 가능)
    # - 미입력시 전체조회
    State = ["2**", "3**"]

    # 전자명세서 문서유형 배열 (121 , 122 , 123 , 124 , 125 , 126 중 선택. 다중 선택 가능)
    # 121 = 명세서 , 122 = 청구서 , 123 = 견적서
    # 124 = 발주서 , 125 = 입금표 , 126 = 영수증
    ItemCode = ["121", "122", "123", "124", "125", "126"]

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    # 통합검색어, 거래처 상호명 또는 거래처 사업자번호로 조회
    # - 미입력시 전체조회
    QString = ""

    response = statementService.search(
        CorpNum,
        DType,
        SDate,
        EDate,
        State,
        ItemCode,
        Page,
        PerPage,
        Order,
        UserID,
        QString,
    )

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for info in response.list:
        print("====== 전자명세서 정보 ======")
        print("itemCode (문서종류코드) : %s" % info.itemCode)
        print("itemkey (팝빌번호) : %s" % info.itemKey)
        print("invoiceNum (팝빌승인번호) : %s" % info.invoiceNum)
        print("mgtKey (문서번호) : %s" % info.mgtKey)
        print("taxType (세금형태) : %s" % info.taxType)
        print("writeDate (작성일자) : %s" % info.writeDate)
        print("regDT (임시저장일시) : %s" % info.regDT)
        print("senderCorpName (발신자 상호) : %s" % info.senderCorpName)
        print("senderCorpNum (발신자 사업자등록번호) : %s" % info.senderCorpNum)
        print("senderPrintYN (발신자 인쇄여부) : %s" % info.senderPrintYN)
        print("receiverCorpName (수신자 상호) : %s" % info.receiverCorpName)
        print("receiverCorpNum (수신자 사업자등록번호) : %s" % info.receiverCorpNum)
        print("receiverPrintYN (수신자 인쇄여부) : %s" % info.receiverPrintYN)
        print("supplyCostTotal (공급가액 합계) : %s" % info.supplyCostTotal)
        print("taxTotal (세액 합계) : %s" % info.taxTotal)
        print("purposeType (영수/청구) : %s" % info.purposeType)
        print("issueDT (발행일시) : %s" % info.issueDT)
        print("stateCode (상태코드) : %s" % info.stateCode)
        print("stateDT (상태 변경일시) : %s" % info.stateDT)
        print("stateMemo (상태메모) : %s" % info.stateMemo)
        print("openYN (개봉 여부) : %s" % info.openYN)
        print("openDT (개봉 일시) : %s" % info.openDT + "\n")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
