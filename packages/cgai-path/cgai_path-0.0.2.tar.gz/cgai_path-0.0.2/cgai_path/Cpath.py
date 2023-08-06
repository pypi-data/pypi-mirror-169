from genericpath import isfile
import os
import re
import glob 



class CGAIPATH(object):

    def __init__(self):
        pass



    def isSequence(self,path,_type=''):
        """
        判定该路径是否为一个序列路径
        path: 输入文本路径
        _type: 可以指定文件类型,需带.,不指定则全部识别 比如： .exr 
        """
        result = False
        pt = '(.*)(%\d+d).*' if not _type else '(.*)(%\d+d).*\\'+_type
        groups = re.match(pt,path)
        try:
            pre = groups.group(1)
            patter = groups.group(2)
            result = pre,patter
        except Exception as ERR:
            print(ERR)
        
        return result

    def get_pnum(self,patter):
        """
        获取匹配中的字符数值
        """
        result = False
        try:
            g = re.match('.*%(\d+).*',patter)
            result = g.group(1)
        except Exception as NUMERR:
            print(NUMERR)

        return result

    def get_files(self,path,missing=True):
        """
        获取路径下的所有文件路径
        """
        fpaths = []
        missing_files = []
        pre,patter = self.isSequence(path)
        if patter:  # 序列路径
            dir_path,file_name = os.path.split(path)
            count = int(self.get_pnum(patter))
            file_name = file_name.replace(patter,'?'*count) 
            fs = glob.glob(os.path.join(dir_path,file_name))
            fpaths = sorted(fs)
            if missing:
                missing_files = self.get_missing_files(path,patter,fpaths)
                
        else:
            if os.path.isdir(path): # 目录
                fpaths = [os.path.join(path,i) for i in path if os.path.isfile(os.path.join(path,i))]
            elif os.path.isfile(path): # 本身是文件
                fpaths = [path]
        if missing:
            return fpaths,missing_files
        else:
            return fpaths

    def get_filename(self,path,ignores=['.','_']):
        """
        传入路径获取当前文件除去序列的名称
        path : 传入的路径
        ignores: 忽略的前缀
        """
        filename = ''
        if os.path.isfile(path):
            filename = os.path.basename(path)
            return os.path.splitext(filename)[0]
        result = self.isSequence(path)
        if result:
            pre,patter = result
            name = os.path.basename(pre)
            if name[-1] in ignores:
                filename = name[:-1]

        return filename


    def get_missing_files(self,ori_path,patter,paths):
        """
        获取缺失的文件路径
        ori_path: 原始格式化路径
        patter: 匹配格式
        paths: 查询到的当前所有文件路径
        """
        pre,_tail = ori_path.split(patter)
        numbers = []
        for path in paths:
            number = path.replace(pre,'').replace(_tail,'')
            numbers.append(int(number))
        min_num = min(numbers)
        max_num = max(numbers)
        miss_files = []
        for i in range(min_num,max_num+1):
            upath = pre + patter%i + _tail
            if upath not in paths:
                miss_files.append(upath)

        return miss_files