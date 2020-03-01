# Decision Tree in Python

Decision Tree ID3 without using builtin libraries. 

***Heuristics Usesd:***
- [Information Gain](https://en.wikipedia.org/wiki/Information_gain_in_decision_trees) as H1
- [Variance Impurity](https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity) as H2

***Accuracy***
1. Dataset 1: </br>
- H1 Training 0.7967
- H1 Test 0.73
- H1 Validation 0.7783
- H2 Training 0.80
- H2 Test 0.7333
- H2 Validation 0.7783
2. Dataset 2:</br>
- H1 Training 0.63</br>
- H1 Test 0.57</br>
- H1 Validation 0.5883</br>
- H2 Training 0.6266</br>
- H2 Test 0.57</br>
- H2 Validation 0.59</br>

***Compiling Instrucitons:***
python3 main.py training_set.csv validation_set.csv test_set.csv to_print huristics
