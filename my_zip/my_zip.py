import zipfile as zf
import pyinputplus as pyip
def menu():
    print('='*40)
    print('='*12+"     my_zip     "+'='*12)
    print("========   1.压缩    2.解压缩   ========")
    print('='*40)
    
def compre(path,name):
    newzip=zf.ZipFile(name+'.zip','w')
    newzip.write(path,compress_type=zf.ZIP_DEFLATED)
    newzip.close()

def decomp(path,name):
    decomf=zf.ZipFile(path)
    decomf.extractall(name)
    decomf.close()
    
def main():
    while True:
        ans=pyip.inputChoice(['1','2'],prompt="请选择：")
        path=input("请输入操作文件的路径：")
        name=input("请输入目的地文件路径:(如果为空格则以操作文件命名)")
        if name==' ':
            name=path.split('.')[0]
        if ans=='1':
            compre(path,name)
        else:
            decomp(path,name)
        choi=pyip.inputChoice(['y','n'],prompt="是否继续(y/n)")
        if choi=='n':
            break

if __name__ == "__main__":
    menu()
    main()
