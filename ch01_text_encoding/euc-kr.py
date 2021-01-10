"""
    1.3 EUC-KR (CP949)
    EUC-KR
    - 한국 산업 표준으로 지정된 한국어 문자 집합, 모든 글자가 완성된 형태로만 존재하는 완성형 코드
      - 한글처럼 초성, 중성, 종성을 조합해 문자를 만들 수 없기 때문에 EUC-KR로 표현할 수 없는 한글이 일부 존재함.
    - 문자하나를 표현하기 위해 2바이트를 사용
    - EUC-KR에 표현하는 문자 집합의 문자 중, 아스키 코드에도 포함되는 문자를 표현할 때는 1바이트를 사용 (아스키 코드와 호환)
    - 하나의 문자 집합, 하나의 문자열 인코딩

    CP949
    - EUC-KR을 확장한 문자 집합, EUC-KR과 같은 문자열 인코딩이나, 더 많은 문자를 표현할 수 있음.

    문자열 인코딩에서는 실제 문자열 길이가 버퍼 길이와 다른 경우가 많음.
    - 실제 문자열 길이: 사람 눈에 보이는 문자 길이
    - 버퍼 길이: 컴퓨터가 문자를 표현하는 데 사용한 바이트 수 (메모리에 할당된 공간을 의미함.)
"""
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = " ".join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = " ".join("{0}".format(int(c)) for c in byte_data)

    print("\"" + text + "\" 전체 문자 길이: {0}".format(len(text)))
    print("\"" + text + "\" 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(len(byte_data)))
    print("\"" + text + "\" 16진수 값: {0}".format(hex_data_as_str))
    print("\"" + text + "\" 10진수 값: {0}".format(int_data_as_str))

print_text("Hello", "euc-kr")
print_text("안녕하세요", "euc-kr")
