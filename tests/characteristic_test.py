from bg3.characteristic import TRIGRAM_TO_CHARACTERISTIC, Characteristic


def test_characteristic() -> None:
    assert len(Characteristic) == 6
    assert len(TRIGRAM_TO_CHARACTERISTIC) == 6
