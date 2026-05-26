"""
Budega Programming Language Translator
Traduz código Budega para C
"""

import re
import sys
import os
from typing import List, Tuple, Optional
from enum import Enum, auto


class TokenType(Enum):
    # Tipos primitivos
    INTEIRINHO = auto()
    BANDA = auto()
    TAIADA = auto()
    GARRANCHO = auto()
    APOIS = auto()
    NADINHA = auto()

    # Valores booleanos
    VALENDO = auto()
    NEM = auto()

    # Modificadores
    UM = auto()
    UMA = auto()
    BOCADO = auto()
    RUMA_DE = auto()
    ACOLA = auto()
    DE = auto()
    NUM_MEXE = auto()

    # Operadores lógicos
    AI_DENTRO = auto()
    EMENDA = auto()
    MOI = auto()
    IMPLICA = auto()
    FRESCA = auto()

    # Estruturas condicionais
    SE_DER = auto()
    SE_NUM_DER = auto()
    ESCOLHE_AI = auto()
    CAUSO = auto()
    SE_NUM_TIVER = auto()

    # Estruturas de repetição
    ARRUDEIA = auto()
    FAZ_AI = auto()
    PRA = auto()
    PRA_CADA = auto()
    EM = auto()

    # Controle de fluxo
    PASSA_RETO = auto()
    ARREDA = auto()
    DEVOLVE = auto()

    # Funções
    PELEJA = auto()
    BERRA = auto()
    ESCUTA = auto()

    # Operadores
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LTE = auto()
    GTE = auto()
    ASSIGN = auto()

    # Delimitadores
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    SEMICOLON = auto()
    COMMA = auto()
    COLON = auto()

    # Outros
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    CHAR = auto()
    EOF = auto()


class Token:
    def __init__(self, type_: TokenType, value: str, line: int, column: int):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, {self.line}:{self.column})"


class Lexer:
    KEYWORDS = {
        'inteirinho': TokenType.INTEIRINHO,
        'banda': TokenType.BANDA,
        'taiada': TokenType.TAIADA,
        'garrancho': TokenType.GARRANCHO,
        'apois': TokenType.APOIS,
        'nadinha': TokenType.NADINHA,
        'valendo': TokenType.VALENDO,
        'nem': TokenType.NEM,
        'um': TokenType.UM,
        'uma': TokenType.UMA,
        'bocado': TokenType.BOCADO,
        'ruma': TokenType.IDENTIFIER,  # Será tratado especialmente
        'de': TokenType.DE,
        'acolá': TokenType.ACOLA,
        'num_mexe': TokenType.NUM_MEXE,
        'ai_dentro': TokenType.AI_DENTRO,
        'emenda': TokenType.EMENDA,
        'mói': TokenType.MOI,
        'implica': TokenType.IMPLICA,
        'fresca': TokenType.FRESCA,
        'se_der': TokenType.SE_DER,
        'se_num_der': TokenType.SE_NUM_DER,
        'escolhe_ai': TokenType.ESCOLHE_AI,
        'causo': TokenType.CAUSO,
        'se_num_tiver': TokenType.SE_NUM_TIVER,
        'arrudeia': TokenType.ARRUDEIA,
        'faz_ai': TokenType.FAZ_AI,
        'pra': TokenType.PRA,
        'pra_cada': TokenType.PRA_CADA,
        'em': TokenType.EM,
        'passa_reto': TokenType.PASSA_RETO,
        'arreda': TokenType.ARREDA,
        'devolve': TokenType.DEVOLVE,
        'peleja': TokenType.PELEJA,
        'berra': TokenType.BERRA,
        'escuta': TokenType.ESCUTA,
    }

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def error(self, msg: str):
        raise SyntaxError(f"Erro léxico na linha {self.line}, coluna {self.column}: {msg}")

    def peek(self, offset: int = 0) -> Optional[str]:
        pos = self.pos + offset
        if pos < len(self.source):
            return self.source[pos]
        return None

    def advance(self) -> Optional[str]:
        if self.pos < len(self.source):
            char = self.source[self.pos]
            self.pos += 1
            if char == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            return char
        return None

    def skip_whitespace(self):
        while self.peek() and self.peek() in ' \t\n\r':
            self.advance()

    def skip_comment(self):
        if self.peek() == '/' and self.peek(1) == '/':
            while self.peek() and self.peek() != '\n':
                self.advance()
            return True
        elif self.peek() == '/' and self.peek(1) == '*':
            self.advance()  # /
            self.advance()  # *
            while True:
                if self.peek() is None:
                    self.error("Comentário não fechado")
                if self.peek() == '*' and self.peek(1) == '/':
                    self.advance()  # *
                    self.advance()  # /
                    break
                self.advance()
            return True
        return False

    def read_number(self) -> Token:
        start_line, start_col = self.line, self.column
        num_str = ''

        while self.peek() and (self.peek().isdigit() or self.peek() == '.'):
            num_str += self.peek()
            self.advance()

        return Token(TokenType.NUMBER, num_str, start_line, start_col)

    def read_string(self) -> Token:
        start_line, start_col = self.line, self.column
        quote = self.advance()  # " ou '
        string_val = ''

        while self.peek() and self.peek() != quote:
            if self.peek() == '\\':
                self.advance()
                next_char = self.advance()
                if next_char == 'n':
                    string_val += '\\n'
                elif next_char == 't':
                    string_val += '\\t'
                elif next_char == '\\':
                    string_val += '\\\\'
                elif next_char == quote:
                    string_val += quote
                else:
                    string_val += next_char
            else:
                string_val += self.peek()
                self.advance()

        if self.peek() != quote:
            self.error("String não fechada")

        self.advance()  # Fecha a string
        return Token(TokenType.STRING, string_val, start_line, start_col)

    def read_identifier(self) -> Token:
        start_line, start_col = self.line, self.column
        ident = ''

        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            ident += self.peek()
            self.advance()

        # Verifica se é "ruma de"
        if ident == 'ruma':
            saved_pos = self.pos
            saved_line = self.line
            saved_col = self.column

            self.skip_whitespace()

            if self.peek() == 'd' and self.peek(1) == 'e':
                self.advance()
                self.advance()
                # Verifica se não faz parte de outra palavra
                if self.peek() is None or not self.peek().isalnum():
                    return Token(TokenType.RUMA_DE, 'ruma de', start_line, start_col)

            # Restaura posição se não for "ruma de"
            self.pos = saved_pos
            self.line = saved_line
            self.column = saved_col

        token_type = self.KEYWORDS.get(ident, TokenType.IDENTIFIER)
        return Token(token_type, ident, start_line, start_col)

    def tokenize(self) -> List[Token]:
        while self.pos < len(self.source):
            self.skip_whitespace()

            if self.pos >= len(self.source):
                break

            if self.skip_comment():
                continue

            char = self.peek()

            # Números
            if char.isdigit():
                self.tokens.append(self.read_number())

            # Strings
            elif char == '"':
                self.tokens.append(self.read_string())

            # Caracteres
            elif char == "'":
                start_line, start_col = self.line, self.column
                self.advance()  # '
                char_val = self.peek()
                self.advance()
                if self.peek() != "'":
                    self.error("Caractere não fechado")
                self.advance()  # '
                self.tokens.append(Token(TokenType.CHAR, char_val, start_line, start_col))

            # Identificadores e palavras-chave
            elif char.isalpha() or char == '_':
                self.tokens.append(self.read_identifier())

            # Operadores de dois caracteres
            elif char == '=' and self.peek(1) == '=':
                start_line, start_col = self.line, self.column
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.EQ, '==', start_line, start_col))

            elif char == '!' and self.peek(1) == '=':
                start_line, start_col = self.line, self.column
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.NEQ, '!=', start_line, start_col))

            elif char == '<' and self.peek(1) == '=':
                start_line, start_col = self.line, self.column
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.LTE, '<=', start_line, start_col))

            elif char == '>' and self.peek(1) == '=':
                start_line, start_col = self.line, self.column
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.GTE, '>=', start_line, start_col))

            # Operadores simples
            elif char == '=':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.ASSIGN, '=', start_line, start_col))

            elif char == '+':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.PLUS, '+', start_line, start_col))

            elif char == '-':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.MINUS, '-', start_line, start_col))

            elif char == '*':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.STAR, '*', start_line, start_col))

            elif char == '/':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.SLASH, '/', start_line, start_col))

            elif char == '%':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.PERCENT, '%', start_line, start_col))

            elif char == '<':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.LT, '<', start_line, start_col))

            elif char == '>':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.GT, '>', start_line, start_col))

            # Delimitadores
            elif char == '(':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.LPAREN, '(', start_line, start_col))

            elif char == ')':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.RPAREN, ')', start_line, start_col))

            elif char == '{':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.LBRACE, '{', start_line, start_col))

            elif char == '}':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.RBRACE, '}', start_line, start_col))

            elif char == '[':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.LBRACKET, '[', start_line, start_col))

            elif char == ']':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.RBRACKET, ']', start_line, start_col))

            elif char == ';':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.SEMICOLON, ';', start_line, start_col))

            elif char == ',':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ',', start_line, start_col))

            elif char == ':':
                start_line, start_col = self.line, self.column
                self.advance()
                self.tokens.append(Token(TokenType.COLON, ':', start_line, start_col))

            else:
                self.error(f"Caractere inesperado: {char}")

        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens


class Translator:
    TYPE_MAP = {
        TokenType.INTEIRINHO: 'int',
        TokenType.BANDA: 'float',
        TokenType.TAIADA: 'double',
        TokenType.GARRANCHO: 'char',
        TokenType.APOIS: 'bool',
        TokenType.NADINHA: 'void',
        TokenType.BOCADO: 'long',
    }

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.output = []
        self.includes = set()

    def error(self, msg: str):
        token = self.current()
        raise SyntaxError(f"Erro na linha {token.line}, coluna {token.column}: {msg}")

    def current(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def peek(self, offset: int = 0) -> Token:
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]

    def advance(self) -> Token:
        token = self.current()
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token

    def expect(self, token_type: TokenType) -> Token:
        token = self.current()
        if token.type != token_type:
            self.error(f"Esperado {token_type}, encontrado {token.type}")
        return self.advance()

    def match(self, *token_types: TokenType) -> bool:
        return self.current().type in token_types

    def translate(self) -> str:
        # Processa o programa
        self.translate_program()

        # Monta o código C com includes
        result = []
        result.append('#include <stdio.h>')
        result.append('#include <stdbool.h>')
        result.append('#include <stddef.h>')

        for include in sorted(self.includes):
            result.append(f'#include <{include}>')

        result.append('')
        result.extend(self.output)

        return '\n'.join(result)

    def translate_program(self):
        while not self.match(TokenType.EOF):
            # Declaração de função
            if self.match(TokenType.PELEJA):
                self.translate_function()
            # Variável global
            elif self.match(TokenType.UM, TokenType.UMA, TokenType.NUM_MEXE):
                self.translate_global_variable()
            else:
                self.error(f"Token inesperado no nível global: {self.current().type}")

    def translate_function(self):
        self.expect(TokenType.PELEJA)

        # Tipo de retorno
        return_type = self.translate_type()

        # Nome da função
        func_name = self.expect(TokenType.IDENTIFIER).value

        # Traduz budega_principal para main
        if func_name == 'budega_principal':
            func_name = 'main'

        # Parâmetros
        self.expect(TokenType.LPAREN)
        params = []

        if not self.match(TokenType.RPAREN):
            while True:
                param = self.translate_parameter()
                params.append(param)

                if not self.match(TokenType.COMMA):
                    break
                self.advance()

        self.expect(TokenType.RPAREN)

        # Cabeçalho da função
        params_str = ', '.join(params) if params else 'void'
        self.output.append(f'{return_type} {func_name}({params_str}) {{')

        # Corpo da função
        self.expect(TokenType.LBRACE)
        self.translate_block(indent=1)
        self.expect(TokenType.RBRACE)

        self.output.append('}')
        self.output.append('')

    def translate_parameter(self) -> str:
        # Ignora um/uma
        if self.match(TokenType.UM, TokenType.UMA):
            self.advance()

        # Tipo
        param_type = self.translate_type()

        # Ignora 'de' opcional
        if self.match(TokenType.DE):
            self.advance()

        # Nome
        param_name = self.expect(TokenType.IDENTIFIER).value

        # Ponteiro (acolá)
        if self.match(TokenType.ACOLA):
            self.advance()
            param_type += '*'

        return f'{param_type} {param_name}'

    def translate_type(self) -> str:
        # Modificador long
        is_long = False
        if self.match(TokenType.BOCADO):
            is_long = True
            self.advance()

        # Constante
        is_const = False
        if self.match(TokenType.NUM_MEXE):
            is_const = True
            self.advance()

        # Vetor (ruma de)
        if self.match(TokenType.RUMA_DE):
            type_info = self.translate_array_type()
            if is_const:
                base_type, dimensions = type_info
                return ('const ' + base_type, dimensions)
            return type_info

        # Tipo base
        type_token = self.current()
        if type_token.type in self.TYPE_MAP and type_token.type != TokenType.BOCADO:
            base_type = self.TYPE_MAP[type_token.type]
            self.advance()
        else:
            self.error(f"Tipo esperado, encontrado {type_token.type}")

        # Monta o tipo
        result = ''
        if is_const:
            result += 'const '
        if is_long:
            result += 'long '
        result += base_type

        return result

    def translate_array_type(self) -> str:
        self.expect(TokenType.RUMA_DE)

        # Dimensões do array
        dimensions = []

        while self.match(TokenType.LBRACKET):
            self.advance()
            size = self.expect(TokenType.NUMBER).value
            self.expect(TokenType.RBRACKET)
            dimensions.append(size)

        # Tipo base
        base_type = self.translate_type()

        return (base_type, dimensions)

    def translate_global_variable(self):
        line = self.translate_variable_declaration()
        self.output.append(line)

    def translate_block(self, indent: int = 0):
        indent_str = '    ' * indent

        while not self.match(TokenType.RBRACE, TokenType.EOF):
            # Declaração de variável
            if self.match(TokenType.UM, TokenType.UMA, TokenType.NUM_MEXE):
                line = self.translate_variable_declaration()
                self.output.append(indent_str + line)

            # Estrutura condicional
            elif self.match(TokenType.SE_DER):
                self.translate_if_statement(indent)

            # Switch
            elif self.match(TokenType.ESCOLHE_AI):
                self.translate_switch_statement(indent)

            # While
            elif self.match(TokenType.ARRUDEIA):
                # Verifica se é do-while (vem depois de faz_ai)
                self.translate_while_statement(indent)

            # Do-while
            elif self.match(TokenType.FAZ_AI):
                self.translate_do_while_statement(indent)

            # Foreach
            elif self.match(TokenType.PRA_CADA):
                self.translate_foreach_statement(indent)

            # For
            elif self.match(TokenType.PRA):
                self.translate_for_statement(indent)

            # Controle de fluxo
            elif self.match(TokenType.PASSA_RETO):
                self.advance()
                self.expect(TokenType.SEMICOLON)
                self.output.append(indent_str + 'continue;')

            elif self.match(TokenType.ARREDA):
                self.advance()
                self.expect(TokenType.SEMICOLON)
                self.output.append(indent_str + 'break;')

            elif self.match(TokenType.DEVOLVE):
                self.advance()
                expr = ''
                if not self.match(TokenType.SEMICOLON):
                    expr = ' ' + self.translate_expression()
                self.expect(TokenType.SEMICOLON)
                self.output.append(indent_str + f'return{expr};')

            # Chamada de função ou expressão
            else:
                expr = self.translate_expression()
                self.expect(TokenType.SEMICOLON)
                self.output.append(indent_str + expr + ';')

    def translate_variable_declaration(self) -> str:
        # Modificadores
        is_const = False
        if self.match(TokenType.NUM_MEXE):
            is_const = True
            self.advance()

        # Ignora um/uma
        if self.match(TokenType.UM, TokenType.UMA):
            self.advance()

        # Tipo
        type_info = self.translate_type()

        # Se for array, type_info é uma tupla
        is_array = isinstance(type_info, tuple)
        if is_array:
            base_type, dimensions = type_info
        else:
            base_type = type_info

        # Ignora 'de' opcional
        if self.match(TokenType.DE):
            self.advance()

        # Nome da variável
        var_name = self.expect(TokenType.IDENTIFIER).value

        # Ponteiro (acolá)
        is_pointer = False
        if self.match(TokenType.ACOLA):
            is_pointer = True
            self.advance()

        # Monta a declaração
        decl = ''
        if is_const:
            decl += 'const '
        decl += base_type + ' '

        if is_pointer:
            decl += '*'

        decl += var_name

        # Dimensões do array
        if is_array:
            for dim in dimensions:
                decl += f'[{dim}]'

        # Inicialização
        if self.match(TokenType.ASSIGN):
            self.advance()
            init_value = self.translate_expression()
            decl += f' = {init_value}'

        self.expect(TokenType.SEMICOLON)
        return decl + ';'

    def translate_if_statement(self, indent: int):
        indent_str = '    ' * indent

        self.expect(TokenType.SE_DER)
        self.expect(TokenType.LPAREN)
        condition = self.translate_expression()
        self.expect(TokenType.RPAREN)

        self.output.append(indent_str + f'if ({condition}) {{')

        self.expect(TokenType.LBRACE)
        self.translate_block(indent + 1)
        self.expect(TokenType.RBRACE)

        # Else
        if self.match(TokenType.SE_NUM_DER):
            self.advance()

            # Else if
            if self.match(TokenType.SE_DER):
                self.output.append(indent_str + '} else if (')
                # Volta um token para processar o if completo
                self.pos -= 1
                self.translate_if_statement(indent)
                return
            else:
                self.output.append(indent_str + '} else {')
                self.expect(TokenType.LBRACE)
                self.translate_block(indent + 1)
                self.expect(TokenType.RBRACE)

        self.output.append(indent_str + '}')

    def translate_switch_statement(self, indent: int):
        indent_str = '    ' * indent

        self.expect(TokenType.ESCOLHE_AI)
        self.expect(TokenType.LPAREN)
        expr = self.translate_expression()
        self.expect(TokenType.RPAREN)

        self.output.append(indent_str + f'switch ({expr}) {{')

        self.expect(TokenType.LBRACE)

        while not self.match(TokenType.RBRACE):
            if self.match(TokenType.CAUSO):
                self.advance()
                case_value = self.translate_expression()
                self.expect(TokenType.COLON)
                self.output.append(indent_str + f'    case {case_value}:')

                # Processa statements até encontrar break ou próximo case
                while not self.match(TokenType.CAUSO, TokenType.SE_NUM_TIVER, TokenType.RBRACE):
                    if self.match(TokenType.UM, TokenType.UMA, TokenType.NUM_MEXE):
                        line = self.translate_variable_declaration()
                        self.output.append(indent_str + '        ' + line)
                    elif self.match(TokenType.ARREDA):
                        self.advance()
                        self.expect(TokenType.SEMICOLON)
                        self.output.append(indent_str + '        break;')
                    elif self.match(TokenType.LBRACE):
                        self.advance()
                        self.translate_block(indent + 2)
                        self.expect(TokenType.RBRACE)
                    else:
                        expr_stmt = self.translate_expression()
                        self.expect(TokenType.SEMICOLON)
                        self.output.append(indent_str + '        ' + expr_stmt + ';')

            elif self.match(TokenType.SE_NUM_TIVER):
                self.advance()
                self.expect(TokenType.COLON)
                self.output.append(indent_str + '    default:')

                while not self.match(TokenType.RBRACE):
                    if self.match(TokenType.UM, TokenType.UMA, TokenType.NUM_MEXE):
                        line = self.translate_variable_declaration()
                        self.output.append(indent_str + '        ' + line)
                    elif self.match(TokenType.ARREDA):
                        self.advance()
                        self.expect(TokenType.SEMICOLON)
                        self.output.append(indent_str + '        break;')
                    elif self.match(TokenType.LBRACE):
                        self.advance()
                        self.translate_block(indent + 2)
                        self.expect(TokenType.RBRACE)
                    else:
                        expr_stmt = self.translate_expression()
                        self.expect(TokenType.SEMICOLON)
                        self.output.append(indent_str + '        ' + expr_stmt + ';')

        self.expect(TokenType.RBRACE)
        self.output.append(indent_str + '}')

    def translate_while_statement(self, indent: int):
        indent_str = '    ' * indent

        self.expect(TokenType.ARRUDEIA)
        self.expect(TokenType.LPAREN)
        condition = self.translate_expression()
        self.expect(TokenType.RPAREN)

        self.output.append(indent_str + f'while ({condition}) {{')

        self.expect(TokenType.LBRACE)
        self.translate_block(indent + 1)
        self.expect(TokenType.RBRACE)

        self.output.append(indent_str + '}')

    def translate_do_while_statement(self, indent: int):
        indent_str = '    ' * indent

        self.expect(TokenType.FAZ_AI)

        self.output.append(indent_str + 'do {')

        self.expect(TokenType.LBRACE)
        self.translate_block(indent + 1)
        self.expect(TokenType.RBRACE)

        self.expect(TokenType.ARRUDEIA)
        self.expect(TokenType.LPAREN)
        condition = self.translate_expression()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.SEMICOLON)

        self.output.append(indent_str + f'}} while ({condition});')

    def translate_for_statement(self, indent: int):
        indent_str = '    ' * indent

        self.expect(TokenType.PRA)
        self.expect(TokenType.LPAREN)

        # Inicialização
        init = ''
        if self.match(TokenType.UM, TokenType.UMA):
            self.advance()
            type_str = self.translate_type()
            if self.match(TokenType.DE):
                self.advance()
            var_name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.ASSIGN)
            init_value = self.translate_expression()
            init = f'{type_str} {var_name} = {init_value}'
        else:
            init = self.translate_expression()

        self.expect(TokenType.SEMICOLON)

        # Condição
        condition = self.translate_expression()
        self.expect(TokenType.SEMICOLON)

        # Incremento
        increment = self.translate_expression()

        self.expect(TokenType.RPAREN)

        self.output.append(indent_str + f'for ({init}; {condition}; {increment}) {{')

        self.expect(TokenType.LBRACE)
        self.translate_block(indent + 1)
        self.expect(TokenType.RBRACE)

        self.output.append(indent_str + '}')

    def is_foreach(self) -> bool:
        # Verifica se é pra_cada olhando alguns tokens à frente
        saved_pos = self.pos

        if not self.match(TokenType.PRA):
            return False

        # Avança para verificar
        self.advance()

        # pra_cada tem UM/UMA depois do PRA
        if self.match(TokenType.UM, TokenType.UMA):
            self.advance()
            # Verifica se tem tipo
            if self.match(*self.TYPE_MAP.keys()):
                self.advance()
                # Verifica se tem DE
                if self.match(TokenType.DE):
                    self.advance()
                # Verifica se tem identificador
                if self.match(TokenType.IDENTIFIER):
                    self.advance()
                    # Verifica se tem EM
                    if self.match(TokenType.EM):
                        self.pos = saved_pos
                        return True

        self.pos = saved_pos
        return False

    def translate_foreach_statement(self, indent: int):
        indent_str = '    ' * indent

        self.expect(TokenType.PRA_CADA)
        self.expect(TokenType.LPAREN)

        # um/uma
        if self.match(TokenType.UM, TokenType.UMA):
            self.advance()

        # Tipo
        item_type = self.translate_type()

        # de (opcional)
        if self.match(TokenType.DE):
            self.advance()

        # Nome da variável
        item_name = self.expect(TokenType.IDENTIFIER).value

        # em
        self.expect(TokenType.EM)

        # Nome do array
        array_name = self.expect(TokenType.IDENTIFIER).value

        self.expect(TokenType.RPAREN)

        # Traduz para for com sizeof
        self.output.append(indent_str + f'for (size_t _i = 0; _i < sizeof({array_name})/sizeof({array_name}[0]); _i++) {{')
        self.output.append(indent_str + f'    {item_type} {item_name} = {array_name}[_i];')

        self.expect(TokenType.LBRACE)
        self.translate_block(indent + 1)
        self.expect(TokenType.RBRACE)

        self.output.append(indent_str + '}')

    def translate_expression(self) -> str:
        return self.translate_assignment()

    def translate_assignment(self) -> str:
        left = self.translate_logical_or()

        if self.match(TokenType.ASSIGN):
            self.advance()
            right = self.translate_assignment()
            return f'{left} = {right}'

        return left

    def translate_logical_or(self) -> str:
        left = self.translate_logical_and()

        while self.match(TokenType.MOI):
            self.advance()
            right = self.translate_logical_and()
            left = f'({left} || {right})'

        return left

    def translate_logical_and(self) -> str:
        left = self.translate_logical_implication()

        while self.match(TokenType.EMENDA):
            self.advance()
            right = self.translate_logical_implication()
            left = f'({left} && {right})'

        return left

    def translate_logical_implication(self) -> str:
        left = self.translate_equality()

        # Implicação: A implica B = !A || B
        if self.match(TokenType.IMPLICA):
            self.advance()
            right = self.translate_equality()
            left = f'(!({left}) || ({right}))'

        # Bi-implicação: A fresca B = (A && B) || (!A && !B)
        elif self.match(TokenType.FRESCA):
            self.advance()
            right = self.translate_equality()
            left = f'(({left} && {right}) || (!({left}) && !({right})))'

        return left

    def translate_equality(self) -> str:
        left = self.translate_relational()

        while self.match(TokenType.EQ, TokenType.NEQ):
            op = self.advance().value
            right = self.translate_relational()
            left = f'({left} {op} {right})'

        return left

    def translate_relational(self) -> str:
        left = self.translate_additive()

        while self.match(TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op = self.advance().value
            right = self.translate_additive()
            left = f'({left} {op} {right})'

        return left

    def translate_additive(self) -> str:
        left = self.translate_multiplicative()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            right = self.translate_multiplicative()
            left = f'({left} {op} {right})'

        return left

    def translate_multiplicative(self) -> str:
        left = self.translate_unary()

        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.advance().value
            right = self.translate_unary()
            left = f'({left} {op} {right})'

        return left

    def translate_unary(self) -> str:
        # Negação lógica
        if self.match(TokenType.AI_DENTRO):
            self.advance()
            expr = self.translate_unary()
            return f'!({expr})'

        # Negativo
        if self.match(TokenType.MINUS):
            self.advance()
            expr = self.translate_unary()
            return f'-({expr})'

        return self.translate_postfix()

    def translate_postfix(self) -> str:
        expr = self.translate_primary()

        while True:
            # Acesso a array
            if self.match(TokenType.LBRACKET):
                self.advance()
                index = self.translate_expression()
                self.expect(TokenType.RBRACKET)
                expr = f'{expr}[{index}]'

            # Chamada de função
            elif self.match(TokenType.LPAREN):
                self.advance()
                args = []

                if not self.match(TokenType.RPAREN):
                    while True:
                        args.append(self.translate_expression())
                        if not self.match(TokenType.COMMA):
                            break
                        self.advance()

                self.expect(TokenType.RPAREN)

                # Traduz berra e escuta
                if expr == 'berra':
                    expr = 'printf'
                elif expr == 'escuta':
                    expr = 'scanf'

                expr = f'{expr}({", ".join(args)})'

            else:
                break

        # Operador acolá (endereço/ponteiro)
        if self.match(TokenType.ACOLA):
            self.advance()
            expr = f'&{expr}'

        return expr

    def translate_primary(self) -> str:
        # Número
        if self.match(TokenType.NUMBER):
            return self.advance().value

        # String
        if self.match(TokenType.STRING):
            return f'"{self.advance().value}"'

        # Caractere
        if self.match(TokenType.CHAR):
            return f"'{self.advance().value}'"

        # Booleanos
        if self.match(TokenType.VALENDO):
            self.advance()
            return 'true'

        if self.match(TokenType.NEM):
            self.advance()
            return 'false'

        # Identificador ou funções nativas tokenizadas como palavras-chave
        if self.match(TokenType.IDENTIFIER, TokenType.BERRA, TokenType.ESCUTA):
            return self.advance().value

        # Expressão entre parênteses
        if self.match(TokenType.LPAREN):
            self.advance()
            expr = self.translate_expression()
            self.expect(TokenType.RPAREN)
            return f'({expr})'

        # Inicializador de array
        if self.match(TokenType.LBRACE):
            self.advance()
            elements = []

            if not self.match(TokenType.RBRACE):
                while True:
                    elements.append(self.translate_expression())
                    if not self.match(TokenType.COMMA):
                        break
                    self.advance()

            self.expect(TokenType.RBRACE)
            return '{' + ', '.join(elements) + '}'

        self.error(f"Expressão esperada, encontrado {self.current().type}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python budega_translator.py <arquivo.budega> [arquivo_saida.c]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(input_file)[0] + '.c'

    try:
        # Lê o arquivo fonte
        with open(input_file, 'r', encoding='utf-8') as f:
            source = f.read()

        # Lexer
        print(f"Analisando {input_file}...")
        lexer = Lexer(source)
        tokens = lexer.tokenize()

        # Tradutor
        print("Traduzindo para C...")
        translator = Translator(tokens)
        c_code = translator.translate()

        # Escreve o arquivo de saída
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(c_code)

        print(f"✓ Tradução concluída: {output_file}")
        print(f"\nPara compilar:")
        print(f"  gcc {output_file} -o programa")
        print(f"  ./programa")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
        sys.exit(1)
    except SyntaxError as e:
        print(f"Erro de sintaxe: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
