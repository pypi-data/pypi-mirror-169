
from typing import Iterable

class ExplainerInterface:
    
    
    def direct_reason(self):
      """Ici

      Raises:
          NotImplementedError: _description_
      """
      raise NotImplementedError

    def sufficient_reason(self, *, n=1, seed=0):
      raise NotImplementedError
    
    def is_implicant(self, reason):
      raise NotImplementedError

    def is_sufficient(self, reason):
      raise NotImplementedError
      
    def is_contrastive(self, reason):
      raise NotImplementedError
      
    
class Explainer:

  def format(reasons, n=1):
    if len(reasons) == 0:
      return tuple()
    if len(reasons) == 1 and isinstance(reasons[0], Iterable):
      if type(n) != int:
        return tuple(tuple(sorted(reason, key=lambda l: abs(l))) for reason in reasons)
      elif type(n) == int and n != 1:
        return tuple(tuple(sorted(reason, key=lambda l: abs(l))) for reason in reasons)
      else:
        return Explainer.format(reasons[0])
    if not isinstance(reasons[0], Iterable):
      return tuple(sorted(reasons, key=lambda l: abs(l)))
    
    return tuple(tuple(sorted(reason, key=lambda l: abs(l))) for reason in reasons)