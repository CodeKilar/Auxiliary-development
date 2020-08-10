import re
import csv
import sys
import logging

def interface():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(funcName)-8s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    buttonlist = [1, 2, 3]
    print('===============')
    print('1.monster表查错')
    print('2.npc表查错')
    print('3.magic表查错')
    print('0.退出')
    print('==============')
    key = input()
    return key

def chk_monster():
    # 检索Monster_type表
    csvFile = open('D:\SVN\编辑器\data\config\monster_type.csv', 'r')
    reader = csv.reader(csvFile)
    MonsterType = []
    for row in reader:
        MonsterType.append(row)
    csvFile.close

    # 检索MonsterGen表
    csvFile = open('D:\SVN\编辑器\data\config\monster_gen.csv', 'r')
    reader = csv.reader(csvFile)
    MonsterGen = []
    for row in reader:
        MonsterGen.append(row)
    csvFile.close

    # 开始比较monster_type->monster_gen
    logging.info("##Start Checking...")
    bMatch = True
    tShowTypeTable = []
    tFilterTable = ['id', '', "monster_type"]
    for i in range(len(MonsterType)):
        bSetTable = True
        for j in range(len(MonsterGen)):
            if re.fullmatch(MonsterType[i][0], MonsterGen[j][1]) != None:
                bSetTable = False
        if bSetTable:
            tShowTypeTable.append(MonsterType[i][0])

    # 开始比较monster_gen->monster_type
    bMatch = True
    tShowGenTable = []
    tFilterTable = ['id', '']
    for i in range(len(MonsterGen)):
        bSetTable = True
        for j in range(len(MonsterType)):
            if re.fullmatch(MonsterGen[i][1], MonsterType[j][0]) != None:
                bSetTable = False
        if bSetTable:
            tShowGenTable.append(MonsterGen[i][0])

    # 输出打印
    print("\n以下TypeId不存在对应的GenId\n")
    for i in range(len(tShowTypeTable)):
        if tShowTypeTable[i] not in tFilterTable:
           print(tShowTypeTable[i])
    print("\n以下GenId不存在对应的TypeId\n")
    for i in range(len(tShowGenTable)):
        if tShowGenTable[i] not in tFilterTable:
           print(tShowGenTable[i])

    logging.info("##End Check")
def chk_npc():
    # 检索npc_type表
    csvFile = open(r'D:\SVN\编辑器\data\config\npc_type.csv', 'r')
    reader = csv.reader(csvFile)
    NpcType = []
    for row in reader:
        NpcType.append(row)
    csvFile.close

    # 检索npcrGen表
    csvFile = open(r'D:\SVN\编辑器\data\config\npc_gen.csv', 'r')
    reader = csv.reader(csvFile)
    NpcGen = []
    for row in reader:
        NpcGen.append(row)
    csvFile.close

    # 开始比较npc_type->npc_gen
    logging.info("##Start Checking...")
    bMatch = True
    tShowTypeTable = []
    tFilterTable = ['id', '', "npc_type"]
    for i in range(len(NpcType)):
        bSetTable = True
        for j in range(len(NpcGen)):
            if re.fullmatch(NpcType[i][0], NpcGen[j][1]) != None:
                bSetTable = False
        if bSetTable:
            tShowTypeTable.append(NpcType[i][0])

    # 开始比较npc_gen->npc_type
    bMatch = True
    tShowGenTable = []
    for i in range(len(NpcGen)):
        bSetTable = True
        for j in range(len(NpcType)):
            if re.fullmatch(NpcGen[i][1], NpcType[j][0]) != None:
                bSetTable = False
        if bSetTable:
            tShowGenTable.append(NpcGen[i][0])

    # 输出打印
    print("\n以下TypeId不存在对应的GenId\n")
    for i in range(len(tShowTypeTable)):
        if tShowTypeTable[i] not in tFilterTable:
           print(tShowTypeTable[i])
    print("\n以下GenId不存在对应的TypeId\n")
    for i in range(len(tShowGenTable)):
        if tShowGenTable[i] not in tFilterTable:
           print(tShowGenTable[i])

    logging.info("##End Check")
def chk_magic():
    print('magic')
def chk_exit():
    sys.exit()
def default():
    switch = {'1': chk_monster,
              '2': chk_npc,
              '3': chk_magic,
              '0': chk_exit,
                 }
    print('请重新输入')
    key = interface()
    switch.get(key, default)()

if __name__ == '__main__':
    switch = {'1': chk_monster,
              '2': chk_npc,
              '3': chk_magic,
              '0': chk_exit,
                 }
    while True:
        key = interface()
        switch.get(key, default)()
