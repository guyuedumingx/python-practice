import action 
import settings

file_name = 'chaci.json'
word_book = settings.open_file(file_name)

# 判断是否退出软件  
judge = True
print("[w]查看单词库\t[d]删除单词\t[r]复习单词\t[q]退出软件\n")
while judge:
    c = input("请输入单词: ")
    judge = action.judge(word_book, c.strip())

# 调用settings保存文件  
settings.save_file(word_book, file_name)
