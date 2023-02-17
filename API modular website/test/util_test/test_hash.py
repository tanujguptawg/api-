# import pytest 
from util import hash_code


def test_correct_hash():
    password = "new1pass"
    hash_value = "fe8ef9b33a20fd81cbf670f4fd8852dce0f2ba6afd850d9f79be6d267deea438357204165f6c7cd4d841031ca168ea927021525c4bf22335aa57275b17305581"
    assert hash_code.HashClass.hash_func(password) == hash_value



def test_incorrect_hash():
    password = "tanu"
    hash_value = "71d389f27e12bade194212b1671306dda5d353ab478a98c772b369b2373027b94425fca4898b210495a7cf8227572f507920ce3c622e1b5e780a91294fbdc6b0"

    assert hash_code.HashClass.hash_func(password) != hash_value