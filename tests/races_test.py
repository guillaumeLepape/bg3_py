from bg3.races import RACE_TO_SUBRACES, Race, SubRace


def test_race() -> None:
    assert len(Race) == 11
    assert len(SubRace) == 28

    assert len(RACE_TO_SUBRACES) == 11
    assert sum(1 for subraces in RACE_TO_SUBRACES.values() for _ in subraces) == 28
