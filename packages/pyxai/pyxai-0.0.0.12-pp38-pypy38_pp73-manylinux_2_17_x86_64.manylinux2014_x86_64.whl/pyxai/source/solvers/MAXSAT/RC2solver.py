
from pysat.formula import WCNF
from pysat.examples.rc2 import RC2

from pysat.pb import *
#from pysat.pb import PBEnc

class RC2MAXSATsolver():

  def __init__(self):
    self.WCNF = WCNF()
    
  def add_soft_clause(self, clause, weight):
    self.WCNF.append(clause, weight=weight)

  def add_soft_clauses_implicant(self, implicant):
    for lit in implicant:
      self.WCNF.append([-lit], weight=1)

  def add_hard_clause(self, clause):
    self.WCNF.append(clause)

  def add_hard_clauses(self, tree_CNF, implicant=None):    
    for clause in tree_CNF:  # hard
      if implicant is not None:
        new_clause = [lit for lit in clause if lit in implicant]
        assert new_clause != [], "This clause cannot be empty"
        self.WCNF.append(new_clause)
      else:
        self.WCNF.append(clause)

  def add_atmost(self, implicant, sufficient_reason):
    self.WCNF.extend(
      PBEnc.atmost(lits=implicant, top_id=self.WCNF.nv + 1, bound=len(sufficient_reason)).clauses)
  
  def add_clause(self, clause):
    self.WCNF.append(clause)

  def solve_implicant(self, implicant):
    result = RC2(self.WCNF).compute()
    if result is None: return None
    return [lit for lit in result if lit in implicant]
            
  def solve(self):
    result = RC2(self.WCNF).compute()
    if result is None: return None
    return [lit for lit in result]