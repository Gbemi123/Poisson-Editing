
def laplace(src,index):
    i, j= index
    value= (4*src[i,j])-(1 * src[i + 1, j]) - (1 * src[i - 1, j]) - (1 * src[i, j + 1]) - (
                1 * src[i, j - 1])
   
    return value  
