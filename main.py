'''

Copy absolute path of a selected file

'''

import sys
import clipboard

file = sys.argv[1]
clipboard.copy(file)
