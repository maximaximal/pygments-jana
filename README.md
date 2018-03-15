# pygments-jana

This project aims to implement a pygments plugin to highlight
the algorithm design language [Jana](https://de.wikipedia.org/wiki/Jana_(Informatik)). It is
a forked version of the original Java lexer from the pygments project.

## Example

![Example of the highlighting engine](example.png)

## Installing 

First, clone the repository using:

    git clone git@github.com:maximaximal/pygments-jana.git
	cd pygments-jana

After that, choose an installation method:

### End-User Mode

Using this method, the software can be used directly.

    sudo python setup.py develop

### Developer Mode

This mode enables code changes directly in the repository, which propagate 
to the lexer called by `pygmentize`. It is therefore more suited for 
development.

    sudo python setup.py develop

## Usage in LaTeX

This highlighter can easily be used in LaTeX with the
great `minted`-Package 
([Documentation](https://www.ctan.org/tex-archive/macros/latex/contrib/minted/), 
[Tutorial](https://de.sharelatex.com/learn/Code_Highlighting_with_minted)). This is also
the main use-case for this small project, which emerged from the wish to have nice syntax
highlighting in student exercises.

After installation, the highlighter should directly be usable in `minted`. It is configured
to work for the keywords `Jana`, `jana`, and on `*.jana` files.

## Ressources for writing pygments plugins

  * https://stackoverflow.com/questions/22321702/how-to-install-a-new-lexer-in-pygments
  * http://www.iamjonas.me/2013/03/custom-syntax-in-pygments.html
