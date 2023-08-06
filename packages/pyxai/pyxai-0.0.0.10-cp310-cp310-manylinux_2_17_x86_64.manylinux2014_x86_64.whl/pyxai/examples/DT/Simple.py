from pyxai import Learning, Explainer, Tools
import sys
#Machine learning part
from source.core.structure.type import TypeReason


# usage
# python3 pyxai/examples/DT/Simple.py -dataset=path/to/dataset.csv

machine_learning = Learning.Scikitlearn(Tools.Options.dataset)
model = machine_learning.evaluate(method=Learning.HOLD_OUT, output=Learning.DT)
instance, prediction = machine_learning.get_instances(model, n=1, correct=False)


#Explanation part
explainer = Explainer.decision_tree(model, instance)

print("instance:", instance)
print("instance binarized: ", explainer.implicant)
print("prediction:", prediction)


direct = explainer.direct_reason()
print("\ndirect:", direct)

sufficient_reason = explainer.sufficient_reason(n=1)
#for s in sufficient_reasons:
print("\nsufficient reason:", sufficient_reason)
print("to features", explainer.to_features(sufficient_reason))
assert explainer.is_sufficient(sufficient_reason), "This is have to be a sufficient reason !"

minimal = explainer.minimal_sufficient_reason()
print("\nminimal:", minimal)
assert explainer.is_sufficient(minimal), "This is have to be a sufficient reason !"

print("\nnecessary literals: ", explainer.necessary_literals())
print("\nrelevant literals: ", explainer.relevant_literals())

sufficient_reasons_per_attribute = explainer.n_sufficient_reasons_per_attribute()
print("\nsufficient_reasons_per_attribute:", sufficient_reasons_per_attribute)

preferred_reasons = explainer.minimal_sufficient_reason(n=Explainer.ALL)
print("\npreferred reasons:", preferred_reasons)

constractive_reasons = explainer.contrastive_reason(n=Explainer.ALL)
print("\nconstractive_reasons:", constractive_reasons)

for contrastive in constractive_reasons:
  assert explainer.is_contrastive(contrastive), "This is have to be a contrastive reason !"
