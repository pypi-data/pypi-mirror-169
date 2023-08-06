import os
import shutil
from bokeys import compute_info
from bokeys import data_pre
from bokeys import run_model
import time



def running(file_name,workdir,split=None,model=None,FP=None, cpus=1):
    split = split if type(split) != type(None) else ['random']
    model = model if type(model) != type(None) else ['SVM']
    FP = FP if type(FP) != type(None) else ['MACCS']
    FP_list = ['2d-3d','MACCS','ECFP4','pubchem']
    split_list = ['random', 'scaffold', 'cluster']
    model_list = ['SVM','KNN','DNN','RF','XGB','gcn','gat','attentivefp','mpnn']
    assert len(set(split) - set(split_list)) == 0, '{} element need in {}'.format(split, split_list)
    assert len(set(model)-set(model_list))==0,'{} element need in {}'.format(model ,model_list)
    assert len(set(FP) - set(FP_list)) == 0, '{} element need in {}'.format(FP, FP_list)
    if not os.path.exists(workdir):
        os.makedirs(workdir)
    assert len(set(list([file_name.split('.')[-1]])) -set(list(['csv','txt','tsv'])))==0, '{} need in ["csv","txt","tsv"]'.format(file_name.split('.')[-1])
    dataset = file_name.split('/')[-1].split('.'+file_name.split('.')[-1])[0]
    dir_path = os.path.join(workdir, dataset)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file = os.path.join(dir_path, dataset + '.csv')
    shutil.copy(file_name, os.path.join(dir_path,dataset + '.csv'))
    data_pre.start(file, des=[])
    mpl = True if cpus>1 else False
    run_model.main(file, split, FP, model, cpus, mpl, 'cpu')
    compute_info.get_info(file_name=file, models=model, split=split, FP=FP)
    compute_info.para(file_name=file)

if __name__ == '__main__':
    running('/data/jianping/bokey/OCAICM/dataset/GLS1/GLS1.csv','/data/jianping/web-ocaicm/OCAICM/dataset/')

# if __name__ == '__main__':
#     # old_file = '../library/plus+/chembl31.csv'
#     #
#     # # mkdir + amend file name
#     # suffix = '_' + str(time.time())
#     # dataset = old_file.split('/')[-1].split('.csv')[0] + suffix
#     # new_file = dataset + '.csv'
#
#     file = '/data/jianping/bokey/OCAICM/dataset/chembl31/chembl31.csv'
#     # dir_path = os.path.join('./dataset', dataset)
#     # if not os.path.exists(dir_path):
#     #     os.mkdir(dir_path)
#     # shutil.copy(old_file, os.path.join(dir_path, new_file))
#     # file = os.path.join(dir_path, new_file)
#
#
#     # parameter set,'2d-3d'
#     split, FP, model  = ['random','cluster','scaffold'], ['ECFP4','MACCS'], ['SVM','KNN','RF','XGB']
#
#     # data prepare
#
#     data_pre.start(file,des = [])
#
#     cpus, mpl, device = 8, True, 'cpu'
#     # model running
#     run_model.main(file, split, FP, model, cpus, mpl, device)
#
#     # info output
#     compute_info.get_info(file_name=file, models=model, split=split, FP=FP)
#     compute_info.para(file_name=file)
#
#
#     #start 2022/9/19 15:04  30-50cpu
#     # 16:11 2d-3d 1451/7921