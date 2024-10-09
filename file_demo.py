# f = open('no.txt', 'r')
# f.close()
# with open('no.txt', 'r') as f:
#     
# f.contents = f.readline()
#     print(f.contents)
# for line in f:
#         print(line,end ='')
with open('me.jpg', 'rb') as rf:
    with open('me_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
        # for line in rf:
        #     wf.write(line)
    
    # f.write('Test chill boi')
    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents,end= '')
    # f.seek(0)
    # f_contents = f.read(size_to_read)
    # print(f_contents,end= '')
    # # print(f.tell())

    # # while len(f_contents) > 0:
    # #     print(f_contents,end = '*')
    # #     f_contents = f.read(size_to_read)
        