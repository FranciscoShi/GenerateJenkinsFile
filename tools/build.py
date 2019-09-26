from config import *


mavenbuild = """
def mvnHome = tool 'M3'
sh " ${mvnHome}/bin/${buildShell} "
"""

