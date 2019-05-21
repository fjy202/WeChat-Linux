import itchat
itchat.auto_login(hotReload=True,enableCmdQR=2)
@itchat.msg_register(itchat.content.TEXT)
def _(msg):
    user=msg.fromUserName
    print(user+": "+msg.text)
while 1:
    cmd=input("enter command(h for help): ")
    if cmd=="h":
        print("""usage:
send message	send message
switch friend	switch to Other party
quit	quit this program""")
    elif "send" == cmd[:4]:
        if not "author" in globals():
            print("Please execute the \"switch\" command.")
            continue
        author.send(cmd[5:] or input('message: '))
    elif "switch" == cmd[:6]:
        try:
            author=itchat.search_friends(cmd[7:] or input("user:"))[0]
        except:
            print("no such friend")
    elif cmd=="quit":
        exit()
    else:
        print("unknow command.")