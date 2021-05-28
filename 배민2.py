

import sys

def solution(S):
    S = list(map(str,S.split('\n')))
    music=0
    images = 0
    movies = 0
    other = 0
    for fileinfo in S:
        file,size = map(str,fileinfo.split())
        filetype = file.split('.')[-1]
        size = int(size[:-1])
        if filetype in ['mp3','acc','flac']:
            music+=size
        elif filetype in ['jpg', 'bmp', 'gif']:
            images+=size
        elif filetype in ['mp4', 'avi', 'mkv']:
            movies+=size
        else:
            other+=size

    filetypelist=['music','images','movies','other']
    filesizelist = [music, images, movies, other]

    resultstr =''
    for idx in range(4):
        resultstr += filetypelist[idx] + ' ' +str(filesizelist[idx]) + 'b'+'\n'
    return resultstr[:-1]

S = open('input.txt').read()
print(solution(S))


