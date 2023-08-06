from time import time
from pyxai import Learning, Explainer, Tools

# To use with the minist dataset (classification between 4 and 9 or between 3 and 8
# available here:
# http://www.cril.univ-artois.fr/expekctation/datasets/mnist38.csv
# http://www.cril.univ-artois.fr/expekctation/datasets/mnist49.csv


# the location of the dataset
path = "."
dataset = "mnist38.csv"

#Machine learning part
machine_learning = Learning.Scikitlearn(f"{path}/{dataset}")
model = machine_learning.evaluate(method=Learning.HoldOut, output=Learning.DT)
instance, prediction = machine_learning.get_instances(model, n=1, correct=True)

print("instance:", instance)
print("prediction:", prediction)

#Explanation part
explainer = Explainer.initialize(model, instance)
direct = explainer.direct_reason()
print("direct:", direct)

sufficient_reason = explainer.sufficient_reason(n=1, time_limit=2)

assert explainer.is_sufficient(sufficient_reason), "This is have to be a sufficient reason !"

minimal = explainer.minimal_sufficient_reason()
print("minimal:", minimal)
assert explainer.is_sufficient(minimal), "This is have to be a sufficient reason !"

sufficient_reasons_per_attribute = explainer.n_sufficient_reasons_per_attribute()
print("\nsufficient_reasons_per_attribute:", sufficient_reasons_per_attribute)

preferred_reasons = explainer.preferred_reason(method=Explainer.WEIGHTS, n=Explainer.ALL, weights=sufficient_reasons_per_attribute)
print("preferred reasons:", preferred_reasons)


#Heatmap part

heatmap = Tools.HeatMap(28, 28, instance)

image1 = heatmap.new_image("Instance").set_instance(instance)

image2 = heatmap.new_image("Direct Vs Minimal")
image2.add_features(explainer.to_features(direct))
image2.add_features(explainer.to_features(minimal))

image4 = heatmap.new_image("Prefered")
image4.add_features(explainer.to_features(preferred_reasons[0]))


heatmap.display()