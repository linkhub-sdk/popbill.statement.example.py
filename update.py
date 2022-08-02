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
"임시저장" 상태의 전자명세서를 수정합니다.
- https://docs.popbill.com/statement/python/api#Update
'''

try:
    print("=" * 15 + " 전자명세서 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 수정할 전자명세서 문서번호
    mgtKey = "20220803-001"

    # 전자명세서 정보
    statement = Statement(
        # 작성일자 yyyyMMdd
        writeDate="20220803",

        # {영수, 청구, 없음} 중 기재
        purposeType="영수",

        # 과세형태, {과세, 영세, 면세} 중 기재
        taxType="과세",

        # 맞춤양식코드, 미기재시 기본양식으로 처리
        formCode="",

        # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
        itemCode=ItemCode,

        # 전자명세서 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 발신자별 고유번호 생성
        mgtKey=mgtKey,

        # 발신자 사업자번호, '-' 제외 10자리
        senderCorpNum=CorpNum,

        # 발신자 상호
        senderCorpName="발신자 상호",

        # 발신자 주소
        senderAddr="발신자 주소_수정",

        # 발신자 대표자 성명
        senderCEOName="발신자 대표자 성명_수정",

        # 발신자 종사업장 식별번호, 필요시 4자리 숫자값 기재
        senderTaxRegID="",

        # 발신자 종목
        senderBizClass="종목",

        # 발신자 업태
        senderBizType="업태",

        # 발신자 담당자 성명
        senderContactName="발신자 담당자명",

        # 발신자 메일주소
        senderEmail="",

        # 발신자 연락처
        senderTEL="",

        # 발신자 휴대폰번호
        senderHP="",

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

        # 수신자 메일주소
        # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
        # 실제 거래처의 메일주소가 기재되지 않도록 주의
        receiverEmail="",

        # 수신자 연락처
        receiverTEL="",

        # 수신자 휴대폰번호
        receiverHP="",

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

        # 사업자등록증 이미지 첨부여부  (true / false 중 택 1)
        # └ true = 첨부 , false = 미첨부(기본값)
        # - 팝빌 사이트 또는 인감 및 첨부문서 등록 팝업 URL (GetSealURL API) 함수를 이용하여 등록
        businessLicenseYN=False,

        # 통장사본 이미지 첨부여부  (true / false 중 택 1)
        # └ true = 첨부 , false = 미첨부(기본값)
        # - 팝빌 사이트 또는 인감 및 첨부문서 등록 팝업 URL (GetSealURL API) 함수를 이용하여 등록
        bankBookYN=False,

        # 발행시 알림문자 전송여부
        smssendYN=True
    )

    # 상세항목(품목) 정보 (배열 길이 제한 없음)
    statement.detailList = []

    statement.detailList.append(
        StatementDetail(
            serialNum=1,  # 일련번호, 1부터 순차기재
            itemName="품목1",  # 품목
            purchaseDT="20220803",  # 거래일자
            spec="BOX",  # 규격
            unitCost="10000",  # 단가
            qty=1,  # 수량
            supplyCost="10000",  # 공급가액
            tax="1000",  # 세액
            remark="비고",  # 비고
            spare1="여분1",  # 여분1
            spare2="여분2",  # 여분2
            spare3="여분3",  # 여분3
            spare4="여분4",  # 여분4
            spare5="여분5",  # 여분5
        )
    )
    statement.detailList.append(
        StatementDetail(
            serialNum=2,  # 일련번호, 1부터 순차기재
            itemName="품목1",  # 품목
            purchaseDT="20220803",  # 거래일자
            spec="BOX",  # 규격
            unitCost="10000",  # 단가
            qty=1,  # 수량
            supplyCost="10000",  # 공급가액
            tax="1000",  # 세액
            remark="비고",  # 비고
            spare1="여분1",  # 여분1
            spare2="여분2",  # 여분2
            spare3="여분3",  # 여분3
            spare4="여분4",  # 여분4
            spare5="여분5",  # 여분5
        )
    )

    # 추가속성정보, 명세서 종류별 추가적인 속성을{key:value}형식의 Dictionary로 정의
    statement.propertyBag = {
        'Balance': "20000",  # 전잔액
        'Deposit': "5000",  # 입금액
        'CBalance': "25000"  # 현잔액
    }

    result = statementService.update(CorpNum, ItemCode, mgtKey, statement)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
