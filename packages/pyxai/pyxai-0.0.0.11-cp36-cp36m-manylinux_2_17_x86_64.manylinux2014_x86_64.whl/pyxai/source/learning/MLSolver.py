
import shutil
from typing import Iterable
import numpy
import pandas
import os
import json
import random
import copy

from pyxai.source.core.structure.type import EvaluationMethod, EvaluationOutput, TypeReason, Indexes, SaveFormat
from pyxai.source.core.tools.utils import shuffle, flatten, compute_accuracy

from pyxai.source.core.structure.boostedTrees import BoostedTrees
from pyxai.source.core.structure.randomForest import RandomForest
from pyxai.source.core.structure.decisionTree import DecisionTree



from collections import OrderedDict
from sklearn.model_selection import LeaveOneGroupOut, train_test_split, KFold


class MLSolverInformation():
    def __init__(self, raw_model, training_index, test_index, group, accuracy):
      self.raw_model = raw_model
      self.training_index = training_index 
      self.test_index = test_index
      self.group = group
      self.accuracy = accuracy

    def set_solver_name(self, solver_name):
      self.solver_name = solver_name

    def set_feature_name(self, feature_name):
      self.feature_name = feature_name

    def set_evaluation_method(self, evaluation_method):
      self.evaluation_method = str(evaluation_method)

    def set_evaluation_output(self, evaluation_output):
      self.evaluation_output = str(evaluation_output)

class MLSolver():
    """
    Load the dataset, rename the attributes and separe the prediction from the data
    instance = observation 
    labels != prediction
    attributes = features
    """
    def __init__(self, dataset):
      if dataset is None or dataset == "None":
        self.data = None
        self.labels = None
        self.ML_solver_information = []
        if dataset is None:
          print("Warning: you have given a dataset but this dataset is None !")
        return None
      self.load_data(dataset)     

    def count_lines(self, filename):
      with open(filename) as f:
        return sum(1 for _ in f)

    def load_data_limited(self, datasetname, possibles_indexes, n):
      self.datasetname = datasetname
      print(self.datasetname)
      n_indexes = self.count_lines(datasetname) - 1 #to skip the first line
      print(n_indexes)
      
      skip = [i+1 for i in range(n_indexes) if i not in possibles_indexes] if possibles_indexes is not None else None
      
      # create a map to get the good order of instances
      if skip is not None:
        sorted_possibles_indexes = sorted(possibles_indexes)
        map_possibles_indexes = [sorted_possibles_indexes.index(index) for index in possibles_indexes]

      data = pandas.read_csv(
        datasetname,
        skiprows=skip,
        nrows=n
      )
    
      #numpy_data = data.to_numpy()
      #sorted_data = [numpy_data[map_possibles_indexes[i]].tolist() for i in range(len(numpy_data))]
      
      # recreate the dataframe object but with the good order of instances
      if skip is not None:
        sorted_data = pandas.DataFrame(columns = data.columns).astype(data.dtypes)
        for i in range(data.shape[0]):
          sorted_data = sorted_data.append(data.loc[map_possibles_indexes[i]].to_dict(),ignore_index=True)
        sorted_data = sorted_data.astype(data.dtypes)
      
      n_instances, n_features = data.shape
      self.rename_attributes(data)
      data, labels = self.remove_labels(data, n_features)
      labels = self.labelsToValues(labels)
      data = data.to_numpy()
      
      return data, labels

    def load_data(self, datasetname):
      self.datasetname = datasetname 
      self.data = pandas.read_csv(datasetname).copy()
      print(self.data)
      self.n_instances, self.n_features = self.data.shape
      self.feature_name = self.data.columns.values.tolist() 
      
      self.rename_attributes(self.data)
      self.data, self.labels = self.remove_labels(self.data, self.n_features)
      self.create_dict_labels(self.labels)
      self.labels = self.labelsToValues(self.labels)
      
      self.n_labels = len(set(self.labels))
      self.data = self.data.to_numpy() #remove the first line (attributes) and now the first dimension represents the instances :)!
      
      self.ML_solver_information = []
      print("---------------   Information   ---------------")
      print("Dataset name:", datasetname)
      print("nFeatures (nAttributes, with the labels):", self.n_features)
      print("nInstances (nObservations):", self.n_instances)
      print("nLabels:", self.n_labels)

    """
    Rename attributes in self.data in string of integers from 0 to 'self.n_attributes'
    """
    def rename_attributes(self, data):
      rename_dictionary = {element: str(i) for i, element in enumerate(data.columns)}
      data.rename(columns=rename_dictionary, inplace=True)

    def create_dict_labels(self, labels):
      index = 0
      self.dict_labels = OrderedDict()
      for p in labels:
        if str(p) not in self.dict_labels:
          self.dict_labels[str(p)] = index
          index+=1

    """
    Convert labels (predictions) into binary values
    Using of OrderedDict in order to be reproducible.
    """
    def labelsToValues(self, labels):
      return [self.dict_labels[str(element)] for element in labels]

    """
    Remove and get the prediction: it is the last attribute (column) in the file
    """
    def remove_labels(self, data, n_features):
      prediction = data[str(n_features-1)].copy().to_numpy()
      data = data.drop(columns=[str(n_features-1)])
      return data, prediction
    
    """
    Method:

    """
    def evaluate(self, *, method, output, n_models=10, test_size=0.3, seed=0, model_directory=None):
      print("---------------   Evaluation   ---------------")
      print("method:", str(method))
      print("output:", str(output))
      
      if method == EvaluationMethod.HoldOut:
        self.hold_out_evaluation(output, test_size=test_size, seed=seed)
      elif method == EvaluationMethod.LeaveOneGroupOut:
        self.leave_one_group_out_evaluation(output, n_trees=n_models, seed=seed)
      elif method == EvaluationMethod.KFolds:
        self.k_folds_evaluation(output, n_models=n_models, seed=seed)
      else:
        assert False, "Not implemented !"

      for ML_solver_information in self.ML_solver_information:
        ML_solver_information.set_solver_name(self.get_solver_name())
        ML_solver_information.set_feature_name(self.feature_name)
        ML_solver_information.set_evaluation_method(method)
        ML_solver_information.set_evaluation_output(output)

      print("---------   Evaluation Information   ---------")
      for i, result in enumerate(self.ML_solver_information):
        print("For the evaluation number " + str(i) + ":")
        print("accuracy:", result.accuracy)
        print("nTraining instances:",len(result.training_index))
        print("nTest instances:", len(result.test_index))
        print()  

      print("---------------   Explainer   ----------------")
      result_output = None
      if output == EvaluationOutput.DT:
        result_output = self.to_DT(self.ML_solver_information)
      elif output == EvaluationOutput.RF:
        result_output = self.to_RF(self.ML_solver_information)
      elif output == EvaluationOutput.BT:
        result_output = self.to_BT(self.ML_solver_information)
      else:
        assert False, "Not implemented !"
      #elif output == EvaluationOutput.SAVE:
      #  self.save_model(model_directory)
      #  result_output = self.to_BT()
      
      for i, result in enumerate(result_output):
        print("For the evaluation number " + str(i) + ":")
        print(result)
      return result_output if len(result_output) != 1 else result_output[0]

    def load_get_files(self, model_directory):
      assert model_directory is not None and os.path.exists(model_directory), "The path of model_directory do not exist: " + str(model_directory)
      
      self.ML_solver_information.clear()
      #get the files
      files = []
      index = 0
      found = True
      while found:
        found = False
        for filename in os.listdir(model_directory): 
          model_file = os.path.join(model_directory, filename) 
          if os.path.isfile(model_file) and model_file.endswith(str(index)+".model"):
            map_file = model_file.replace(".model", ".map")
            assert os.path.isfile(map_file), "A '.model' file must be accompanied by a '.map' file !"
            files.append((model_file, map_file)) 
            index += 1
            found = True
            break
      
      assert len(files) != 0, "No file representing a model in the path: " + model_directory 
      return files

    def load(self, *, model_directory, with_tests=False):
      files = self.load_get_files(model_directory)
      
      for _, model in enumerate(files):
        model_file, map_file = model

        #recuperate map
        f = open(map_file)
        data = json.loads(json.load(f))
        training_index = data['training_index']
        test_index = data['test_index']
        accuracy_saved = data['accuracy']
        solver_name =  data['solver_name'] 
        evaluation_method =  data['evaluation_method'] 
        evaluation_output =  data['evaluation_output'] 
        
        self.n_features = data['n_features']
        self.n_labels = data["n_labels"]
        self.dict_labels = data["dict_labels"]
        self.feature_name = data["feature_name"]

        f.close()
        
        assert self.get_solver_name() == solver_name, "You try to load a model with " + self.get_solver_name() + ", but you have save the model with " + solver_name + " !"

        #load model
        classifier = self.load_model(model_file)

        print("----------   Loading Information   -----------")
        print("mapping file:", map_file)
        print("nFeatures (nAttributes, with the labels):", self.n_features)
        print("nInstances (nObservations):", len(training_index) + len(test_index))
        print("nLabels:", self.n_labels)
        if with_tests is True:
          # Test phase
          instances_test = [self.data[i] for i in test_index]
          labels_test = [self.labels[i] for i in test_index]
          result = classifier.predict(instances_test)
          accuracy = compute_accuracy(result, labels_test)
          assert accuracy == accuracy_saved, "The accuracy between the model loaded and the one determined at its creation is not the same !"
        self.ML_solver_information.append(MLSolverInformation(copy.deepcopy(classifier),training_index,test_index,None,accuracy_saved))
        self.ML_solver_information[-1].set_solver_name(solver_name)
        self.ML_solver_information[-1].set_evaluation_method(evaluation_method)
        self.ML_solver_information[-1].set_evaluation_output(evaluation_output)
        self.ML_solver_information[-1].set_feature_name(self.feature_name)

      assert all(ML_solver_information.evaluation_output == self.ML_solver_information[-1].evaluation_output for ML_solver_information in self.ML_solver_information), "All evaluation outputs have to be the same !"

      print("---------   Evaluation Information   ---------")
      for i, result in enumerate(self.ML_solver_information):
        print("For the evaluation number " + str(i) + ":")
        print("accuracy:", result.accuracy)
        print("nTraining instances:",len(result.training_index))
        print("nTest instances:", len(result.test_index))
        print()
        
      print("---------------   Explainer   ----------------")
      output = EvaluationOutput.from_str(self.ML_solver_information[-1].evaluation_output)
      result_output = None

      if output == EvaluationOutput.DT:
        result_output = self.to_DT(self.ML_solver_information)
      elif output == EvaluationOutput.RF:
        result_output = self.to_RF(self.ML_solver_information)
      elif output == EvaluationOutput.BT:
        result_output = self.to_BT(self.ML_solver_information)
      else:
        assert False, "Not implemented !"
      
      for i, result in enumerate(result_output):
        print("For the evaluation number " + str(i) + ":")
        print(result)
      return result_output if len(result_output) != 1 else result_output[0]
  
    def save(self, models, model_directory, generic=False):
      
      name = self.datasetname.split(os.sep)[-1].split('.')[0]
      if model_directory is not None:
        if not os.path.exists(model_directory):
          os.makedirs(model_directory)
        base_directory = model_directory + os.sep + name + "_model" 
      else:
        base_directory = name + "_model"
        
      shutil.rmtree(base_directory, ignore_errors=True)
      os.mkdir(base_directory)

      if not isinstance(models, Iterable):
        models = [models]
      
      for i, trees in enumerate(models):
        ML_solver_information = trees.ML_solver_information
        filename = base_directory + os.sep + name + '.' + str(i)
        # model:
        if generic is False:
          self.save_model(ML_solver_information, filename)
        else:
          
          self.save_model_generic(trees, filename)
        # map of indexes for training and test part
        data = {"training_index": ML_solver_information.training_index.tolist(), 
                "test_index": ML_solver_information.test_index.tolist(),
                "accuracy": ML_solver_information.accuracy,
                "solver_name": ML_solver_information.solver_name if generic is False else "Generic", 
                "evaluation_method": ML_solver_information.evaluation_method,
                "evaluation_output": ML_solver_information.evaluation_output,
                "format": str(format),
                
                "n_features": self.n_features, 
                "n_labels": self.n_labels,
                "dict_labels": self.dict_labels,
                "feature_name": self.feature_name}

        json_string = json.dumps(data)
        with open(filename + ".map", 'w') as outfile:
          json.dump(json_string, outfile)
        
        print("Model saved in:", base_directory)

    def save_model_generic(self, trees, filename):
      json_string = json.dumps(trees.raw_data())
      with open(filename + ".model", 'w') as outfile:
        json.dump(json_string, outfile)


    def hold_out_evaluation(self, output, *, seed=0, test_size=0.3):
      self.ML_solver_information.clear()
      assert self.data is not None, "You have to put the dataset in the class parameters."
      #spliting
      indices = numpy.arange(len(self.data))
      instances_training, instances_test, labels_training, labels_test, training_index, test_index = train_test_split(self.data, self.labels, indices, test_size = test_size, random_state = seed)
      
      #solving
      if output == EvaluationOutput.DT:
        tree, accuracy = self.fit_and_predict_DT(instances_training, instances_test, labels_training, labels_test)
      elif output == EvaluationOutput.RF:
        tree, accuracy = self.fit_and_predict_RF(instances_training, instances_test, labels_training, labels_test)
      elif output == EvaluationOutput.BT:
        tree, accuracy = self.fit_and_predict_BT(instances_training, instances_test, labels_training, labels_test)
      else:
        assert False, "hold_out_evaluation: EvaluationOutput Not implemented !"

      self.ML_solver_information.append(MLSolverInformation(tree,training_index,test_index,None,accuracy))
      return self

    def k_folds_evaluation(self, output, *, n_models=10, seed=0):
      assert self.data is not None, "You have to put the dataset in the class parameters."
      assert n_models > 1, "This k_folds_evaluation() expects at least 2 parts. For just one tree, please use hold_out_evaluation()"
      self.ML_solver_information.clear()

      cross_validator = KFold(n_splits=n_models, random_state=seed, shuffle=True)
      
      for training_index, test_index in cross_validator.split(self.data):
        # Select good observations for each of the 'n_trees' experiments.
        instances_training = [self.data[i] for i in training_index]
        labels_training = [self.labels[i] for i in training_index]
        instances_test = [self.data[i] for i in test_index]
        labels_test = [self.labels[i] for i in test_index]
        
        #solving
        if output == EvaluationOutput.DT:
          tree, accuracy = self.fit_and_predict_DT(instances_training, instances_test, labels_training, labels_test)
        elif output == EvaluationOutput.RF:
          tree, accuracy = self.fit_and_predict_RF(instances_training, instances_test, labels_training, labels_test)
        elif output == EvaluationOutput.BT:
          tree, accuracy = self.fit_and_predict_BT(instances_training, instances_test, labels_training, labels_test)
        else:
          assert False, "leave_one_group_out_evaluation: EvaluationOutput Not implemented !"

        # Save some information
        self.ML_solver_information.append(MLSolverInformation(tree,training_index,test_index,None,accuracy))
      return self

    def leave_one_group_out_evaluation(self, output, *, n_trees=10, seed=0):
      assert self.data is not None, "You have to put the dataset in the class parameters."
      assert n_trees > 1, "cross_validation() expects at least 2 trees. For just one tree, please use simple_validation()"
      self.ML_solver_information.clear()

      #spliting
      quotient, remainder = (self.n_instances//n_trees, self.n_instances%n_trees) 
      groups = flatten([quotient*[i] for i in range(1, n_trees + 1)]) + [i for i in range(1, remainder + 1)]
      random.Random(seed).shuffle(groups)
      cross_validator = LeaveOneGroupOut()
      
      for training_index, test_index in cross_validator.split(self.data, self.labels, groups):
        # Select good observations for each of the 'n_trees' experiments.
        instances_training = [self.data[i] for i in training_index]
        labels_training = [self.labels[i] for i in training_index]
        instances_test = [self.data[i] for i in test_index]
        labels_test = [self.labels[i] for i in test_index]
        
        #solving
        #solving
        if output == EvaluationOutput.DT:
          tree, accuracy = self.fit_and_predict_DT(instances_training, instances_test, labels_training, labels_test)
        elif output == EvaluationOutput.RF:
          tree, accuracy = self.fit_and_predict_RF(instances_training, instances_test, labels_training, labels_test)
        elif output == EvaluationOutput.BT:
          tree, accuracy = self.fit_and_predict_BT(instances_training, instances_test, labels_training, labels_test)
        else:
          assert False, "leave_one_group_out_evaluation: EvaluationOutput Not implemented !"

        # Save some information
        self.ML_solver_information.append(MLSolverInformation(tree,training_index,test_index,groups,accuracy))
      return self

    """
    Return couples (instance, prediction) from data and the MLsolver results.
    
    'indexes': take only into account some indexes of instances
      - Indexes.Training: indexes from the training instances of a particular model 
      - Indexes.Test: indexes from the test instances of a particular model
      - Indexes.Mixed: take firsly indexes from the test set and next from the training set in order to have at least 'n' instances. 
      - Indexes.All: all indexes are take into account
      - string: A file contening specific indexes 
    
    'dataset': 
      - can be None if the dataset is already loaded
      - the dataset if you have not loaded it yet
      
    'model':
      - a model for the 'type=training' or 'type=test'
        
    'n': The desired number of instances (None for all).

    'correct': only available if a model is given 
      - None: all instances
      - True: only correctly classified instances by the model 
      - False: only misclassified instances by the model 

    'classes': 
      - None: all instances
      - []: List of integers representing the classes/labels for the desired instances  

    'backup_directory': save the instance indexes in a file in the directory given by this parameter 
    """
    def get_instances(self, model=None, indexes=Indexes.All, *, dataset=None, n=None, correct=None, predictions=None, backup_directory=None, backup_id=None):
      print("---------------   Instances   ----------------")
      print("Correctness of instances : ", correct)
      print("Predictions of instances: ", predictions)
      
      assert isinstance(indexes, (Indexes, str)), "Bad value in the parameter 'indexes'"
      if model is None: 
        assert indexes == Indexes.All, "Please insert the model to use this parameter !"
        assert correct is None, "Please insert the model to use this parameter !"
        assert predictions is None, "Please insert the model to use this parameter !"
        # In this case, no prediction, just return some instances
      elif isinstance(model, Iterable):
        assert False, "The model is not a model !"
      else:
        #depending of the model
        if isinstance(model, BoostedTrees):
          id_solver_results = model.forest[0].id_solver_results
          classifier = self.ML_solver_information[id_solver_results].raw_model
          results = self.ML_solver_information[id_solver_results]
        if isinstance(model, RandomForest):
          assert False, "Not implemented !"
        if isinstance(model, DecisionTree):
          id_solver_results = model.id_solver_results
          classifier = self.ML_solver_information[id_solver_results].raw_model
          results = self.ML_solver_information[id_solver_results]
          
      # starting by get the correct indexes:
      possible_indexes = None

      if isinstance(indexes, str):
        if os.path.isfile(indexes):
          files_indexes = indexes
        elif os.path.isdir(indexes):
          if backup_id is None:
            found = False
            for filename in os.listdir(indexes): 
              file = os.path.join(indexes, filename)
              if os.path.isfile(file) and file.endswith(".instances"):
                  files_indexes = file
                  assert found is False, "Too many .instances files in the directory: " + indexes + " Please put directly the good file in the option or use the backup_id parameter !"
                  found = True
          else:
            found = False
            for filename in os.listdir(indexes): 
              file = os.path.join(indexes, filename)
              if os.path.isfile(file) and file.endswith("." + str(backup_id) + ".instances"):
                  files_indexes = file
                  found = True
                  break
            assert found is True, "No ." + str(backup_id) + ".instances" + " files in the directory: " + indexes + " Please put directly the good file in the option or use the backup_id parameter !"
                          
        print("instances file:", files_indexes)
        f = open(files_indexes)
        data = json.loads(json.load(f))
        possible_indexes = data['indexes']
        f.close()

      elif indexes == Indexes.Training or indexes == Indexes.Test or indexes == Indexes.Mixed:
        possible_indexes = results.training_index if indexes == Indexes.Training else results.test_index
        if indexes == Indexes.Mixed and n is not None and len(possible_indexes) < n:
          for i in range(n + 1 - len(possible_indexes)):
            if i < len(results.training_index):      
              possible_indexes = numpy.append(possible_indexes, results.training_index[i])
      
      # load data and get instances
      if self.data is None:
        assert dataset is not None, "Data are not loaded yet. You have to put your dataset filename through the 'dataset' parameter !"
        data, labels = self.load_data_limited(dataset, possible_indexes, n)
      else:
        if possible_indexes is None: 
          data = self.data
          labels = self.labels 
        else:
          data = numpy.array([self.data[x] for x in possible_indexes])
          labels = numpy.array([self.labels[x] for x in possible_indexes])
      
      if possible_indexes is None:
        possible_indexes = [i for i in range(len(data))]
      
      if isinstance(possible_indexes, numpy.ndarray):
        possible_indexes = possible_indexes.tolist()

      # select instance according to parameters
      instances = []
      instances_indexes = []
      if model is None:
        for j in range(len(data)):
          current_index = possible_indexes[j]
          instances.append(data[j])
          instances_indexes.append(current_index)
          if isinstance(n, int) and len(instances) >= n:
            break
      else:
        for j in range(len(data)):
          current_index = possible_indexes[j]
          prediction_solver = classifier.predict(data[j].reshape(1, -1))[0] #J'ai, a priori de la chance, que la fonction predict de xgboost et scikit learnt ont la meme def !
          label = labels[j]
          if (correct is True and prediction_solver == label) \
            or (correct is False and prediction_solver != label) \
            or (correct is None):
            if predictions is None or prediction_solver in predictions:
              instances.append((data[j], prediction_solver))
              instances_indexes.append(current_index)
          if isinstance(n, int) and len(instances) >= n:
            break
      
      if backup_directory is not None:
        # we want to save the instances indexes in a file
        name = self.datasetname.split(os.sep)[-1].split('.')[0]
        if not os.path.isdir(backup_directory):
          os.mkdir(backup_directory)
        base_directory = backup_directory + os.sep + name + "_model" 
        if not os.path.isdir(base_directory):
          os.mkdir(base_directory)
        if backup_id is None:  
          complete_name = base_directory + os.sep + name + ".instances"
        else:
          complete_name = base_directory + os.sep + name + "." + str(backup_id) + ".instances"
        data = {"dataset": name, 
                "n": len(instances_indexes),
                "indexes": instances_indexes}

        json_string = json.dumps(data)
        with open(complete_name, 'w') as outfile:
          json.dump(json_string, outfile)
        
        print("Indexes of selected instances saved in:", complete_name)
      print("number of instances selected:", len(instances))
      print("----------------------------------------------")
      return instances if len(instances) != 1 else instances[0] 
    

