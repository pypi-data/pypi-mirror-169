from pyxai import Learning, Explainer, Tools

#Machine learning part
machine_learning = Learning.Xgboost(Tools.Options.dataset)
model = machine_learning.evaluate(method=Learning.HOLD_OUT, output=Learning.BT)
instance = machine_learning.get_instances(n=1)

#Explanation part
explainer = Explainer.initialize(model, instance)
direct = explainer.direct_reason()
tree_specific = explainer.tree_specific_reason(reason_expressivity=Explainer.CONDITIONS)

#s = explainer.sufficient_reason()


print("direct: ", direct, "\n", len(direct), "\n")
print("check abductive:", explainer.check_abductive(direct))

print("tree_specific: ", tree_specific, "\n", len(tree_specific), "\n")
print("check abductive:", explainer.check_abductive(tree_specific))
