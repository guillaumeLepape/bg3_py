from bg3.classes import CLASS_TO_SUBCLASSES, CLASSES_UUID, SUBCLASSES_UUID, Class, SubClass


def test_classes() -> None:
    assert len(Class) == 12
    assert len(SubClass) == 46

    assert len(CLASS_TO_SUBCLASSES) == 12
    assert sum(1 for subclasses in CLASS_TO_SUBCLASSES.values() for _ in subclasses) == 46

    assert len(CLASSES_UUID) == 12
    assert len(SUBCLASSES_UUID) == 46
