# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Statement, StatementDetail, StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest

'''
전자명세서 1건을 임시저장합니다.
- 임시저장 상태의 명세서는 발행(Issue API)을 호출해야 공급받는자에게 메일이 전송됩니다.
'''

try:
    print("=" * 15 + " 전자명세서 임시저장 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 전자명세서 정보
    statement = Statement(
        # 작성일자 yyyyMMdd
        writeDate = "20161123",

        # '영수'/'청구' 중 기재
        purposeType = "영수",

        # 과세형태, '과세'/'영세'/'면세' 중 기재
        taxType = "과세",

        # 맞춤양식코드, 미기재시 기본양식으로 처리
        formCode = "",

        # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
        itemCode = 121,

        # 전자명세서 관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
        mgtKey = "20161123-02",

        # 공급자 사업자번호, '-' 제외 10자리
        senderCorpNum = CorpNum,

        # 공급자 상호
        senderCorpName = "공급자 상호",

        # 공급자 주소
        senderAddr = "공급자 주소",

        # 공급자 대표자 성명
        senderCEOName = "공급자 대표자 성명",

        # 공급자 종사업장 식별번호, 필요시 4자리 숫자값 기재
        senderTaxRegID = "",

        # 공급자 종목
        senderBizClass = "종목",

        # 공급자 업태
        senderBizType = "업태",

        # 공급자 담당자 성명
        senderContactName = "공급자 담당자명",

        # 공급자 메일주소
        senderEmail = "test@test.com",

        # 공급자 연락처
        senderTEL = "070-4304-2991",

        # 공급자 휴대폰번호
        senderHP = "010-000-222",


        # 공급받는자 사업자번호, '-' 제외 10자리
        receiverCorpNum = "8888888888",

        # 공급받는자 상호
        receiverCorpName = "공급받는자 상호",

        # 공급받는자 대표자 성명
        receiverCEOName = "공급받는자 대표자 성명",

        # 공급받는자 주소
        receiverAddr = "공급받는자 주소",

        # 공급받는자 종사업장식별번호, 필요시 4자리 숫자값 기재
        receiverTaxRegID = "",

        # 공급받는자 종목
        receiverBizClass = "공급받는자 종목",

        # 공급받는자 업태
        receiverBizType = "공급받는자 업태",

        # 공급받는자 담당자 성명
        receiverContactName = "공급받는자 담당자명",

        # 공급받는자  메일주소
        receiverEmail = "test@test.com",

        # 공급받는자 연락처
        receiverTEL = "070111222",

        # 공급받는자 휴대폰번호
        receiverHP = "010-111-222",

        # 공급가액 합계
        supplyCostTotal = "20000",

        # 세액 합계
        taxTotal = "2000",

        # 합계금액, 공금가액 합계 + 세액 합계
        totalAmount = "22000",

        # 기재 상 '일련번호' 항목
        serialNum = "123",

        # 기재 상 '비고' 항목
        remark1 = "비고1",
        remark2 = "비고2",
        remark3 = "비고3",

        # 사업자등록증 이미지 첨부 여부
        businessLicenseYN = False,

        # 통장사본 이미지 첨부 여부
        bankBookYN = False,

        # 상세항목(품목) 정보
        detailList = [
            StatementDetail(
                serialNum = 1,          #일련번호, 1부터 순차기재
                itemName = "품목1",
                purchaseDT = "20161120", # 거래일자
                spec = "BOX",           # 규격
                unitCost = "10000",     # 단가
                qty = 1,                # 수량
                supplyCost = "10000",   # 공급가액
                tax = "1000" #세액
            ),
            StatementDetail(
                serialNum = 2,          #일련번호, 1부터 순차기재
                itemName = "품목1",
                purchaseDT = "20161120", # 거래일자
                spec = "BOX",           # 규격
                unitCost = "10000",     # 단가
                qty = 1,                # 수량
                supplyCost = "10000",   # 공급가액
                tax = "1000" #세액
            )
        ],

        # 추가속성정보, 명세서 종류별 추가적인 속성을{key:value}형식의 Dictionary로 정의
        # 자세한 정보는 "전자명세서 API 연동매뉴얼 > [5.2. 기본양식 추가속성 테이블] 참조
        propertyBag = {
            'Balance': '20000', # 전잔액
            'Deposit' : '5000', # 입금액
            'CBalance': '25000' # 현잔액
        }
    )

    result = statementService.register(CorpNum, statement)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
