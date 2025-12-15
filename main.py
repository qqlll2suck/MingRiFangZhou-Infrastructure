import json

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
        if character["own"] != True:
            CHARACTER_LIST.remove(character)

def check_database():
    global CHARACTER_LIST, DATABASE_JSON
    global GOLD_CHARACTER_LIST, LEVEL_CHARACTER_LIST, MONEY_CHARACTER_LIST, ALL_CHARACTER_LIST, STORAGE_CHARACTER_LIST

    database = {}
    with open(DATABASE_JSON, "r", encoding='utf-8') as file:
        database = json.load(file)
    for owned_character in CHARACTER_LIST:
        character = database[owned_character["name"]]

        if character["type"] == "Gold":
            GOLD_CHARACTER_LIST.append(character)
        elif character["type"] == "Level":
            LEVEL_CHARACTER_LIST.append(character)
        elif character["type"] == "Money":
            MONEY_CHARACTER_LIST.append(character)
        elif character["type"] == "All":
            ALL_CHARACTER_LIST.append(character)

        if character["storage_skill"] != None:
            STORAGE_CHARACTER_LIST.append(character)

        if character["mood_skill"] != None:
            MOOD_CHARACTER_LIST.append(character)

def room_make():
    '''
    有4个LEVEL房间, 1个GOLD房间
    每个房间需要2个队列, 每个队列需要3个角色

    优先逻辑:
    每个房间优先使用对应类型的角色, 如果不够则使用ALL类型的角色补充
    每个角色只能使用一次
    每个队列中不能有重复角色
    每个队列中最多有一个仓库技能角色,最好每个队列都有仓库技能角色
    '''


if __name__ == "__main__":
    get_my_character()
    check_database()