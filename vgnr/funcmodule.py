from classmodule import Vigenere

def fire( n_arg ):


    vigenere = Vigenere( n_arg.key )

    if(n_arg.decrypt):

        output = vigenere.decode( n_arg.decrypt )
        way = 'decrypt'
        input = n_arg.decrypt

    elif(n_arg.encrypt):

        output = vigenere.encode( n_arg.encrypt )
        way = 'encrypt'
        input = n_arg.encrypt

    if(n_arg.quiet):

        print('''
        - The given key is  : {}
        - The output is {}
        '''.format(n_arg.key, output) )

    elif(n_arg.verbose):

        print('''
        ------------------------------------------------------------------
        {}
        ------------------------------------------------------------------
        '''.format(vigenere.getTable() ) )

        print('''
        ------------------------------------------------------------------
        - The given key is  : {}
        - My job way to {} the given string  : {}
        ------------------------------------------------------------------
        - The output is {}
        '''.format(n_arg.key, way, input, output) )
    else:
        print('''
        - The given key is  : {}
        - My job way to {} the given string  : {}
        ------------------------------------------------------------------
        - The output is {}
        '''.format(n_arg.key, way, input, output) )
