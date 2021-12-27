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

from popbill import Statement, StatementDetail, StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
팝빌에 등록하지 않고 전자명세서를 팩스전송합니다.
- 팩스 전송 요청시 포인트가 차감됩니다. (전송실패시 환불처리)
- 전송내역 확인은 "팝빌" > [문자 팩스] > [팩스] > [전송내역] 메뉴에서 전송결과를 확인할 수 있습니다.
- https://docs.popbill.com/statement/python/api#FAXSend
'''

try:
    print("=" * 15 + " 선팩스 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팩스발신번호
    SendNum = "070-4304-2991"

    # 팩스수신번호
    ReceiveNum = "070-111-222"

    # 전자명세서 문서번호
    mgtKey = "20210429-001"

    # 전자명세서 정보
    statement = Statement(
        # 작성일자 yyyyMMdd
        writeDate="20210429",

        # '영수'/'청구' 중 기재
        purposeType="영수",

        # 과세형태, '과세'/'영세'/'면세' 중 기재
        taxType="과세",

        # 맞춤양식코드, 미기재시 기본양식으로 처리
        formCode="",

        # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
        itemCode=121,

        # 전자명세서 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 발신자별 고유번호 생성
        mgtKey=mgtKey,

        # 발신자 사업자번호, '-' 제외 10자리
        senderCorpNum=CorpNum,

        # 발신자 상호
        senderCorpName="발신자 상호",

        # 발신자 주소
        senderAddr="발신자 주소",

        # 발신자 대표자 성명
        senderCEOName="발신자 대표자 성명",

        # 발신자 종사업장 식별번호, 필요시 4자리 숫자값 기재
        senderTaxRegID="",

        # 발신자 종목
        senderBizClass="종목",

        # 발신자 업태
        senderBizType="업태",

        # 발신자 담당자 성명
        senderContactName="발신자 담당자명",

        # 발신자 메일주소
        senderEmail="test@test.com",

        # 발신자 연락처
        senderTEL="070-4304-2991",

        # 발신자 휴대폰번호
        senderHP="010-000-222",

        # 수신자 사업자번호, '-' 제외 10자리
        receiverCorpNum="8888888888",

        # 수신자 상호
        receiverCorpName="수신자 상호",

        # 수신자 대표자 성명
        receiverCEOName="수신자 대표자 성명",

        # 수신자 주소
        receiverAddr="수신자 주소",

        # 수신자 종사업장식별번호, 필요시 4자리 숫자값 기재
        receiverTaxRegID="",

        # 수신자 종목
        receiverBizClass="수신자 종목",

        # 수신자 업태
        receiverBizType="수신자 업태",

        # 수신자 담당자 성명
        receiverContactName="수신자 담당자명",

        # 수신자  메일주소
        receiverEmail="test@test.com",

        # 수신자 연락처
        receiverTEL="070111222",

        # 수신자 휴대폰번호
        receiverHP="010-111-222",

        # 공급가액 합계
        supplyCostTotal="20000",

        # 세액 합계
        taxTotal="2000",

        # 합계금액, 공금가액 합계 + 세액 합계
        totalAmount="22000",

        # 기재 상 '일련번호' 항목
        serialNum="123",

        # 기재 상 '비고' 항목
        remark1="비고1",
        remark2="비고2",
        remark3="비고3",

        # 사업자등록증 이미지 첨부 여부
        businessLicenseYN=False,

        # 통장사본 이미지 첨부 여부
        bankBookYN=False,
    )

    # 상세항목(품목) 정보 (배열 길이 제한 없음)
    statement.detailList = []

    statement.detailList.append(
        StatementDetail(
            serialNum=1,  # 일련번호, 1부터 순차기재
            itemName="품목1",  # 품목
            purchaseDT="20210429",  # 거래일자
            spec="BOX",  # 규격
            unitCost="10000",  # 단가
            qty=1,  # 수량
            supplyCost="10000",  # 공급가액
            tax="1000"  # 세액
        )
    )
    statement.detailList.append(
        StatementDetail(
            serialNum=2,  # 일련번호, 1부터 순차기재
            itemName="품목1",  # 품목
            purchaseDT="20210429",  # 거래일자
            spec="BOX",  # 규격
            unitCost="10000",  # 단가
            qty=1,  # 수량
            supplyCost="10000",  # 공급가액
            tax="1000"  # 세액
        )
    )

    # 추가속성정보, 명세서 종류별 추가적인 속성을{key:value}형식의 Dictionary로 정의
    # 자세한 정보는 "전자명세서 API 연동매뉴얼 > [5.2. 기본양식 추가속성 테이블] 참조
    statement.propertyBag = {
        'Balance': "20000",  # 전잔액
        'Deposit': "5000",  # 입금액
        'CBalance': "25000"  # 현잔액
    }

    result = statementService.FAXSend(CorpNum, statement, SendNum, ReceiveNum, UserID)

    print("팩스 접수번호 : " + result)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
