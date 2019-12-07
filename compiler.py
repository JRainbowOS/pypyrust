"""
The top-level compiler module for PyPyRust. It takes a Python source
file and generates a Rust source file, representing the Python.
"""

import ast
import sys
from rust_generator import RustGenerator

def compile_to_rust(source, filename: str) -> bool:
    """
    Compiles a Python source file, generating Rust source in
    stdout that does the same thing. Warnings and compiler errors are
    sent to stderr. Returns a bool which is True if the compilation
    was successful (no errors, though there may have been warnings).

    source is typically a string, but other types are supported
    (see ast.parse).
    
    filename_in is only used for prettifying the error output.
    """

    # compile the python source into an AST
    tree = ast.parse(source, filename, 'exec')

    # Walk the tree, outputting Rust code as we go (rather like XSLT)
    RustGenerator().visit(tree)

    return True

def compile_file_to_rust(filename: str) -> bool:
    """
    Compiles a Python source file, generating Rust source in
    stdout that does the same thing. Warnings and compiler errors are
    sent to stderr. Returns a bool which is True if the compilation
    was successful (no errors, though there may have been warnings).

    filename is the file containing the Python source.
    """
    file = open(filename, 'r')
    source = file.read()
    file.close()
    ok = compile_to_rust(source, filename)
    assert(ok)

if __name__ == "__main__":
    python_file = r"C:\Users\JRainbow\Documents\Python Scripts\pypyrust\fib.py"
    # python_file = r"C:\Users\JRainbow\Documents\Python Scripts\TwitterScraper\twitter_client.py"
    compile_file_to_rust(python_file)
    print('Done')
