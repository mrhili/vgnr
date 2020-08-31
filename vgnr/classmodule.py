import string

class Vigenere():
    def __init__(self, key ):
        self.key = self.prepare( key )
        self.decoded = ''
        self.encoded = ''

        self.lenght_error = '''
        lenght error th fiven key lenght should be the same as the given input
        -h to seek the help
        '''

        #self.table = {}
        self.a2z = string.ascii_lowercase[:26]
        self.z2a = string.ascii_lowercase[:26]

        self.table = {}

        self.table_rep = '''
        ----A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        +----------------------------------------------------
        A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
        C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
        D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
        E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
        F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
        G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
        H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
        I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
        J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
        K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
        L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
        M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
        N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
        O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
        P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
        Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
        R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
        S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
        T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
        U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
        V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
        W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
        X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
        Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
        Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
        '''

        self.fillTable()
    def prepare(self, str):
        str = str.lower()
        prepared = str.translate(str.maketrans('', '', string.punctuation))

        return prepared

    def getTable(self):


        return self.table_rep

    def fillTable(self):


        #INIT
        for char in self.a2z:
            self.table[char] = {}

        for char in self.a2z:
            for i, char2 in enumerate( self.a2z , start=0 ):
                self.table[char][char2] = self.z2a[ i ]

            toPop = self.z2a[0]
            self.z2a = self.z2a[1:] + toPop

    def decode(self, cypher):
        cypher = self.prepare( cypher )
        if len( self.key ) == len( cypher ):


            for i, char in enumerate( self.key , start=0 ) :

                column2search = self.table[char]

                cypher_char = cypher[i]
                #print( char )
                #print( column2search )

                column2search_values = list( column2search.values() )

                #print( char+' _values' )
                #print( column2search_values )

                #print( 'trying 2 find mirror index' )
                index = column2search_values.index( cypher_char )
                #print( index )



                #print( 'trying 2 find mirror ' )


                self.decoded+= string.ascii_lowercase[index]

            return self.decoded



        else:
            return self.lenght_error



    def encode(self, word):
        word = self.prepare( word )
        if len( self.key ) == len( word ):


            for i, char in enumerate( self.key , start=0 ) :

                column2search = self.table[char]

                cypher_char = word[i]



                self.encoded+= column2search[cypher_char]

            return self.encoded

        else:
            return self.lenght_error
