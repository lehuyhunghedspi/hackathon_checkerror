

def getvideo():
    pass
def sendvideo():
    pass
def receive_respond():
    pass

def playrecord():
    pass
def playvideo():
    pass


dongtacs=['01','02']

i=0
while(True):
    dongtac=dongtacs[i]
    currentvideo=[]
    has_false=False
    while(True):
        #lấy ảnh video trong 1s
        video=getvideo()
        #gửi video lên server
        sendvideo(video)
        currentvideo.append(video)
        res=receive_respond()
        if res['loi']=='conglung':
            playrecord('conglung')
            has_false=True
            break

    if has_false:
        playvideo(currentvideo)
    else:
        if i ==len(dongtacs):
            print("chuc mung ban")
            break
        else:
            i+=1


