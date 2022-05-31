from main import RS4
def test():
    rs4 = RS4(67)
    text = 'hello my friend, sending you super secret password from my binance account: flower key book table stream leg fluffy toothbrush chicken jeans plant power'
    encrypted = rs4.run(text)
    decrypted = rs4.run(encrypted)
    print(decrypted)
    assert decrypted == text
test()