
import uuid
import subprocess
import os

MUSER_DIRECTORY = os.sep.join(__file__.split(os.sep)[:-1]) + os.sep
MUSER_EXEC = MUSER_DIRECTORY + "muser_static"


class MUSERSolver():
  def __init__(self, filenames="/tmp/muser", hash=str(uuid.uuid4().fields[-1])[:8]):
    self.hash = hash
    self.filename_gcnf = "/tmp/muser-"+self.hash+".gcnf"
    
    
  def write_gcnf(self, n_variables, hard_clauses, soft_clauses):

    file = open(self.filename_gcnf, "w")    
    file.write(f"p gcnf {n_variables} {len(hard_clauses) + len(soft_clauses)} {len(soft_clauses) + 1}\n")

    for clause in hard_clauses: 
      file.write("{1} " + " ".join(str(l) for l in clause) + " 0\n")
    for i, clause in enumerate(soft_clauses): 
      file.write("{" + str(i+2) + "} " + " ".join(str(l) for l in clause) + " 0\n")
    
    file.close()


  def solve(self, implicant):
    reason_str = subprocess.getoutput(f'{MUSER_EXEC} -comp  -grp {self.filename_gcnf}')
    reason_str = [line for line in reason_str.split('\n') if line.startswith("v")][0]
    reason = [implicant[int(element) - 2] for element in reason_str.split(' ')[2:-1]]
    return reason