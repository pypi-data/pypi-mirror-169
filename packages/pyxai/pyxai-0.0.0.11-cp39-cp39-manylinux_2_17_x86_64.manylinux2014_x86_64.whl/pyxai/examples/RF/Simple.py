from pyxai import Learning, Explainer, Tools

#Machine learning part
machine_learning = Learning.Scikitlearn(Tools.Options.dataset)
model = machine_learning.evaluate(method=Learning.HOLD_OUT, output=Learning.RF)
instance = machine_learning.get_instances(n=1)

# Explainer part
explainer = Explainer.initialize(model, instance=instance)

direct = explainer.direct_reason()
print("direct:", direct)

majoritary = explainer.majoritary_reason(n = 1)
print("majoritary:", majoritary)

print("len direct: ", len(direct), "  majoritary: ", len(majoritary))

if len(majoritary) < 100:
  print("is_majoritary_implicant:", explainer.is_majoritary(majoritary))
