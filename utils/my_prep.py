import pandas as pd

class CategoricalEncoder:
    def __init__(self, df, columns=None):
        self.dtypes = df.dtypes.apply(str).to_dict()
        if columns is None:
            self.columns = [k for k in self.dtypes.keys() if self.dtypes[k] == 'object']
        else: 
            self.columns = columns
        self.mapping = self.__get_mapping(df, self.columns)
        
        
    def __get_mapping(self, df, cols) -> dict:
        mapping = {}
        for c in cols:
            unique_cats = df[c].unique()
            # assign to each unique value its number
            mapping[c] = dict(zip(unique_cats, range(len(unique_cats))))
        return mapping
    
    def encode(self, df, col) -> None:
        assert col in self.columns, 'Unknown column. Cannot process further'
        # values not in mapper
        df.loc[~df[col].isin(self.mapping[col].keys()), col] = -1
        # values in mapper
        df[col].replace(to_replace=self.mapping[col], inplace=True)
    
    def decode(self, df, col) -> None:
        assert col in self.columns, 'Unknown column. Cannot process further'
        inv_mapping = {v: k for k, v in self.mapping[col].values()}
        df.loc[~df[col].isin(inv_mapping.keys()), col] = None