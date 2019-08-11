

def checkerror(previouspose,batch_poses,dongtac,batch_id):
    if dongtac=='01':
        pass
    if dongtac=='02':
        pass
    if dongtac=='05':
        count_fail_batch=0
        for batch in previouspose:
            for pose in batch:
                if abs(batch[pose]['LKnee'][0] - batch[pose]['LBigToe'][0]) > 10:
                    count_fail_batch+=1
                    break

        print(count_fail_batch,len(previouspose))
        if count_fail_batch>0.5*len(previouspose)  and count_fail_batch>5:
            return {'correct':False,'error_type':'saichan'}
    return {'correct':True}

dongtacs=['05']

import json

tocdo=12
def getbatchposes(poses,tocdo,batch_id):
    ans={}
    for i in range(tocdo):
        ans[batch_id*tocdo+i]=poses[batch_id*tocdo+i]

    return ans
    pass

def convert_poses(poses):
    ans={}
    i=0
    for key in poses.keys():
        ans[i]=poses[key]
        i+=1
    return ans
for dongtac in dongtacs:
    # print(dongtac)
    poses=json.load(open("./data/"+dongtac+'/false_changapqua_01.json'))
    poses=convert_poses(poses)
    # print(poses)

    current_all_poses=[]
    for i in range(0,int(130/tocdo)):
        batch_poses=getbatchposes(poses,tocdo,batch_id=i)
        current_all_poses.append(batch_poses)
        result=checkerror(current_all_poses,batch_poses,dongtac,batch_id=i)
        print('respond result',result)







