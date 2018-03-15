import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
    this, combined, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic
from pygments.util import shebang_matches
from pygments import unistring as uni

class JanaLexer(RegexLexer):
    """
    A lexer for the Jana language: https://de.wikipedia.org/wiki/Jana_(Informatik)
    """

    name = 'Jana'
    aliases = ['jana']
    filenames = ['*.jana']
    mimetypes = ['text/x-jana']

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = {
        'root': [
            (r'(?<![(),][ ])([A-Z]|\u2026|\.\.\.)[a-zA-Z0-9.;:,\!\? ]*\n', String.Doc),
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            # keywords: go before method names to avoid lexing "throw new XYZ"
            # as a method signature
            (r'(assert|break|case|catch|continue|default|do|else|finally|for|'
             r'if|goto|instanceof|new|return|switch|this|throw|try|while)\b',
             Keyword),
            # method names
            (r'((?:(?:[^\W\d]|\$)[\w.\[\]$<>]*\s+)+?)*'  # return arguments
             r'((?:[^\W\d]|\$)[\w$]*)'                   # method name
             r'(\s*)(\()',                               # signature start
             bygroups(using(this), Name.Function, Text, Operator)),
            (r'@[^\W\d][\w.]*', Name.Decorator),
            (r'(abstract|const|enum|extends|final|implements|native|private|'
             r'protected|public|static|strictfp|super|synchronized|throws|'
             r'transient|volatile)\b', Keyword.Declaration),
            (r'(boolean|byte|char|double|float|int|long|short|void)\b',
             Keyword.Type),
            (r'(\u2191|\u2193|\u2195)', Name.Decorator), # Arrows for parameters
            (r'(package)(\s+)', bygroups(Keyword.Namespace, Text), 'import'),
            (r'(true|false|null)\b', Keyword.Constant),
            (r'(class|interface|type)(\s+)', bygroups(Keyword.Declaration, Text),
             'class'),
            (r'(import(?:\s+static)?)(\s+)', bygroups(Keyword.Namespace, Text),
             'import'),
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'\\.'|'[^\\]'|'\\u[0-9a-fA-F]{4}'", String.Char),
            (r'(\.)((?:[^\W\d]|\$)[\w$]*)', bygroups(Operator, Name.Attribute)),
            (r'^\s*([^\W\d]|\$)[\w$]*:', Name.Label),
            (r'([^\W\d]|\$)[\w$]*', Name),
            (r'([A-Z]*[^\W\d]|\$)[\w$]*\n', Text),
            (r'([0-9][0-9_]*\.([0-9][0-9_]*)?|'
             r'\.[0-9][0-9_]*)'
             r'([eE][+\-]?[0-9][0-9_]*)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9_]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9_]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F_]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F_]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            (r'0[bB][01][01_]*[lL]?', Number.Bin),
            (r'0[0-7_]+[lL]?', Number.Oct),
            (r'0|[1-9][0-9_]*[lL]?', Number.Integer),
            (r'([~^*!%&\[\](){}<>|+=;/?-]|\u007e|\u00d7|\u2205|\u2208|\u2209|\u220b|\u221e|\.\.)', Operator),
            (r'[~^*:.,]', Punctuation),
            (r'\s+', Text),
        ],
        'class': [
            (r'([^\W\d]|\$)[\w$]*', Name.Class, '#pop')
        ],
        'import': [
            (r'[\w.]+\*?', Name.Namespace, '#pop')
        ],
    }
