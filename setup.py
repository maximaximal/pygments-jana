from setuptools import setup, find_packages

setup (
    name='janalexer',
    packages=find_packages(),
    entry_points =
    """
    [pygments.lexers]
    janalexer = janalexer.lexer:JanaLexer
    """,
)
