    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    #######
    ##  ALGORITM USED: from sklearn.ensemble import RandomForestClassifier
    ##  find more detail at: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
    #######
    
    import matplotlib.pyplot as plt
    from prep_terrain_data import makeTerrainData
    from class_vis import prettyPicture
    
    features_train, labels_train, features_test, labels_test = makeTerrainData()
    
    
    ### the training data (features_train, labels_train) have both "fast" and "slow"
    ### points mixed together--separate them so we can give them different colors
    ### in the scatterplot and identify them visually
    grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
    bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
    grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
    bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]
    
    #### initial visualization
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
    plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.show()
    
    ################################################################################
    
    ### your code here!  name your classifier object clf if you want the 
    ### visualization code (prettyPicture) to show you the decision boundary
    
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    from time import time
    
    features_train, labels_train = RandomForestClassifier.make_classification(n_samples=10, n_features=1,
                                                                              n_informative=2, n_redundant=0,
                                                                              random_state=0, shuffle=False)
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    t0 = time()
    clf.fit(features_train, labels_train)
    print("training time:", round(time()-t0, 3), "s")
    t0 = time()
    pred = clf.predict(features_test)
    
    print("predict time:", round(time()-t0, 3), "s")
    
    ## call the method to show the updated chart.
    
    print("Accuracy precision for Random Forest: %r" % accuracy_score(pred, labels_test))
    print("10th: %r, 26th: %r, 50th: %r" % (pred[10], pred[26], pred[50]))
    print("No. of predicted to be in the 'Chris'(1): %r" % sum(pred))
    
    
    try:
        prettyPicture(clf, features_test, labels_test)
    except NameError:
        pass
    
