def test(x):
    if 'lizhe' in x:
        return True
    return False

imagelist = ['lizhe best', 'never lose']
imagelistnew = [ x for x in imagelist if test(x)]

print imagelistnew
