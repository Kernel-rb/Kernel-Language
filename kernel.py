# somesheet to know before strating : 
# Lexer howa l'analyseur lexical dyalna , howa li aykhlina n3rf l tt dyal les tokens 
# TODO : Create a Token Class  :
# TODO : Error Class :

"""
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'{self.error_name} : {self.details}'
        return result

class illegalCharError(Error):
    def __init__(self, details):
        super().__init__('illegal character', details) # super() howa class parent dyal illegalCharError

"""

# tt hiya token type 
digits = '0123456789'
tt_integer = 'INTEGER'
tt_float  = 'FLOAT'
tt_plus   = 'PLUS' 
tt_minus  = 'MINUS'
tt_mul    = 'MUL'
tt_div    = 'DIV'
tt_lparen = 'LPAREN'
tt_rparen = 'RPAREN'





class Token:
    def __init__(self, type, value=None):
        # init howa constructeur dyal l'objet ; for example : Token(INTEGER, 3)
        self.type = type
        self.value = value
    def __repr__(self):
        # repr howa representation dyal l'objet ; for example : <Token:INTEGER, 3>
        return f'{self.type}:{self.value}' if self.value else f'{self.type}'
    
# lexer class howa class dyal l'analyseur lexical 

class lexer : 
    def __init__(self , text):
        self.text = text
        self.pos = -1             # drna -1 bach nbdaw mn 0
        self.current_char = None  # drna None bach nbdaw mn ''
        self.advance()            # advance() howa fonction dyal advance
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None # bach n3rfu wach kayn char f text wla la

    def make_tokens(self):
        Tokens = []
        while self.current_char != None:  # bach n3rfo bli bdina f text wla la
            if self.current_char in ' \t':    # hna kan7aydo les espaces 
                self.advance()
            elif self.current_char == "+" :
                Tokens.append(Token(tt_plus))
                self.advance()
            elif self.current_char == "-" :
                Tokens.append(Token(tt_minus))
                self.advance()
            elif self.current_char == "*" :
                Tokens.append(Token(tt_mul))
                self.advance()
            elif self.current_char == "/" :
                Tokens.append(Token(tt_div))
                self.advance()
            elif self.current_char == "(" :
                Tokens.append(Token(tt_lparen))
                self.advance()
            elif self.current_char == ")" :
                Tokens.append(Token(tt_rparen))
                self.advance()
            elif self.current_char.isdigit() : # isdigit() howa fonction dyal python li kay3rf wach kayn char f text wla la
                Tokens.append(self.make_number()) # make_number() howa fonction dyalna ttdir l'analyse dyal les nombres
            else:
                # char = self.current_char
                # self.advance()
                # return [], illegalCharError("'" + char + "'")
                char = self.current_char
                self.advance()
                return [], Exception(f"'{char}'")
        return Tokens
    
    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in f'{digits}.':
            if self.current_char == '.' :
                if dot_count == 1 : break # 7it number fih 1 point
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
            if dot_count == 0 :
                return Token(tt_integer, int(num_str)) 
            else:
                return Token(tt_float, float(num_str))

# Run :
def run(text):
    lexer_instance = lexer(text)
    return lexer_instance.make_tokens()