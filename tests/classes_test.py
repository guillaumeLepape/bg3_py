from bg3.classes import CLASS_TO_SUBCLASSES, Class, SubClass


def test_classes() -> None:
    assert len(Class) == 12
    assert len(SubClass) == 46

    assert len(CLASS_TO_SUBCLASSES) == 12
    assert sum(1 for subclasses in CLASS_TO_SUBCLASSES.values() for _ in subclasses) == 46
