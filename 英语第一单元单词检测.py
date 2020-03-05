from itertools import islice
st = open ("存储文件，不要删除！.reiiio","r")
def hangman(word):
    wrong = 0
    stages = ["",
              "______________                ",
              "|                              ",
              "|             |                ",
              "|             Ο               ",
              "|            /|\               ",
              "|             /\               ",
              "|                               ",
              ]
    rletters = list(word)
    board = ["＿"] * len(word)
    win = False
    print("欢迎来到hangman小游戏\n 游戏规则：\n 1.根据提示，猜出字母；\n 2.拼好单词，如果错误超出10个，游戏失败")
    print("祝你好运！")
    print("\n")
    while wrong < len(stages) + 1:
        msg = "请回答"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print((" ".join(board)))
            print("正确")
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0:e]))
            print("错误")
            if "＿" not in board:
                print("你赢了！")
                print(" ".join(board))
                with open("存储文件，不要删除！.reiiio") as f:
                    金币1 = list(islice(f, 2))
                    金币 = 金币1[1]
                    金币 = int(金币)
                    金币 = 金币+1
                    pass
                st = open ("存储文件，不要删除！.reiiio","w")
                with open("存储文件，不要删除！.reiiio") as f:
                   st.write("！！！"+"\n")
                   金币 = str (金币)
                   st.write(金币+"\n")
                win = True
                break
                ans = input("再来一局？请回答“T”或者“F”")
                if ans == "T":
                  hangman(单词[gf])
                ans = input("再来一局？请回答“T”或者“F”")
                if ans == "T":
                  hangman(单词[gf])
    if not win:
        print("\n".join(stages[0:wrong]))
        print("你输了！正确的单词是：cat".format(word))
        ans = input("再来一局？请回答“T”或者“F”")
        if ans == "T":
          hangman(单词[gf])
        ans = input("再来一局？请回答“T”或者“F”")
        if ans == "T":
         hangman(单词[gf])



单词 = ["younger","older","taller","shorter","longer","thinner","heavier","bigger","smaller","stronger","dinosaur","hall","metre","than","both","kilogram","countryside","lower","shadow","smarter","become"]
import random
gf = random.randint(0,20)
hangman(单词[gf])
ans = input("再来一局？请回答“T”或者“F”")
if ans == "是":
    hangman(单词[gf])
ans = input("再来一局？请回答“T”或者“F”")
if ans == "T":
  hangman(单词[gf])

            

