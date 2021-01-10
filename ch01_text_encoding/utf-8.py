"""
    유니코드
    유니코드 (Unicode)
    - 동일한 규칙으로 모든 언어를 표현할 수 있는 문자 집합
    - 유니코드 문자 집합을 표현하는 문자열 인코딩은 UTF-8, UTF-16, UTF-32 등이 존재
    - 문자의 종류에 따라 기본 다국어 평면 (Basic Multilingual Plane, BMP), 보충 다국어 평면 (Supplementary Multilingual Plane, SMP), 상형 문자 보충 평면 (Supplementary Ideographic Plane, SIP),
     특수 목적 보충 평면 (Supplementary Specialpurpose Plane, SSP) 등이 있음.
    - 하나의 문자 집합 다수의 문자열 인코딩

    UTF-8
    - 유니코드 문자 집합을 8비트 (1바이트)로 인코딩 하는 문자열 인코딩
    - 아스키 코드와 완벽하게 호환, 표현하려는 문자에 따라 최소 1바이트에서 최대 6바이트까지 사용
"""
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = " ".join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = " ".join("{0}".format(int(c)) for c in byte_data)

    print("\"" + text + "\" 전체 문자 길이: {0}".format(len(text)))
    print("\"" + text + "\" 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(len(byte_data)))
    print("\"" + text + "\" 16진수 값: {0}".format(hex_data_as_str))
    print("\"" + text + "\" 10진수 값: {0}".format(int_data_as_str))

print_text("Hello", "utf-8")
print_text("안녕하세요", "utf-8")
