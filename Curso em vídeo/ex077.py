palavras = ('aprender', 'python')
for c in range (0, int(len(palavras))):
    print(f'\nNa palavra {palavras[c].upper()} temos ', end='')
    for a in range(0, int(len(palavras[c]))):
        if (palavras[c].lower())[a] in 'aeiou':
            print((palavras[c].lower())[a], end=' ')