# ========================LICENSE_START=================================
#   O-RAN-SC
#   %%
#   Copyright (c) 2019 AT&T Intellectual Property.
#   %%
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ========================LICENSE_END===================================

from acumos.session import AcumosSession
from acumos.modeling import Model, List, create_dataframe

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

clf = RandomForestClassifier(random_state=0)
clf.fit(X, y)

# here, an appropriate NamedTuple type is inferred from a pandas DataFrame
X_df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
IrisDataFrame = create_dataframe('IrisDataFrame', X_df)

# ==================================================================================
# # or equivalently:
#
# IrisDataFrame = create_namedtuple('IrisDataFrame', [('sepal_length', List[float]),
#                                                     ('sepal_width', List[float]),
#                                                     ('petal_length', List[float]),
#                                                     ('petal_width', List[float])])
# ==================================================================================

def classify_iris(df: IrisDataFrame) -> List[int]:
    '''Returns an array of iris classifications'''
    X = np.column_stack(df)
    return clf.predict(X)

model = Model(classify=classify_iris)

session = AcumosSession()

session.dump(model,'iris_sklearn','/temp')
