import json
from const import DataConst


CHARACTER_JSON = r"./character.json"
DATABASE_JSON = r"./database.json"
# 已有角色列表
CHARACTER_LIST = []
# 生产力角色列表 (互斥)
GOLD_CHARACTER_LIST = []
LEVEL_CHARACTER_LIST = []
MONEY_CHARACTER_LIST = []
ALL_CHARACTER_LIST = []
# 有存储技能的角色列表 (非互斥)
STORAGE_CHARACTER_LIST = []
# 有影响心情技能的角色列表 (非互斥)
MOOD_CHARACTER_LIST = []


def get_my_character():
    global CHARACTER_JSON, CHARACTER_LIST
    with open(CHARACTER_JSON, "r", encoding='utf-8') as file:
        CHARACTER_LIST = json.load(file)
    for character in CHARACTER_LIST:
        if character[DataConst.CHARACTER_OWN] != True:
            CHARACTER_LIST.remove(character)

def check_database():
    global CHARACTER_LIST, DATABASE_JSON
    global GOLD_CHARACTER_LIST, LEVEL_CHARACTER_LIST, MONEY_CHARACTER_LIST, ALL_CHARACTER_LIST, STORAGE_CHARACTER_LIST

    database = {}
    with open(DATABASE_JSON, "r", encoding='utf-8') as file:
        database = json.load(file)
    for owned_character in CHARACTER_LIST:
        character = database[owned_character[DataConst.CHARACTER_NAME]]

        if character[DataConst.SKILL_PRODUCT_TYPE] == DataConst.TYPE_METAL:
            GOLD_CHARACTER_LIST.append(character)
        elif character[DataConst.SKILL_PRODUCT_TYPE] == DataConst.TYPE_LEVEL:
            LEVEL_CHARACTER_LIST.append(character)
        elif character[DataConst.SKILL_PRODUCT_TYPE] == DataConst.TYPE_MONEY:
            MONEY_CHARACTER_LIST.append(character)
        elif character[DataConst.SKILL_PRODUCT_TYPE] == DataConst.TYPE_ALL:
            ALL_CHARACTER_LIST.append(character)

        if character[DataConst.SKILL_STORAGE] != None:
            STORAGE_CHARACTER_LIST.append(character)

        if character[DataConst.SKILL_MOOD] != None:
            MOOD_CHARACTER_LIST.append(character)

def room_make():
    # TODO 
    pass


if __name__ == "__main__":
    get_my_character()
    check_database()