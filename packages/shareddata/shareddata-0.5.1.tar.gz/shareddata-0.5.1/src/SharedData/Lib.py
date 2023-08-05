import pandas as pd
import numpy as np
from numba import njit, prange, jit


def unstack_series(values,symbols):
    tmp = pd.DataFrame(values.unstack())
    tmp['symbol']=symbols.unstack()    
    tmp = tmp.reset_index()
    tmp.columns=['serie','date','value','symbol']
    tmp = tmp.pivot_table(values='value',index='date',columns='symbol')
    return tmp


@njit(parallel=True)
def ffill_sequence(dt_ini_row,dt_end_row, mktdata_cols, sequence_chg, values):
    nsymbols = values.shape[1]
    for dt in range(dt_ini_row,dt_end_row):
        for s in prange(nsymbols):        
            mktdata_s = mktdata_cols[s]
            if (~np.isnan(sequence_chg[dt,mktdata_s])):
                last_s = int(s-sequence_chg[dt,s])
                last_dt = int(dt-1)
                if (np.isnan(values[dt,s])):
                    values[dt,s] = values[last_dt,last_s]


@njit(parallel=True)
def shift_sequence(dt_ini_row,dt_end_row, mktdata_cols, sequence_chg, values):
    nsymbols = values.shape[1]
    for dt in range(dt_ini_row,dt_end_row):
        for s in prange(nsymbols):        
            mktdata_s = mktdata_cols[s]
            if (~np.isnan(sequence_chg[dt,mktdata_s])):
                last_s = int(s-sequence_chg[dt,mktdata_s])
                last_dt = int(dt-1)
                values[dt,s] = values[last_dt,last_s]


@njit(parallel=True)
def mean_sequence(dt_ini_row, dt_end_row, mktdata_cols, sequence_chg, values, values_mean, alpha=0.06):
    nsymbols = values_mean.shape[1]
    for dt in range(dt_ini_row,dt_end_row):        
        for s in prange(nsymbols):        
            mktdata_s = int(mktdata_cols[s])
            if (~np.isnan(sequence_chg[dt,mktdata_s])):
                last_s = int(s-sequence_chg[dt,mktdata_s])
                last_dt = int(dt-1)
                if (~np.isnan(values[dt,s])):

                    if (~np.isnan(mean_sequence[last_dt,last_s])):
                        mean_sequence[dt,s] = values[dt,s]*alpha \
                            + mean_sequence[last_dt,last_s]*(1-alpha)
                    else:
                        mean_sequence[dt,s] = values[dt,s]

                elif (~np.isnan(mean_sequence[last_dt,s])):
                    # forward fill mean sequence
                    mean_sequence[dt,s] = mean_sequence[last_dt,last_s]
            else:
                # first value of sequence
                mean_sequence[dt,s] = values[dt,s]

@njit(parallel=True)
def rollmax_sequence(dt_ini_row, dt_end_row, mktdata_cols, sequence_chg, values, values_rollmax):
    nsymbols = values_rollmax.shape[1]
    for dt in range(dt_ini_row,dt_end_row):
        for s in prange(nsymbols):        
            mktdata_s = int(mktdata_cols[s])
            if (~np.isnan(sequence_chg[dt,mktdata_s])):                
                last_s = int(s-sequence_chg[dt,mktdata_s])
                last_dt = int(dt-1)
                if (~np.isnan(values[dt,s])):

                    if (~np.isnan(values_rollmax[last_dt,last_s])):
                        values_rollmax[dt,s] = max(values_rollmax[last_dt,last_s],values[dt,s])
                    else:
                        values_rollmax[dt,s] = values[dt,s]

                elif (~np.isnan(values_rollmax[last_dt,last_s])):
                    values_rollmax[dt,s] = values_rollmax[last_dt,last_s]

            elif (~np.isnan(values[dt,s])):
                values_rollmax[dt,s] = values[dt,s]


@njit(parallel=True)
def rollmin_sequence(dt_ini_row, dt_end_row, mktdata_cols, sequence_chg, values, values_rollmin):
    nsymbols = values_rollmin.shape[1]
    for dt in range(dt_ini_row,dt_end_row):
        for s in prange(nsymbols):        
            mktdata_s = int(mktdata_cols[s])
            if (~np.isnan(sequence_chg[dt,mktdata_s])):                
                last_s = int(s-sequence_chg[dt,mktdata_s])
                last_dt = int(dt-1)
                if (~np.isnan(values[dt,s])):

                    if (~np.isnan(values_rollmin[last_dt,last_s])):
                        values_rollmin[dt,s] = min(values_rollmin[last_dt,last_s],values[dt,s])
                    else:
                        values_rollmin[dt,s] = values[dt,s]

                elif (~np.isnan(values_rollmin[last_dt,last_s])):
                    values_rollmin[dt,s] = values_rollmin[last_dt,last_s]

            elif (~np.isnan(values[dt,s])):
                values_rollmin[dt,s] = values[dt,s]