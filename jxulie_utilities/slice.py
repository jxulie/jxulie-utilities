#-*- coding:UTF-8 -*-
'''
Created on 2016年1月2日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

def slice_dict(origin_dict, slice_num):
    slice_dict = dict()
    for k in range(slice_num):
        slice_dict[k] = dict()
    for i, (key, value) in enumerate(origin_dict.items()):
        slice_dict[i%slice_num].update({key:value})
    
    return slice_dict
    

        