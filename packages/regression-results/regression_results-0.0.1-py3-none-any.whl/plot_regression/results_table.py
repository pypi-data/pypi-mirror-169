import statsmodels.api as sm


def result_table(var_dep, var_pred):

    results = sm.OLS(var_dep, var_pred).fit()

    outs = print(results.summary())

    return outs
