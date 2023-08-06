
import c_explainer

from tkinter import N
from unittest import result
from itertools import chain, combinations
import random
import numpy

from pyxai.source.core.explainer.explainerInterface import ExplainerInterface, Explainer
from pyxai.source.core.tools.encoding import CNFencoding
from pyxai.source.solvers.GRAPH.TreeDecomposition import TreeDecomposition
from pyxai.source.core.structure.type import TypeReason, ReasonExpressivity
from pyxai.source.core.tools.utils import flatten

from pyxai.source.solvers.CSP.TSMinimalV2 import TSMinimal
from pyxai.source.solvers.CSP.AbductiveV1 import AbductiveModelV1
from pyxai.source.solvers.CSP.AbductiveV2 import AbductiveModelV2
from pycsp3 import SAT, UNSAT, UNKNOWN, OPTIMUM, protect

class ExplainerBT(ExplainerInterface):

  def __init__(self, boosted_trees, instance=None):
    self.boosted_trees = boosted_trees # The boosted trees.
    self.c_BT = None
    if instance is not None:
      self.set_instance(instance)
  
  def set_instance(self, instance, implicant=None, target_prediction=None):
    self.instance = instance # The target observation.
    self.implicant = implicant # An implicant of self.tree (a term that implies the tree)
    self.target_prediction = target_prediction # The target prediction (0 or 1)
    if self.implicant is None:
      self.implicant = self.boosted_trees.instance_to_binaries(instance)

    if self.target_prediction is None:
      self.target_prediction = self.boosted_trees.predict_instance(instance)
    
    #The id_features of each variable of the implicant
    self.implicant_id_features = self.boosted_trees.get_id_features(self.implicant) 

  def trees_statistics(self):
    #print("---------   Trees Information   ---------")
    n_nodes = sum([len(tree.get_variables()) for tree in self.boosted_trees.forest])
    n_nodes_biggest_tree = max([len(tree.get_variables()) for tree in self.boosted_trees.forest])
    n_nodes_biggest_tree_without_redundancy = max([len(set(tree.get_variables())) for tree in self.boosted_trees.forest])
    

    n_features = len(set(flatten([tree.get_features() for tree in self.boosted_trees.forest])))
    
    n_nodes_without_redundancy = []
    for tree in self.boosted_trees.forest:
      n_nodes_without_redundancy.extend(tree.get_variables())
    n_nodes_without_redundancy = len(list(set(n_nodes_without_redundancy)))



    return {"n_nodes": n_nodes,
            "n_nodes_without_redundancy": n_nodes_without_redundancy,
            "n_nodes_biggest_tree": n_nodes_biggest_tree,
            "n_nodes_biggest_tree_without_redundancy": n_nodes_biggest_tree_without_redundancy,
            "n_features": n_features}
            
  def reason_statistics(self, reason, *, reason_expressivity):
    if reason_expressivity == ReasonExpressivity.Conditions:
      if reason is not None:
        reason_length = len(reason)
        features_in_reason = self.to_features_indexes(reason)
        reduction_features = round(float(100-(len(features_in_reason)*100)/len(self.instance)),2)
        reduction_conditions = round(float(100-(len(reason)*100)/len(self.implicant)),2) 
      else:
        reason_length = len(self.implicant)
        features_in_reason = []
        reduction_features = round(float(0),2)
        reduction_conditions = round(float(0),2)
      return {"instance_length": len(self.instance),
              "implicant_length": len(self.implicant),
              "reason_length": reason_length,
              "features_in_reason_length": len(features_in_reason),
              "features_not_in_reason_length": len(self.instance)-len(features_in_reason),
              "%_reduction_conditions": reduction_conditions,
              "%_reduction_features": reduction_features}
    elif reason_expressivity == ReasonExpressivity.Features:
      if reason is not None:
        reason_length = len(reason)
        reduction_features = round(float(100-(len(reason)*100)/len(self.instance)),2) 
      else:
        reason_length = 0
        reduction_features = round(float(0),2)
      print("here:", reduction_features)
      return {"instance_length": len(self.instance),
              "reason_length": reason_length,
              "features_in_reason_length": reason_length,
              "features_not_in_reason_length": len(self.instance)-reason_length,
              "%_reduction_features": reduction_features}
    else:
      assert True, "TODO"

  def to_features_indexes(self, reason):
    """Return the indexes of the instance that are involved in the reason. 
  
    Args:
        reason (list): The reason.

    Returns:
        list: indexes of the instance that are involved in the reason.
    """
    features = [feature for (feature,_,_,_) in self.to_features(reason)]
    return [i for i, _ in enumerate(self.instance) if i+1 in features]

  def to_features(self, implicant):
    return self.boosted_trees.to_features(implicant)

  def redundancy_analysis(self):
    return self.boosted_trees.redundancy_analysis()

  def compute_propabilities(self):
    return self.boosted_trees.compute_probabilities(self.instance)
 
  def direct_reason(self):
    """The direct reason is the set of conditions used to classified the instance.

    Returns:
        list: The direct reason.
    """
    seen_in_trees = set()
    for tree in self.boosted_trees.forest:
      seen_in_trees |= set(tree.direct_reason(self.instance))
    return Explainer.format(list(seen_in_trees))


  def sufficient_reason(self, *, n=1, seed=0):
    """ Compute a sufficient reason using several CSP thanks to pycsp3 models.
    Works only on binary instances for the moment 

    Returns:
        list: The sufficient reason.
    """
    assert n == 1, "To do implement that"

    cp_solver = AbductiveModelV1()

    abductive = list(self.implicant).copy()
    is_removed = [False for _ in abductive]
    if seed != 0:
      random.seed(seed)
      random.shuffle(abductive)

    for i, lit in enumerate(abductive):
      is_removed[i] = True
      cp_solver.create_model_is_abductive(abductive, is_removed, self.boosted_trees, self.target_prediction)      
      #cp_solver.create_model_is_abductive(abductive, i, is_removed, self.boosted_trees, self.target_prediction)            
      result, solution = cp_solver.solve()
      if result == UNKNOWN:
        print("problem")
        exit(0)
      if result != UNSAT: #We can not remove this literal because else at least one solution do not predict the good class !
        is_removed[i] = False

    abductive = [l for i, l in enumerate(abductive) if is_removed[i] is False]  
      
    return Explainer.format(abductive, n)
  
  def minimal_tree_specific_reason(self, *, time_limit=0, reason_expressivity, from_reason=None):
   cp_solver = TSMinimal()
   implicant_id_features = self.implicant_id_features if reason_expressivity == ReasonExpressivity.Features else []
   cp_solver.create_model_minimal_abductive_BT(
     self.implicant, 
     self.boosted_trees, 
     self.target_prediction,
     self.boosted_trees.n_classes,
     implicant_id_features,
     from_reason)
   result, solution = cp_solver.solve(time_limit=time_limit)
   if result == UNSAT or result == UNKNOWN:
     return result, None
   return result, Explainer.format([l for i, l in enumerate(self.implicant) if solution[i] == 1])

  def tree_specific_reason(self, *, reason_expressivity, n_iterations=50, time_limit=None):
    """
    Tree-specific (TS) explanations are abductive explanations that can be computed in polynomial time. While tree-specific explanations are not subset-minimal in the general case, they turn out to be close to sufficient reasons in practice. Furthermore, because sufficient reasons can be derived from tree-specific explanations, computing tree-specific explanations can be exploited as a preprocessing step in the derivation of sufficient reasons 
    
    The method used (in c++), for a given seed, compute several tree specific reasons and return the best. 
    For that, the algorithm is executed either during a given time or or until a certain number of reasons is calculated.
    
    The parameter 'reason_expressivity' have to be fixed either by ReasonExpressivity.Features or ReasonExpressivity.Conditions. 
  
    Args:
        reason_expressivity (Explainer.FEATURES, Explainer.CONDITIONS): _description_
        n_iterations (int, optional): _description_. Defaults to 50.
        time_limit (int, optional): _description_. Defaults to None.

    Returns:
        list: The tree-specific reason
    """
    if time_limit is None: time_limit = 0
    if self.c_BT == None :
      # Preprocessing to give all trees in the c++ library
      self.c_BT = c_explainer.new_BT(self.boosted_trees.n_classes)
      for tree in self.boosted_trees.forest:
        c_explainer.add_tree(self.c_BT, tree.raw_data_for_CPP())
    reason = c_explainer.compute_reason(self.c_BT, self.implicant, self.implicant_id_features, self.target_prediction, n_iterations, time_limit, int(reason_expressivity))
    if reason_expressivity == ReasonExpressivity.Conditions:
      return reason
    elif reason_expressivity == ReasonExpressivity.Features:
      return self.to_features_indexes(reason)

  def tree_specific_reason_python(self, seed=0):
    """
    Compute in python only one TS reason.
    """
    abductive = list(self.implicant).copy()
    copy_implicant = list(self.implicant).copy()
    if seed != 0:
      random.seed(seed)
      random.shuffle(copy_implicant)

    for lit in copy_implicant:
      tmp_abductive = abductive.copy()
      tmp_abductive.remove(lit)
      if self.is_implicant(tmp_abductive):
        abductive.remove(lit)
      
    return Explainer.format(abductive)

  def is_implicant(self, abductive):
    if self.boosted_trees.n_classes == 2:
      # 2-classes case
      sum_weights = []
      for tree in self.boosted_trees.forest:
        weights = self.compute_weights(tree, tree.root, abductive)
        worst_weight = min(weights) if self.target_prediction == 1 else max(weights)
        #print(worst_weight, " ", end = "")
        sum_weights.append(worst_weight)
      sum_weights = sum(sum_weights)
      prediction = numpy.argmax([0, 1]) if sum_weights > 0 else numpy.argmax([1, 0])
      #print("result = " , prediction)
      return self.target_prediction == prediction
    else:
      # multi-classes case
      worst_one = self.compute_weights_class(abductive, self.target_prediction, king="worst")
      best_ones = [self.compute_weights_class(abductive, cl, king="best") for cl
      in self.boosted_trees.classes if cl != self.target_prediction]
      return all(worst_one > best_one for best_one in best_ones)

  def compute_weights_class(self, implicant, cls, king="worst"):
    weights = [self.compute_weights(tree, tree.root, implicant) for tree in self.boosted_trees.forest if tree.target_class == cls]
    weights = [min(weights_per_tree) if king=="worst" else max(weights_per_tree) for weights_per_tree in weights]
    return sum(weights)

  def weight_float_to_int(self, weight):
    return weight
    #return int(weight*pow(10,9))

  def compute_weights(self, tree, node, implicant):

    if tree.root.is_leaf(): #Special case for tree without condition
      return [self.weight_float_to_int(tree.root.value)]

    id_variable = tree.get_id_variable(node)
    weights = []
    if id_variable in implicant:
      if node.right.is_leaf():
        return [self.weight_float_to_int(node.right.value)]
      else:
        weights.extend(self.compute_weights(tree, node.right, implicant))
        return weights
    elif -id_variable in implicant:
      if node.left.is_leaf():
        return [self.weight_float_to_int(node.left.value)]
      else:
        weights.extend(self.compute_weights(tree, node.left, implicant))
        return weights
    else: # the variable is not in the implicant
      if node.left.is_leaf():
        weights.append(self.weight_float_to_int(node.left.value))
      else:
        weights.extend(self.compute_weights(tree, node.left, implicant))
      if node.right.is_leaf():
        weights.append(self.weight_float_to_int(node.right.value))
      else:
        weights.extend(self.compute_weights(tree, node.right, implicant))
    return weights

  def reason_to_complete_implicant(self, reason):
    complete = list(reason).copy()
    to_add = [literal for literal in self.implicant if literal not in complete]
    for literal in to_add:
      sign = random.choice([1, -1])
      complete.append(sign * abs(literal))
    return complete

  def check_sufficient(self, reason, n_samples=1000):
    """
    Check if the ''reason'' is abductive and check if the reasons with one selected literal in less are not abductives. This allows to check approximately if the reason is sufficient or not.
    Return nothing, just display the information.       
    
    Args:
        reason (list): The reason.
        n_samples (int, optional): Number of samples to test. Defaults to 1000.
    """
    percentage_abductive = self.check_abductive(reason, n_samples)
    print("check_abductive:", percentage_abductive)
    for lit in reason:
      copy_reason = list(reason).copy()
      copy_reason.remove(lit)
      copy_reason = tuple(copy_reason)
      percentage_current = self.check_abductive(copy_reason, n_samples)
      print("check_sufficient:", percentage_current)


  def check_abductive(self, reason, n_samples=1000):
    """
    Check if ''n_samples'' of complete implicants created from a ''reason'' are alway of the same class. In other words, this method check approximately if a reason seems abductive or not.      
    
    Args:
        reason (list): The reason.
        n_samples (int, optional): Number of samples to test. Defaults to 1000.

    Returns:
        float: The result is in the form of a percentage that represents the amount of complete implicants that are well classified.
    """
    ok_samples = 0
    for _ in range(n_samples):
      complete = self.reason_to_complete_implicant(reason)
      prediction = self.boosted_trees.predict_implicant(complete)
      if prediction == self.target_prediction:
        ok_samples += 1
    return round((ok_samples * 100) / n_samples, 2)
    
  def compute_tree_decomposition(self):
    """
    Compute the treewidth and the optimal tree decomposition.
    """
    tree_decomposition_solver = TreeDecomposition()
    tree_decomposition_solver.create_instance(self.boosted_trees)
    
 