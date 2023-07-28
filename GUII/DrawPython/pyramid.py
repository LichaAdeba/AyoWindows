import string
def drawPyramid(rows):
    result = string.ascii_lowercase
    if rows == 0:
        return
    else:
        drawPyramid(rows- 1)
        s1 = slice(1)
        s2 = slice(2)
        print(result[s1] *rows)
if __name__=='__main__':
    rows = 13
    drawPyramid(rows)