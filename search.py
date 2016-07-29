# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService,PopbillException

statementService =  StatementService(testValue.LinkID,testValue.SecretKey)
statementService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 문서 조회 " + "=" * 15)

    # 일자유형, R-등록일시, W-작성일자, I-발행일시 중 택 1
    DType = "W"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20160601"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20160831"

    # 명세서 상태코드, 2,3번째 자리에 와일드카드(*) 사용 가능
    State = ["2**", "3**"]

    # 명세서 종류 코드 배열, 121-명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    ItemCode = ["121", "122", "123","124", "125", "126"]

    #페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    response = statementService.search(testValue.testCorpNum, DType, SDate, EDate, State, ItemCode, Page, PerPage, Order, testValue.testUserID)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
