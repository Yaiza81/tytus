from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

class AlterDataBase(instruction.Instruction):
    def __init__(self, option, name, newname, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.option = option  # define si se renombra o se cambia de dueño
        self.name = name  # define el nombre nuevo de la base de datos o el nuevo dueño
        self.newname = newname

    def execute(self, environment):
        out = "fase1.execution("
        out += '"'
        out += "ALTER DATABASE "
        out += self.name + " "
        out += self.option + " TO "
        out += self.newname + ";"
        out += '")\n'
        return code.C3D(out, "alter_db", self.row, self.column)
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_ALTER_DATABASEs")
        
