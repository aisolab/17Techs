"""
    1.2 아스키 코드 (ASCII)
    아스키 코드 (ASCII)
    - 처음으로 표준을 정립한 문자열 인코딩 방식이다. 
    - 사용할 수 있는 문자의 종류에는 대문자, 소문자, 아라비아 숫자, 공백 및 특수 문자들이 있으며 문자를 표현할 때는 0부터 127까지, 총 128개의 숫자를 사용한다.
    - 하나의 문자 집합, 하나의 문자열 인코딩
"""
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = " ".join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = " ".join("{0}".format(int(c)) for c in byte_data)
    
    print("\"" + text + "\" 전체 문자 길이: {0}".format(len(text)))
    print("\"" + text + "\" 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(len(byte_data)))
    print("\"" + text + "\" 16진수 값: {0}".format(hex_data_as_str))
    print("\"" + text + "\" 10진수 값: {0}".format(int_data_as_str))

print_text("Hello", "ascii")
