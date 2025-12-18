import dataclasses


@dataclasses.dataclass
class DataConst:
    CHARACTER_NAME = "name"
    CHARACTER_OWN = "own"

    TYPE_METAL = "metal"
    TYPE_LEVEL = "level"
    TYPE_MONEY = "money"
    TYPE_ALL = "all"

    SKILL_PRODUCT_TYPE = "type"
    SKILL_STORAGE = "storage_skill"
    SKILL_MOOD = "mood_skill"
