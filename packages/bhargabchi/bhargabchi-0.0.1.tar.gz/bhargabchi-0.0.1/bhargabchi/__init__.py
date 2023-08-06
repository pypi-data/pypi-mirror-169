import numpy as np
import pandas as pd
from scipy import stats

class bg_chi:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.table=pd.crosstab(self.x,self.y) 
    self.chi2,self.p,self.dof,self.exp=stats.chi2_contingency(self.table)
    self.exp_table=pd.DataFrame(self.exp, columns = self.table.columns, index=self.table.index)
  def expected(self):
    return (self.exp_table)
  def chivalue(self):
    return self.chi2
  def pvalue(self):
    return self.p
  def degreeoffreedom(self):
    return self.dof