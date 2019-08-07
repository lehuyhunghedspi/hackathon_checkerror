
def receive_video():
    pass

def detecthumanpose():
    pass
def checkerror(previouspose,pose,dongtac):
    pass
def send_feedback(result):
    pass
def newprocess(connect):
    dongtacs = ['01', '02']

    i = 0
    while (True):
        dongtac = dongtacs[i]
        previouspose=[]
        has_false=False
        while (True):
            # lay video tu client
            video = receive_video()
            # detect human pose

            poses=detecthumanpose(video)
            previouspose.extend(poses)
            check_result=checkerror(previouspose,poses,dongtac)
            send_feedback(check_result)
            if check_result['has_error']==True:
                has_false=True
                break

        if has_false:
            pass
        else:
            if i == len(dongtacs):
                print("chuc mung ban")
                exit()
                break
            else:
                i += 1

    pass

def getconnect():
    pass

def createnewprocess(newconnect):
    pass
while(True):
    newconnect=getconnect()
    createnewprocess(newconnect)