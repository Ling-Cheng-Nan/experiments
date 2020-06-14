{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.impute import KNNImputer\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "dict = {'First':[100, 90, np.nan, 95], \n",
    "        'Second': [30, 45, 56, np.nan], \n",
    "        'Third':[np.nan, 40, 80, 98]} \n",
    "    \n",
    "# creating a dataframe from list \n",
    "df = pd.DataFrame(dict)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   First  Second  Third\n",
      "0  100.0    30.0    NaN\n",
      "1   90.0    45.0   40.0\n",
      "2    NaN    56.0   80.0\n",
      "3   95.0     NaN   98.0\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[100.  30.  98.]\n",
      " [ 90.  45.  40.]\n",
      " [ 95.  56.  80.]\n",
      " [ 95.  30.  98.]]\n"
     ]
    }
   ],
   "source": [
    "imputer = KNNImputer(n_neighbors=1 )\n",
    "df_filled = imputer.fit_transform(df)\n",
    "print(df_filled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
