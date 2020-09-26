import os
import shutil

KeyWordDic = {
    '图像增强': ['Inpainting','Denoising','Restoration','Resolution','Demosaicing'],
    '风格迁移': ['Style','Translation','GAN','Face','Editing','Attribution'],
    '目标检测': ['Detection','Stage','Anchor','Object','Detecor'],
    '架构搜索': ['Prune','Compress','NAS','Architecture'],
    '元学习': ['Meta','FSL','Continual','Incremental','Few','Shot','Embedding','Learn'],
    '图学习': ['Graph','GNN','Embedding'],
    '图像超分': ['Resolution'],
    '图像去噪': ['Deraining','Deraindrop','Deblurring','Dehaze','Reflection','Shadow'],
    '网络剪枝': ['Prune','Pruning','Distillation'],
    '对抗学习': ['Adversarial','Attack','Target','Untarget','Perturbation','black'],
    '对抗去噪': ['Defense','Adversarial','Denoising','Example']
}

FileNameDic = {
    '图像增强':[],
    '风格迁移':[],
    '目标检测':[],
    '架构搜索':[],
    '元学习': [],
    '图学习': [],
    '图像超分':[],
    '图像去噪':[],
    '网络剪枝':[],
    '对抗学习':[],
    '对抗去噪':[]
}


# 文件过滤器：根据关键词筛选各个方向的论文的pdf文件，并移动到相应文件夹中
def filefilter(file_path,head):
    tempfilename = os.listdir(file_path)#获取pdf文件列表
    # print(len(tempfilename))

    #截取文件名
    for i in range(len(tempfilename)):
        tailindex = tempfilename[i].rfind('.')
        filenameraw = tempfilename[i][len(head):tailindex]
        filename = filenameraw.split('-')
        for key in KeyWordDic :
            # print()
            for j in KeyWordDic[key]:
                if j in filename:
                    FileNameDic[key].append(filenameraw)

    # 生成目录索引TXT文件
    outfile = 'out.txt'

    with open(outfile,'w',encoding='utf-8') as file_handle:
        for key in FileNameDic:
            file_handle.write("{}:\n".format(key))
            # print(key+':'+str(len(FileNameDic[key])))
            for i in FileNameDic[key]:
                file_handle.write("{}\n".format(i))
            file_handle.write("\n")

    #移动文件
    for key in FileNameDic:
        temppath = key
        for i in FileNameDic[key]:
            oldfile = file_path+"\\"+head+i+'.pdf'
            newfile = os.path.join(temppath,head+i+'.pdf')
            if not os.path.exists(newfile):
                shutil.copyfile(oldfile,newfile)

    
# 创建文件夹，移动文件
def v_mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+"创建成功")
        return True
    else:
        print(path+"目录已存在")
        return False

if __name__ == "__main__":
    """
    1. 修改file_path为论文pdf文件所在文件夹
    2. 修改head为文件前缀
    3. 更新KeyWordDic部分关键词
    """

    # 文件路径
    file_path = r"D:\200-Study-学习文件\240-Learning-Master\01-论文\03-最新\2020\ICML2020"
   
    # 文件前缀，如：ICML-2020-Educating-Text-Autoencoders-Latent-Representation-Guidance-Via-Denoising.pdf
    head = 'ICML-2020-'
    
    # 创建目录
    for path in FileNameDic:
        v_mkdir(path)
    
    # 筛选文件
    filefilter(file_path,head)
