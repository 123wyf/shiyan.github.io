import easygui
import time
easygui.msgbox("你是一个“编程猿”")
easygui.msgbox("天天编“智障”游戏")
easygui.msgbox("有一个被核辐射遍布的岛屿")
easygui.msgbox("每年，都会有许多的叫“和平精英”的大傻子来这里跳伞")
easygui.msgbox("但他们没有一个回来的")
easygui.msgbox("有一天，你脑瓜子犯病")
easygui.msgbox("你竟然花钱去作死，玩“和平精英”")
easygui.msgbox("你加入和平大厅")
easygui.msgbox("人家都穿貂皮大衣，就你一个穿小白衬衫")
a = easygui.buttonbox("你要选择", "", ["充钱", "使用爬虫", "啥都不干"])
if (a == "使用爬虫"):
    easygui.msgbox("光子把你告上了法庭,你蹲监狱了10年")
if (a == "充钱"):
    easygui.msgbox('你得到了一个小蓝衣')
    if easygui.ynbox("是否继续","",["是","否"]):
        easygui.msgbox("你点击了开始游戏")
        a = easygui.buttonbox("你要跳哪个地方","",["G港","医院","路边茅坑","P城","山顶废墟","啥都不干"])
        if (a == "G港"):
            easygui.msgbox("落地一把信号Q")
            if easygui.ynbox("继续","",["继续捡装备","找辆车,走人"]):
                easygui.msgbox("你捡了一把m416")
