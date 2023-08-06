import imp
import numpy
from collections import OrderedDict
from math import pow

from pyxai.source.core.explainer.explainerInterface import ExplainerInterface, Explainer
from pyxai.source.core.structure.decisionTree import DecisionTree, DecisionNode
from pyxai.source.core.tools.utils import add_lists_by_index
from pyxai.source.core.structure.type import TypeReason, TypeCount, PreferredReasonMethod
from pyxai.source.core.tools.encoding import CNFencoding

from pyxai.source.solvers.MAXSAT.RC2solver import RC2MAXSATsolver
from pyxai.source.solvers.MAXSAT.OPENWBOSolver import OPENWBOSolver
from pyxai.source.solvers.SAT.glucoseSolver import GlucoseSolver
from pyxai.source.solvers.COMPILER.D4Solver import D4Solver
from pyxai.source.core.tools.utils import compute_weight


class ExplainerDT(ExplainerInterface, Explainer):

  def __init__(self, tree, instance=None):
    """Create object dedicated to finding explanations from a decision tree ``tree`` and an instance ``instance``. 

    Args:
        tree (DecisionTree): The model in the form of a DecisionTree object.
        instance (:obj:`list` of :obj:`int`, optional): The instance (an observation) on which explanations must be calculated. Defaults to None.
    """
    self.tree = tree  # The decision tree.
    if instance is not None: self.set_instance(instance)


  def set_instance(self, instance):
    """Change the instance on which explanations must be calculated.  
    Args:
        instance (obj:`list` of :obj:`int`): The instance (an observation) on which explanations must be calculated.
    """
    # The target observation.
    self.instance = instance
    # An implicant of self.tree (a term that implies the tree)
    self.implicant = self.tree.instance_to_binaries(instance)
    # The target prediction (0 or 1)
    self.target_prediction = self.tree.take_decisions_instance(instance)


  def to_features(self, implicant):
    """_summary_

    Args:
        implicant (_type_): _description_

    Returns:
        _type_: _description_
    """

    return self.tree.to_features(implicant)


  def direct_reason(self):
    """Coucou

    Returns:
        _type_: _description_
    """
    return Explainer.format(self.tree.direct_reason(self.instance))


  def contrastive_reason(self, *, n=1):
    cnf = self.tree.to_CNF(self.instance)
    core = CNFencoding.extract_core(cnf, self.implicant)
    contrastives = sorted(core, key=lambda clause: len(clause))
    
    print(contrastives)

    return Explainer.format(contrastives, n) if type(n) != int else Explainer.format(contrastives[:n], n)


  def necessary_literals(self):
    cnf = self.tree.to_CNF(self.instance, target_prediction=self.target_prediction)
    core = CNFencoding.extract_core(cnf, self.implicant)
    return sorted({l for _, clause in enumerate(core) if len(clause) == 1 for l in clause})


  def relevant_literals(self):
    cnf = self.tree.to_CNF(self.instance, target_prediction=self.target_prediction)
    core = CNFencoding.extract_core(cnf, self.implicant)
    return [l for _, clause in enumerate(core) if len(clause) > 1 for l in clause]


  def sufficient_reason(self, *, n=1, time_limit=0):
    time_used = 0
    n = n if type(n) == int else float('inf')
    cnf = self.tree.to_CNF(self.instance, target_prediction=self.target_prediction)
    prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)
    SATsolver = GlucoseSolver()
    SATsolver.add_clauses(prime_implicant_cnf.cnf)

    sufficient_reasons = []
    while True:
      if (time_limit != 0 and time_used > time_limit) or len(sufficient_reasons) == n:
        break
      result, time = SATsolver.solve(time_limit - time_used)
      time_used += time
      if result is None: break
      sufficient_reasons.append(prime_implicant_cnf.get_reason_from_model(result))
      SATsolver.add_clauses([prime_implicant_cnf.get_blocking_clause(result)])
    return Explainer.format(sufficient_reasons, n)


  def preferred_reason(self, *, method, n=1, time_limit=0, weights=None):
    n = n if type(n) == int else float('inf')
    cnf = self.tree.to_CNF(self.instance)

    prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)
    cnf = prime_implicant_cnf.cnf
    if len(cnf) == 0:  # TODO: test when this case append
      return [l for l in prime_implicant_cnf.necessary]

    weights = compute_weight(method, self.instance, weights, self.tree.ML_solver_information)
    weights_per_feature = {i + 1: weight for i, weight in enumerate(weights)}

    soft = [l for l in prime_implicant_cnf.mapping_original_to_new if l != 0]

    weights_soft = []
    for l in soft:  # soft clause 
      for i in range(len(self.instance)):
        if self.tree.to_features([l], eliminate_redundant_features=False)[0][0] == i + 1:
          weights_soft.append(weights[i])

    solver = OPENWBOSolver()

    # Hard clauses
    for c in cnf:
      solver.add_hard_clause(c)

    # Soft clauses
    for i in range(len(soft)):
      solver.add_soft_clause([-soft[i]], weights_soft[i])

    # Solving
    time_used = 0
    best_score = -1
    reasons = []
    first_call = True

    while True:
      status, model, time = solver.solve(time_limit - time_used)
      time_used += time
      if (time_limit != 0 and time_used > time_limit) or len(reasons) == n:
        break
      if model is None:
        return Explainer.format(reasons, n)

      preferred = prime_implicant_cnf.get_reason_from_model(model)
      solver.add_hard_clause(prime_implicant_cnf.get_blocking_clause(model))
      # Compute the score
      score = sum([weights_per_feature[id_feature] for (id_feature, _, _, _) in
                   self.tree.to_features(preferred, eliminate_redundant_features=False)])
      if first_call:
        best_score = score
      elif score != best_score:
        return Explainer.format(reasons, n)
      first_call = False

      if status == "OPTIMUM":
        reasons.append(preferred)
      else:
        assert False, "The status do not return the optimum !"
    return Explainer.format(reasons, n)


  def minimal_sufficient_reason(self, *, n=1, time_limit=0):
    return self.preferred_reason(method=PreferredReasonMethod.Minimal, n=n, time_limit=time_limit)


  def n_sufficient_reasons_per_attribute(self, *, time_limit=0):
    cnf = self.tree.to_CNF(self.instance)
    prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)
    if len(prime_implicant_cnf.cnf) == 0:  # Special case where all in necessary
      return {l: 1 for l in prime_implicant_cnf.necessary}

    compiler = D4Solver()
    compiler.add_cnf(prime_implicant_cnf.cnf, prime_implicant_cnf.n_literals - 1)
    compiler.add_count_model_query(prime_implicant_cnf.cnf, prime_implicant_cnf.n_literals - 1,
                                   prime_implicant_cnf.n_literals_mapping)
    n_models = compiler.solve(time_limit)
    n_necessary = n_models[0] if len(n_models) > 0 else 1

    n_sufficients_per_attribute = {n: n_necessary for n in prime_implicant_cnf.necessary}
    for l in range(1, prime_implicant_cnf.n_literals_mapping):
      n_sufficients_per_attribute[prime_implicant_cnf.mapping_new_to_original[l]] = n_models[l]
    return n_sufficients_per_attribute


  def is_implicant(self, reason):
    return self.tree.is_implicant(reason, self.target_prediction)


  def is_sufficient(self, reason):
    if self.is_implicant(reason) is False:
      return False
    for lit in reason:
      copy_reason = list(reason).copy()
      copy_reason.remove(lit)
      if self.is_implicant(tuple(copy_reason)) is True:
        return False
    return True


  def is_contrastive(self, reason):
    copy_implicant = list(self.implicant).copy()
    for lit in reason:
      copy_implicant[copy_implicant.index(lit)] = -lit

    if self.tree.is_implicant(copy_implicant, self.target_prediction):
      return False
    return True


  def rectify(self, tree, positive_rectifying_tree, negative_rectifying_tree):
    not_positive_rectifying_tree = positive_rectifying_tree.negating_tree()
    not_negative_rectifying_tree = negative_rectifying_tree.negating_tree()

    tree_1 = positive_rectifying_tree.concatenate_tree(not_negative_rectifying_tree)
    tree_2 = negative_rectifying_tree.concatenate_tree(not_positive_rectifying_tree)

    not_tree_2 = tree_2.negating_tree()

    tree_and_not_tree_2 = tree.concatenate_tree(not_tree_2)
    tree_and_not_tree_2.simplify()

    tree_and_not_tree_2_or_tree_1 = tree_and_not_tree_2.disjoint_tree(tree_1)
    tree_and_not_tree_2_or_tree_1.simplify()
    return tree_and_not_tree_2_or_tree_1


  def contrastive_reason_maxsat(self, *, n=100):
    n = n if type(n) == int else float('inf')
    tree_cnf = self.tree.to_CNF(self.instance, target_prediction=1 if self.target_prediction == 0 else 0)
    MAXSATsolver = RC2MAXSATsolver()
    for l in self.implicant:
      MAXSATsolver.add_soft_clause([-l], weight=1)
    for clause in tree_cnf:
      MAXSATsolver.add_clause(clause)

    results = []
    while len(results) < n:
      reason = MAXSATsolver.solve()
      if reason is None:
        results = CNFencoding.remove_subsumed(results)
        return Explainer.format(results, n)

      # We have to invert the reason :)
      true_reason = [-l for l in reason if -l in self.implicant]
      MAXSATsolver.add_clause([-l for l in reason])
      results.append(true_reason)
    results = CNFencoding.remove_subsumed(results)
    return Explainer.format(results, n)

# def old_preferred_reason(self, n=1, weights=None):
#     # TODO: preferred_reason avec des poids a 1 pour les minimals.

#     n = n if type(n) == int else float('inf')
#     cnf = self.tree.to_CNF(self.instance)
#     prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)

#     if len(prime_implicant_cnf.cnf) == 0 : # TODO: test when this case append
#       return [l for l in prime_implicant_cnf.necessary]

#     print("weights:", weights)
#     soft = [l for l in prime_implicant_cnf.mapping_original_to_new if l != 0]
#     weights_soft = [weights[l] if l in weights else 1 for l in soft]

#     weights_per_feature = {id_features:weight for (id_features, _, _, weight) in self.to_features(weights)}
#     print("weights_per_feature:", weights_per_feature)

#     MAXSATsolver = RC2MAXSATsolver()
#     MAXSATsolver.add_hard_clauses(prime_implicant_cnf.cnf)
#     for i, l in enumerate(soft):
#       MAXSATsolver.add_soft_clause([l], weights_soft[i])

#     results = []
#     best_weight = -1
#     while len(results) < n:
#       result = MAXSATsolver.solve_implicant(self.implicant)
#       if result is None: return CNFencoding.format(results)
#       preferred = prime_implicant_cnf.get_reason_from_model(result)
#       active_weight_feature = sum([weights_per_feature[id_feature] for (id_feature,_,_,_) in self.to_features(preferred)])

#       if len(results) == 0: #first step
#         best_weight = active_weight_feature
#       elif active_weight_feature != best_weight: #other steps
#         return CNFencoding.format(results)

#       MAXSATsolver.add_clause(prime_implicant_cnf.get_blocking_clause(result))
#       results.append(preferred)

#     return Explainer.format(results)


# def check_sufficient(self, reason, n_samples=1000):
#   delta = 1
#   scores = self.compute_scores(reason, self.target_prediction, self.tree.root)
#   print(scores)
#   return scores[1] * 100 >= int(delta * 100) * (scores[0] + scores[1])

# def compute_scores_leaf(self, target_prediction, value, times, exponent):
#   scores=[0,0]
#   if target_prediction == value:
#     scores[1] += times * pow(2, exponent)
#   else:
#     scores[0] += times * pow(2, exponent)
#   return scores

# def compute_scores(self, implicant, target_prediction, node, fixed_variables=[]):

#   id_variable = self.tree.get_id_variable(node)
#   exponent = len(self.tree.map_id_binaries_to_features) - len(implicant) - len(fixed_variables)

#   if id_variable in implicant:
#     if not isinstance(node.right, DecisionNode):
#       return self.compute_scores_leaf(target_prediction, node.right.value, 1, exponent)
#     return self.compute_scores(implicant, target_prediction, node.right, fixed_variables.copy())
#   elif -id_variable in implicant:
#     if not isinstance(node.left, DecisionNode):
#       return self.compute_scores_leaf(target_prediction, node.left.value, 1, exponent)
#     return self.compute_scores(implicant, target_prediction, node.left, fixed_variables.copy())
#   else: # the variable is not in the implicant
#     scores = [0, 0]
#     if id_variable not in fixed_variables:
#       fixed_variables.append(id_variable)
#       exponent -= 1

#     scores_to_add = self.compute_scores_leaf(target_prediction, node.right.value, 2, exponent) \
#       if not isinstance(node.right, DecisionNode) \
#       else self.compute_scores(implicant, target_prediction, node.right, fixed_variables.copy())
#     scores = add_lists_by_index(scores, scores_to_add)

#     scores_to_add = self.compute_scores_leaf(target_prediction, node.left.value, 2, exponent) \
#       if not isinstance(node.left, DecisionNode) \
#       else self.compute_scores(implicant, target_prediction, node.left, fixed_variables.copy())
#     return add_lists_by_index(scores, scores_to_add)

# def sufficient_reason_python(self):
# """
# Ad hoc method (not usefull now)
# """
# i = 0
# sufficient = self.implicant.copy()
# while i < len(sufficient):
#   candidate = sufficient.copy()
#   candidate.pop(i)
#   if self.is_sufficient_reason(implicant=candidate, target_prediction=self.target_prediction):
#     sufficient = candidate
#   else:
#     i+=1
# return Explainer.format(sufficient)
