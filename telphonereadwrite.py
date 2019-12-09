# 利用字典存储 姓名-电话号码对, 并练习字典的各种操作
f=open('telphonenum.txt','r')

tel_dict={}

while True:
    s=f.readline()
    if s=="":
        break
    li=s.split() #分隔得到列表  li[0]是姓名, li[1]是电话
    if len(li)==2:
        tel_dict[li[0]]=li[1]

f.close()




def find_phone():
    print ('电话号码如下：')
    for x in tel_dict:
        print (x, tel_dict[x])
    print('\n') 
    while True:
        name=input('\n请输入查询电话:')
        if name=="":   #如不输入姓名，则跳出
            break
        if name in tel_dict: #先判断有无此key
            print  ('\n',name, '的电话号码是',tel_dict[name])
            print ("\n按回车键退出")
        else:
            print ('nobody is:',name)

            
def change_phone():
    name=input('请输入姓名:')
    if (name == ''):
        return 0
    elif (name in tel_dict):
        print  ('\n',name, '的电话号码是',tel_dict[name])
        newtel=input('请输入'+name+'的新电话:')
    else:
        print ("电话本中没有" + name + "的电话")
        newtel=input('新增'+name+'的电话:')
        

    tel_dict[name]=newtel  #如name已存在,则是更新; 如name不存在,则是新增
    print (name+'的号码已更新\n')

    
def delete_phone():
    name=input('请输入要删除的姓名:')
    try:
        del tel_dict[name] #如name不存在, del 删除时将报错
        print (name+'已删除')
    except Exception as e:
        print ('删除错误:', e)

def add_phone():
    name = input("请输入要添加的联系人：")
    phonenumber = input(name + "的电话是：")
    tel_dict [name] = phonenumber
    print("已添加" + name + "的电话是：" + phonenumber)


def print_phonelist():
    print ('电话号码如下：')
    for x in tel_dict:
        print (x, tel_dict[x])
    print('\n')
    

while True:
    c = input("[1] 查询电话\n[2] 更改电话\n[3] 删除电话\n[4] 新增电话\n[5] 查看电话表\n[q] 退出\n")
    if (c == '1'):
        find_phone()
    if (c == '2'):
        change_phone()
    if (c == '3'):   
        delete_phone()
    if (c == '4'):
        add_phone()
    if (c == '5'):
        print_phonelist()
    if (c == 'q' or c == ''):
        break
        
print ('\n电话本保存完成...')
f=open('telphonenum.txt','w')
for x in tel_dict:
    f.write(x+'  '+tel_dict[x]+'\n')
f.close()
    


