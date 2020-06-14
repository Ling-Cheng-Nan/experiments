{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.impute import KNNImputer\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "np.set_printoptions(precision=3)\n",
    "\n",
    "dict = {'First':  [70, 100, 90, np.nan, 95, 40, 53, 88, 15, 20], \n",
    "        'Second': [20, 30, 45, 56, np.nan, 10, np.nan, 32, 9, 7], \n",
    "        'Third':  [np.nan, np.nan, 40, 80, 98, 70, 21, 43, 12, 33],\n",
    "        'Fourth': [64, 20, 54, 90, 70, 81, 22, 10, 70, 4],\n",
    "        'Fifth':  [np.nan, np.nan, 74, np.nan, 10, 51, 17, 23, 87, 19],\n",
    "        'Sixth':  [82, np.nan,5,20,np.nan, np.nan,np.nan, 50, 4, 11]\n",
    "       }\n",
    "# creating a dataframe from list \n",
    "df = pd.DataFrame(dict)\n"
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
      "   First  Second  Third  Fourth  Fifth  Sixth\n",
      "0   70.0    20.0    NaN      64    NaN   82.0\n",
      "1  100.0    30.0    NaN      20    NaN    NaN\n",
      "2   90.0    45.0   40.0      54   74.0    5.0\n",
      "3    NaN    56.0   80.0      90    NaN   20.0\n",
      "4   95.0     NaN   98.0      70   10.0    NaN\n",
      "5   40.0    10.0   70.0      81   51.0    NaN\n",
      "6   53.0     NaN   21.0      22   17.0    NaN\n",
      "7   88.0    32.0   43.0      10   23.0   50.0\n",
      "8   15.0     9.0   12.0      70   87.0    4.0\n",
      "9   20.0     7.0   33.0       4   19.0   11.0\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 70.     20.     52.     64.     40.143  82.   ]\n",
      " [100.     30.     55.     20.     40.143  28.667]\n",
      " [ 90.     45.     40.     54.     74.      5.   ]\n",
      " [ 71.143  56.     80.     90.     40.143  20.   ]\n",
      " [ 95.     28.571  98.     70.     10.     28.667]\n",
      " [ 40.     10.     70.     81.     51.     28.667]\n",
      " [ 53.     21.857  21.     22.     17.     28.667]\n",
      " [ 88.     32.     43.     10.     23.     50.   ]\n",
      " [ 15.      9.     12.     70.     87.      4.   ]\n",
      " [ 20.      7.     33.      4.     19.     11.   ]]\n"
     ]
    }
   ],
   "source": [
    "#take mean of k-nearest neigbors, \n",
    "#if k > number of all rows then k = # of rows\n",
    "\n",
    "imputer = KNNImputer(n_neighbors = 7)\n",
    "df_filled = imputer.fit_transform(df)\n",
    "\n",
    "print(df_filled)\n",
    "#for i in range(df_filled.shape[0]):\n",
    "#    print ([ '%.5f' %x for x in df_filled[i] ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
