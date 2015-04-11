import os
input_file='test.txt'
def compress(input_file):

    f=open(input_file,'r+')
    content=f.read()
    content=content.replace("\n",'')
    f.close()
    
    contentlist=content.split(' ')
    content_solver={} 
    count=1

    for i in contentlist:
        if(i not in content_solver):
           content_solver[i]=str(count)
           count+=1
           
    for i in range(0,len(contentlist)):
        contentlist[i]=content_solver[contentlist[i]]

    content_compressed=" ".join(contentlist)
    

    f1=open('key.txt','w+')
    for i in content_solver:
        t=i + '###' +content_solver[i]+'!$!'
        f1.writelines(t)
    f1.close()
    
    f2=open(input_file[0:-4]+'-compressed.txt','w+')
    f2.write(content_compressed)
    f2.close()
    print "Compression complete!"

compress(input_file)


input_file_compressed=input_file[0:-4]+'-compressed.txt'
key='key.txt'

def uncompress(input_file_compressed,key):

    f=open(key,'r+')
    content_comp=f.read()
    f.close()
    
    content_comp=content_comp.replace('!$!','\n')
    
    f_temp_write=open('temp.txt','w+')
    f_temp_write.write(content_comp)
    f_temp_write.close()

    f_temp_read=open('temp.txt','r+')
    content_solver_uncompress={}

    for i in f_temp_read.readlines():
        
        i=i.replace("\n",'')
        l=i.split('###')
        content_solver_uncompress[l[1]]=l[0]

    f_temp_read.close()
    os.remove('temp.txt')

    f1=open(input_file_compressed,'r+')
    content_compressed=f1.read()
    f1.close()

    content_compressed=content_compressed.replace('\n','')
    content_compressed_list=content_compressed.split(' ')

    for i in range(0,len(content_compressed_list)):
        content_compressed_list[i]=content_solver_uncompress[content_compressed_list[i]]
    content_normal=" ".join(content_compressed_list)

    f2=open(input_file_compressed[0:-4]+'-normal.txt','w+')
    f2.write(content_normal)
    f2.close()
    print "Uncompression complete!"
    os.remove(key)
    
uncompress(input_file_compressed,key)

    
    
    
    
        
        

