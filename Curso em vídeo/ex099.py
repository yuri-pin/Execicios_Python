
def maior(*núm):
    if len(núm) == 1:
        mai = núm[0]
    elif len(núm) > 1:
        mai = núm[0]
        for k in range(1,len(núm)):
            if núm[k]> mai:
                mai = núm[k]
    print(f'O maior número é {mai}')

maior(5, 6, 9, 1)


