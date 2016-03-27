import numpy as np


def SLS(estimator, X_train, Y_train, X_test, Y_test, r, T, h, d):
    n = X_train.shape[1]
    p = [1 / n] * n
    best_features = []
    score = 0
    error_steps = 0
    for j in range(1, n + 1):
        local_score = 0
        local_features = []
        for t in range(T):
            variates = [np.random.choice(n, j, replace=False, p=p) for q in range(r)]
            tmp_best_features = []
            tmp_worst_features = []
            min_score = 1
            max_score = 0
            for feature_set in variates:
                estimator.fit(X_train[:, feature_set], Y_train)
                score = estimator.score(X_test[:, feature_set], Y_test)
                if score > max_score:
                    max_score = score
                    tmp_best_features = feature_set
                
                if score < min_score:
                    min_score = score
                    tmp_worst_features = feature_set
               
                if score > local_score:
                    local_score = score
                    local_features = feature_set
            H = 0
            for bad_feature in tmp_worst_features:
                p_delta = min(p[bad_feature], h)
                p[bad_feature] -= p_delta
                H += p_delta
            for good_feature in tmp_best_features:
                p[good_feature] += H / j
        estimator.fit(X_train[:, local_features], Y_train)
        current_score = estimator.score(X_test[:, local_features], Y_test)
        if current_score > score:
            score = current_score
            best_features = local_features
            error_steps = 0
        else:
            error_steps += 1
        if error_steps >= d:
            break;
    return best_features
