# EFA (example)
import pandas as pd
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
df = pd.read_csv("msi_items.csv")   # columns: q1..qk
kmo_all, kmo_model = calculate_kmo(df)
chi_square_value, p_value = calculate_bartlett_sphericity(df)
fa = FactorAnalyzer(rotation='oblimin', method='principal', n_factors=3)
fa.fit(df)
loadings = fa.loadings_
ev, v = fa.get_eigenvalues()

# CFA (example using semopy)
from semopy import Model, Optimizer
model_desc = """
# measurement model
Planning =~ q1 + q2 + q3 + q4
Monitoring =~ q5 + q6 + q7 + q8
Evaluation =~ q9 + q10 + q11
# allow latent covariances
Planning ~~ Monitoring
Planning ~~ Evaluation
Monitoring ~~ Evaluation
"""
mod = Model(model_desc)
res = mod.fit(df)
print(mod.inspect())   # includes loadings, fit indices etc.
