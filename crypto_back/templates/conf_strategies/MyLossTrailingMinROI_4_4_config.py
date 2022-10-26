#  2022-06-15 / 22:30:03
 
import numpy as np 
class config_strategy(): 
    minimal_roi = {
        "0":  0.045
        }
    arg_N =  4
    arg_R =  100
    arg_P =  4
    arg_MR =  0.025
    stoploss = -0.03
    my_stoploss = np.array([32, -0.01])
    arg_stoploss =  0.005
#
    hyperopt = False
#
    buy_cci_val = -50
    sell_cci_val = 100
#    
    buy_adx_val = 32
    buy_fastd_val = 30
    buy_fastk_val = 26
    buy_mfi_val = 22
#    
    buy_adx_enable_val = True
    buy_fastd_enable_val = True
    buy_fastk_enable_val = False
    buy_mfi_enable_val = True
#    
    sell_adx_val = 53
    sell_cci_scalp_val = 183
    sell_fastd_val = 79
    sell_fastk_val = 70
    sell_mfi_val = 92
#    
    sell_adx_enable_val = False
    sell_cci_scalp_enable_val = True
    sell_fastd_enable_val = True
    sell_fastk_enable_val = True
    sell_mfi_enable_val = False