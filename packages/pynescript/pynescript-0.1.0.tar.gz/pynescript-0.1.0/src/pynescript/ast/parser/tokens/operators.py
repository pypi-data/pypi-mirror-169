from pyparsing import Literal


ASSIGN = Literal("=")
NEQ = Literal("!=")
MOD = Literal("%")
MOD_ASSIGN = Literal("%=")
MUL = Literal("*")
MUL_ASSIGN = Literal("*=")
ADD = Literal("+")
ADD_ASSIGN = Literal("+=")
SUB = Literal("-")
SUB_ASSIGN = Literal("-=")
DIV = Literal("/")
DIV_ASSIGN = Literal("/=")
LT = Literal("<")
LE = Literal("<=")
EQ = Literal("==")
GT = Literal(">")
GE = Literal(">=")
QUESTION = Literal("?")
COLON = Literal(":")
COLON_ASSIGN = Literal(":=")
LBRACKET = Literal("[")
RBRACKET = Literal("]")
