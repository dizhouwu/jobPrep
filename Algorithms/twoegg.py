
# coding: utf-8

# In[1]:


import functools
@functools.lru_cache(maxsize = None)

#n is floor and m is egg
def f(n, m):
    if n == 0:
        return 0
    if m == 1:
        return n
    
    ans = min([max([f(i - 1, m - 1), f(n - i, m)]) for i in range(1, n + 1)]) + 1

    return ans


# In[2]:


f(100, 2)

