from enum import Enum


class Class(str, Enum):
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"


class SubClass(str, Enum):
    # Barbarian
    BERSERKER = "Berserker"
    WILDHEART = "Wildheart"
    WILD_MAGIC_BARBARIAN = "Wild Magic Barbarian"

    # Bard
    COLLEGE_OF_LORE = "College of Lore"
    COLLEGE_OF_SWORDS = "College of Swords"
    COLLEGE_OF_VALOR = "College of Valor"

    # Cleric
    LIFE_DOMAIN = "Life Domain"
    LIGHT_DOMAIN = "Light Domain"
    TRICKERY_DOMAIN = "Trickery Domain"
    KNOWLEDGE_DOMAIN = "Knowledge Domain"
    NATURE_DOMAIN = "Nature Domain"
    TEMPEST_DOMAIN = "Tempest Domain"
    WAR_DOMAIN = "War Domain"

    # Druid
    CIRCLE_OF_THE_LAND = "Circle of the Land"
    CIRCLE_OF_THE_MOON = "Circle of the Moon"
    CIRCLE_OF_THE_SPORES = "Circle of the Spores"

    # Fighter
    BATTLE_MASTER = "Battle Master"
    CHAMPION = "Champion"
    ELDRITCH_KNIGHT = "Eldritch Knight"

    # Monk
    WAY_OF_THE_OPEN_HAND = "Way of the Open Hand"
    WAY_OF_SHADOW = "Way of Shadow"
    WAY_OF_THE_FOUR_ELEMENTS = "Way of the Four Elements"

    # Paladin
    OATH_OF_DEVOTION = "Oath of Devotion"
    OATH_OF_THE_ANCIENTS = "Oath of the Ancients"
    OATH_OF_VENGEANCE = "Oath of Vengeance"
    OATHBREAKER = "Oathbreaker"

    # Ranger
    BEAST_MASTER = "Beast Master"
    GLOOM_STALKER = "Gloom Stalker"
    HUNTER = "Hunter"

    # Rogue
    ARCANE_TRICKSTER = "Arcane Trickster"
    ASSASSIN = "Assassin"
    THIEF = "Thief"

    # Sorcerer
    DRACONIC_BLOODLINE = "Draconic Bloodline"
    STORM_SORCERY = "Storm Sorcery"
    WILD_MAGIC_SORCERER = "Wild Magic Sorcerer"

    # Warlock
    THE_ARCHFEY = "The Archfey"
    THE_FIEND = "The Fiend"
    THE_GREAT_OLD_ONE = "The Great Old One"

    # Wizard
    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"


CLASS_TO_SUBCLASSES = {
    Class.BARBARIAN: {SubClass.BERSERKER, SubClass.WILDHEART, SubClass.WILD_MAGIC_BARBARIAN},
    Class.BARD: {SubClass.COLLEGE_OF_LORE, SubClass.COLLEGE_OF_SWORDS, SubClass.COLLEGE_OF_VALOR},
    Class.CLERIC: {
        SubClass.LIFE_DOMAIN,
        SubClass.LIGHT_DOMAIN,
        SubClass.TRICKERY_DOMAIN,
        SubClass.KNOWLEDGE_DOMAIN,
        SubClass.NATURE_DOMAIN,
        SubClass.TEMPEST_DOMAIN,
        SubClass.WAR_DOMAIN,
    },
    Class.DRUID: {
        SubClass.CIRCLE_OF_THE_LAND,
        SubClass.CIRCLE_OF_THE_MOON,
        SubClass.CIRCLE_OF_THE_SPORES,
    },
    Class.FIGHTER: {SubClass.BATTLE_MASTER, SubClass.CHAMPION, SubClass.ELDRITCH_KNIGHT},
    Class.MONK: {
        SubClass.WAY_OF_THE_OPEN_HAND,
        SubClass.WAY_OF_SHADOW,
        SubClass.WAY_OF_THE_FOUR_ELEMENTS,
    },
    Class.PALADIN: {
        SubClass.OATH_OF_DEVOTION,
        SubClass.OATH_OF_THE_ANCIENTS,
        SubClass.OATH_OF_VENGEANCE,
        SubClass.OATHBREAKER,
    },
    Class.RANGER: {SubClass.BEAST_MASTER, SubClass.GLOOM_STALKER, SubClass.HUNTER},
    Class.ROGUE: {SubClass.ARCANE_TRICKSTER, SubClass.ASSASSIN, SubClass.THIEF},
    Class.SORCERER: {
        SubClass.DRACONIC_BLOODLINE,
        SubClass.STORM_SORCERY,
        SubClass.WILD_MAGIC_SORCERER,
    },
    Class.WARLOCK: {SubClass.THE_ARCHFEY, SubClass.THE_FIEND, SubClass.THE_GREAT_OLD_ONE},
    Class.WIZARD: {
        SubClass.ABJURATION,
        SubClass.CONJURATION,
        SubClass.DIVINATION,
        SubClass.ENCHANTMENT,
        SubClass.EVOCATION,
        SubClass.ILLUSION,
        SubClass.NECROMANCY,
        SubClass.TRANSMUTATION,
    },
}
