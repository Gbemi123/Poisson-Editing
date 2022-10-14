def gradient(im,index):
    i,j=index

    right = 1* (im[i+1,j])
    left = -1 * (im[i-1,j])
    down = 1 * (im[i,j+1])
    up = -1 * (im[i,j-1])
    
    value=right+left+down+up

    return value
