import sys

# disable creation of *.pyc files
sys.dont_write_bytecode = True


class For:
    """
        For loop has the following structure:
        >>> for(int i=0; i<n; i++){
                // loop body instructions
            }
        >>> for(int i=0; i<n; i++)
                // inline loop instructions
    """

