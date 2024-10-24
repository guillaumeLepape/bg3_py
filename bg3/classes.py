from enum import Enum
from uuid import UUID


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


CLASSES_UUID = {
    Class.BARBARIAN: UUID("1b821d50-33b9-40f1-bc0e-a048dfc2e3c0"),
    Class.BARD: UUID("587f8458-6b68-48d9-a751-9f1473c52067"),
    Class.CLERIC: UUID("fd6ae40a-a51e-480f-8902-d6c4cfba08b4"),
    Class.DRUID: UUID("058f0ada-4730-4923-b28a-7ce32c0ba2ba"),
    Class.FIGHTER: UUID("6081cffe-c535-46ec-a5c4-c77b232e9c45"),
    Class.MONK: UUID("0b73c986-5d28-4be6-96fb-61da212d4d56"),
    Class.PALADIN: UUID("d78ff927-f3b3-4948-ada0-3b924c17c947"),
    Class.RANGER: UUID("155e86b0-2991-492a-98fe-7d5250416822"),
    Class.ROGUE: UUID("d92ce93a-298b-421f-a8a1-7d45bbdb5ffe"),
    Class.SORCERER: UUID("c3c2d668-5170-48a5-ae9e-543c8979d9c2"),
    Class.WARLOCK: UUID("48ba1741-5b96-4bad-ac13-ba03aec26ddc"),
    Class.WIZARD: UUID("9fef5003-8ec9-4f22-80a4-ad49c37e9cf1"),
}


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


SUBCLASSES_UUID = {
    SubClass.BERSERKER: UUID("07daa49f-9452-478f-bb83-f573a76ffb5e"),
    SubClass.WILDHEART: UUID("ad41acef-613c-4591-9f62-b4e971ad525c"),
    SubClass.WILD_MAGIC_BARBARIAN: UUID("51b47ffc-3167-4bec-a19e-cfa088f1077b"),
    SubClass.COLLEGE_OF_LORE: UUID("78c252b5-ba90-4920-adfe-5d08949ab151"),
    SubClass.COLLEGE_OF_SWORDS: UUID("977de590-3d3b-4be3-9fee-8a7433ee398b"),
    SubClass.COLLEGE_OF_VALOR: UUID("3b7e4698-b9d5-4ebb-ae34-396303f51264"),
    SubClass.LIFE_DOMAIN: UUID("3ccb2a08-dcf0-411a-aab7-35f1bd1cd7de"),
    SubClass.LIGHT_DOMAIN: UUID("25099171-97bf-488f-8e3a-f7a4838c8388"),
    SubClass.TRICKERY_DOMAIN: UUID("47046ddd-c55e-4203-8572-e6b97bc471a0"),
    SubClass.KNOWLEDGE_DOMAIN: UUID("de4aed2c-919b-4144-beab-beae20c41ac7"),
    SubClass.NATURE_DOMAIN: UUID("41867585-e683-4451-ab2a-076d1b4c7eea"),
    SubClass.TEMPEST_DOMAIN: UUID("d2a985b3-df45-4c07-bf54-f8e35a3e7468"),
    SubClass.WAR_DOMAIN: UUID("8c89eaf4-e6ee-4fa7-86e7-b007a309b006"),
    SubClass.CIRCLE_OF_THE_LAND: UUID("528d5789-3c58-413a-bbe4-42a222245dee"),
    SubClass.CIRCLE_OF_THE_MOON: UUID("d1bf3120-ffea-49bc-992b-5cfbe8486c4e"),
    SubClass.CIRCLE_OF_THE_SPORES: UUID("baf94633-169c-4cb6-9b98-9f3cf2384f62"),
    SubClass.BATTLE_MASTER: UUID("95d1015c-11e3-4eb6-8f6a-dc76e4b02aae"),
    SubClass.CHAMPION: UUID("01139c16-5f89-4e01-95bb-6c9231fc88cb"),
    SubClass.ELDRITCH_KNIGHT: UUID("a516f975-0728-485b-996c-b5d2ef810961"),
    SubClass.WAY_OF_THE_OPEN_HAND: UUID("832e951e-2103-414f-a388-1da027c182fa"),
    SubClass.WAY_OF_SHADOW: UUID("b18d7568-3385-4dca-a8fb-a2a11893d654"),
    SubClass.WAY_OF_THE_FOUR_ELEMENTS: UUID("3a73be6b-6567-41e2-8d11-2fe02d0f789b"),
    SubClass.OATH_OF_DEVOTION: UUID("d3dbd155-f92d-4245-9730-6a9f7e34adfd"),
    SubClass.OATH_OF_THE_ANCIENTS: UUID("838cc1af-4df1-4c0d-8364-c5547989101f"),
    SubClass.OATH_OF_VENGEANCE: UUID("cf599e7d-3109-4f75-9c93-8258cc5c26ab"),
    SubClass.OATHBREAKER: UUID("0e409d36-a37d-4d72-84f3-e14b2c2da1c7"),
    SubClass.BEAST_MASTER: UUID("9fad21be-4149-4d61-b98a-0307cf4d7abb"),
    SubClass.GLOOM_STALKER: UUID("21b7db94-0491-4366-98a5-2d49da8eba17"),
    SubClass.HUNTER: UUID("c14fe07d-0b14-4938-8908-b23fab95e51f"),
    SubClass.ARCANE_TRICKSTER: UUID("2fa5f771-f183-4610-9dfc-d4af901b7142"),
    SubClass.ASSASSIN: UUID("18894f3a-354a-48da-a529-9a496ad66b68"),
    SubClass.THIEF: UUID("5260aae1-e4b3-44e3-ba96-dc106d25f70f"),
    SubClass.DRACONIC_BLOODLINE: UUID("677fed50-13b1-437e-be8e-4aff039016cd"),
    SubClass.STORM_SORCERY: UUID("83cbe48b-a63f-4b5e-bb06-69839eb6fac6"),
    SubClass.WILD_MAGIC_SORCERER: UUID("67130f95-10f6-4aac-a457-75884350ab19"),
    SubClass.THE_ARCHFEY: UUID("c80b17b5-77ff-49b9-8539-7af0ebcf9e80"),
    SubClass.THE_FIEND: UUID("c9dbe3ff-ff57-469b-94dc-e40127e1ba1e"),
    SubClass.THE_GREAT_OLD_ONE: UUID("82efe519-1c26-44ee-a090-e4d35b94fb0b"),
    SubClass.ABJURATION: UUID("072f4bc8-1531-4b35-bf18-ff4c343b436f"),
    SubClass.CONJURATION: UUID("8cac78c5-93f2-428f-abc5-7a2802890dcc"),
    SubClass.DIVINATION: UUID("f0f12ef6-aeeb-452e-8cc1-ad0f066f437a"),
    SubClass.ENCHANTMENT: UUID("0a66cda3-1fda-4f3a-abf5-6fd6d61c566f"),
    SubClass.EVOCATION: UUID("74b8e74c-f89c-4723-b3c1-1aa2165c15c8"),
    SubClass.ILLUSION: UUID("8581394c-9c8c-4b7a-963d-073264fd7a9b"),
    SubClass.NECROMANCY: UUID("437a7d9a-faab-4170-b690-805b53d1c888"),
    SubClass.TRANSMUTATION: UUID("a8610286-eeee-4de9-9535-7a1931eb8ad1"),
}


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
