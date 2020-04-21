from backend.util.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    number = 3526
    hex_number = hex(number)[2:]

    binary_number = hex_to_binary(hex_number)
    backtransformed_number = int(binary_number, 2)

    assert backtransformed_number == number