filename = "./ASTGeneration.py"
fo = open(filename, "w")
fo.write("""# Generate automatically
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
""")

with open("./target/BKITParser.py") as fp: 
    Lines = fp.readlines()
    classBkit = False
    for line in Lines:
        index = line.find("class")
        if index != -1 and classBkit == True:
            comment = ""
            with open("./src/main/bkit/parser/BKIT.g4") as bkit:
                bkitlines = bkit.readlines()
                for cmt in bkitlines:
                    i = cmt.find(line[index + 6:-28].lower())
                    if i != -1 and cmt[0] != '/':
                        comment = cmt

            fo.write("""    # """ + comment + """    def visit""" + line[index + 6:-28] + """(self,ctx:BKITParser.""" + line[index + 6:-21] + """):
        return None

""")
        elif index != -1 and classBkit == False:
            classBkit = True

fo.close()