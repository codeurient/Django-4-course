from django.shortcuts import render

# 1) Controller-də 3 dənə metod yaradırıq və bu metodlar 2 dənə parametr qəbul edəcək:
                                                                                        # a) request
                                                                                        # b) product_id

def cart_add(request, product_id):
    ...

def cart_change(request, product_id):
    ...

def cart_remove(request, product_id):
    ...
