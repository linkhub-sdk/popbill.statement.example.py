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
검색조건을 사용하여 전자명세서 목록을 조회합니다.
- 응답항목에 대한 자세한 사항은 "[전자명세서 API 연동매뉴얼] > 3.2.4. Search (목록 조회)" 를 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 문서 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 일자유형, R-등록일시, W-작성일자, I-발행일시 중 택 1
    DType = "W"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20190101"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20190117"

    # 명세서 상태코드, 2,3번째 자리에 와일드카드(*) 사용 가능
    State = ["2**", "3**"]

    # 명세서 종류 코드 배열, 121-명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    ItemCode = ["121", "122", "123", "124", "125", "126"]

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    # 거래처 정보, 거래처 상호 또는 사업자등록번호 기재, 공백처리시 전체조회
    QString = ""

    response = statementService.search(CorpNum, DType, SDate, EDate, State, ItemCode,
                                       Page, PerPage, Order, UserID, QString)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    i = 1
    for info in response.list:
        print("====== 전자명세서 정보 [%d] ======" % i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
