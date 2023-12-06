# oss-project2

이 과제는 두 가지로 나뉘어져 있음.
우선 2-1 과제의 경우 
1.각 년도별 , 기준별 상위 10명의 선수를 판다스의 nlargest(10) 를 이용하여 구하였음.
출력 방식은 각 기준별로 순위 : [기준,수치] , [기준,수치],[기준,수치] 형식의 리스트로 구분하여 보기 쉽게 출력하였음.
2.포지션별 승리 기여도는 마찬가지로 판다스의   nlargest(1)을 사용하여 구하고 바로 출력가능 하도록 구현하였음.
3.연봉과의 상관관계는 corr()을 이용하여 구하였고 가장 큰 수를 가지는 것을 출력하였음.


2-2
1.sort_dataset() 함수 -> sort_values를 사용하여 쉽게 정리하였음.
2.split_dataset() 함수 -> index 슬라이싱을 통해서 범위를 나눴음.
3. extract_numerical_cols() 함수 -> 주어진 numerical만 사용하도록 했음.
4-1.train_predict_decision_tree() 함수 -> DecisionTreeRegressor()를 사용하여 쉽게 구했음.
4-2.train_predict_random_forest() 함수 -> RandomForestRegressor()를 사용하여 쉽게 구했음.
4-3.train_predict_svm() 함수 -> SVR()를 사용하여 쉽게 구했음.
5.calculate_RMSE() 함수 -> np.sqrt(mean_squared_error(labels, predictions)) 사용하여 쉽게 RMSE를 계산함.
