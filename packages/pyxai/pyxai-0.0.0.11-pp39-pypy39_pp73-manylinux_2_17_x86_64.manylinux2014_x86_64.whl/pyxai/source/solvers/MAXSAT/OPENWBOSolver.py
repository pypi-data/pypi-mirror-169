
from pysat.formula import WCNF

import time
import subprocess
import os
import uuid

OPENWBO_DIRECTORY = os.sep.join(__file__.split(os.sep)[:-1]) + os.sep
OPENWBO_EXEC = OPENWBO_DIRECTORY + "openwbo_static"

class OPENWBOSolver():

  def __init__(self, hash=str(uuid.uuid4().fields[-1])[:8]):
    self.WCNF = WCNF()
    self.hash = hash
    self.filename_wcnf = "/tmp/wbo-"+self.hash+".wcnf"
    
  def add_soft_clause(self, clause, weight):
    self.WCNF.append(clause, weight=weight)

  def add_hard_clause(self, clause):    
    self.WCNF.append(clause)

  def solve(self, time_limit=0):
    wcnf_file = f"/tmp/wbo-{self.hash}.wcnf"
    self.WCNF.to_file(wcnf_file)          
    time_used = -time.time()
    if time_limit != 0:
      p = subprocess.run([OPENWBO_EXEC,
                          f"-cpu-lim={time_limit}", wcnf_file], 
                          timeout=None,
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, 
                          universal_newlines=True)
    else:
      p = subprocess.run([OPENWBO_EXEC, wcnf_file], 
                        timeout=None,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        universal_newlines=True)
    time_used += time.time()
    output_str = [line.split(" ") for line in p.stdout.split("\n") if len(line) > 0 and line[0] == "v"]
    if len(output_str) == 0:
      return p.stderr, None, time_used 
    
    status = [line.split(" ")[1] for line in p.stdout.split("\n") if len(line) > 0 and line[0] == "s"][0]
    model = [int(l) for l in output_str[0] if l != 'v' and l != '']
    return status, model, time_used