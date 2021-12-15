# %%
def imageDecrypt(fin, fout):
    with open(fin, 'rb') as dat:
        out=fout+'.jpg'
        with open(out, 'wb') as jpg:
            hByte=dat.read(2)
            print(hByte)
            code=list()
            for i in range(2):
                code.append(hByte[i] ^ [0xff,0xd8][i])
            wd=code[0]
            # wd=int(wd)
            # print(code)
            print(bytes(code))
            dat.seek(0)
            for now in dat:
                for nowByte in now:
                    # print(nowByte," ")
                    newByte=nowByte ^ wd
                    newByte=bytes([newByte])
                    # print(newByte)
                    jpg.write(newByte)
                    
# fin=['44e5b6b465e6fcf3788b6704b22d943d.dat','44226c511276a7f74caf2931187cbff9.dat','c8d82dd0591c404ed416419327077485.dat','ec9f6d7ebe3dacc7c13c978d65c3eb50.dat']
# fout=['44e5b6b465e6fcf3788b6704b22d943d','44226c511276a7f74caf2931187cbff9','c8d82dd0591c404ed416419327077485','ec9f6d7ebe3dacc7c13c978d65c3eb50']

# %%
import os
os.listdir()
fin=list()
for file in os.listdir():
    if '.dat' in file:
        fin.append(file)
fout=[i[:-4] for i in fin]
for i in range(len(fin)):
    imageDecrypt(fin[i], fout[i])

# %%
# def imageDecode(f,fn):
#     dat = open(f, "rb")
#     out = fn + ".png"
#     png = open(out, "wb")
#     for now in dat:
#         for nowByte in now:
#             newByte = nowByte ^ 0xb7 #修改为自己的解密码
#             png.write(bytes([newByte]))
#     dat.close()
#     png.close()

# f='44e5b6b465e6fcf3788b6704b22d943d.dat'
# fn='44e5b6b465e6fcf3788b6704b22d943d'
# imageDecode(f,fn)


