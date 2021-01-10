"""
    UTF-16
    UTF-16
    - 16비트 (2바이트)로 인코딩하는 것을 의미함.
    - 2바이트 또는 4바이트만 사용하기 때문에 아스키 코드와 호환되지 않음.
    - 문자가 어떤 평면에 속하느냐에 따라 사용하는 바이트 수가 달라짐. 
      - 기본 다국어 평면에 포함되는 문자일 경우 2바이트, 그 외는 4바이트를 사용함.
    - 바이트 순서 표시를 사용함.

    바이트 순서 표시 (byte order mark, BOM)
    - 문자열 가장 맨 앞 2바이트에 0xFEFF (유니코드로 U+FEFF)로 표기하여 사용하는 것을 의미함.
      - 0xFE와 0xFF 중 어떤 문자가 먼저 오는 지에 따라 리틀 엔디언 (little endian, LE), 빅 엔디언 (big endian, BE)로 나누어짐.
        - 리틀 엔디언: 0xFF 다음에 0xFE를 읽음. (작은 단위부터 읽음. <-)
        - 빅 엔디언: 0xFE 다음에 0xFF를 읽음. (큰 단위부터 읽음. ->)
      - 두 방식에 따라 문자열 인코딩 시 바이트 데이터를 조합하는 순서가 바뀜.
      - 순서를 정하는 이유는, CPU 설계에 따라 바이트 값을 처리하는 순서가 다르기 때문임.
      - 오늘 날 대부분의 개인 컴퓨터는 리틀 엔디언 방식을 활용함. 
"""
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = " ".join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = " ".join("{0}".format(int(c)) for c in byte_data)

    print("\"" + text + "\" 전체 문자 길이: {0}".format(len(text)))
    print("\"" + text + "\" 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(len(byte_data)))
    print("\"" + text + "\" 16진수 값: {0}".format(hex_data_as_str))
    print("\"" + text + "\" 10진수 값: {0}".format(int_data_as_str))

print_text("Hello", "utf-16")
print_text("안녕하세요", "utf-16")
