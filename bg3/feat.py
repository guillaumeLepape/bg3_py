from .classes import Class


def new_feat(class_name: Class, level: int) -> bool:
    return (
        level == 4
        or level == 8
        or level == 12
        or (level == 6 and class_name == Class.FIGHTER)
        or (level == 10 and class_name == Class.ROGUE)
    )
