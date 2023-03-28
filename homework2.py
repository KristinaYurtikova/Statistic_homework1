#!/usr/bin/env python
# coding: utf-8

# 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
# 
# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>p</mi>
#   <mo>=</mo>
#   <msubsup>
#     <mi>C</mi>
#     <mrow data-mjx-texclass="ORD">
#       <mn>100</mn>
#     </mrow>
#     <mrow data-mjx-texclass="ORD">
#       <mn>85</mn>
#     </mrow>
#   </msubsup>
#   <mo>&#x22C5;</mo>
#   <msup>
#     <mrow data-mjx-texclass="ORD">
#       <mn>0.8</mn>
#     </mrow>
#     <mrow data-mjx-texclass="ORD">
#       <mn>85</mn>
#     </mrow>
#   </msup>
#   <mo>&#x22C5;</mo>
#   <msup>
#     <mrow data-mjx-texclass="ORD">
#       <mn>0.2</mn>
#     </mrow>
#     <mrow data-mjx-texclass="ORD">
#       <mn>15</mn>
#     </mrow>
#   </msup>
#   <mo>=</mo>
#   <mn>0.048</mn>
# </math>

# In[1]:


import numpy as np
from math import factorial as f

def choose(n,k):
    return f(n) / (f(k) * f(n-k))

def bern(p, n, k):
    return choose(n,k) * p**(k) * (1 - p)**(n - k)

def puas(l,m):
    return l**m/f(m)*np.exp(-l)


# In[2]:


bern(0.8, 100, 85)


# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. К
# акова вероятность, что ни одна из них не перегорит в первый день?
# 
# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>P</mi>
#   <mo>&#x2248;</mo>
#   <mfrac>
#     <msup>
#       <mi>&#x3BB;</mi>
#       <mi>m</mi>
#     </msup>
#     <mrow>
#       <mi>m</mi>
#       <mo>!</mo>
#     </mrow>
#   </mfrac>
#   <msup>
#     <mi>e</mi>
#     <mrow data-mjx-texclass="ORD">
#       <mo>&#x2212;</mo>
#       <mi>&#x3BB;</mi>
#     </mrow>
#   </msup>
#   <mo>&#x2248;</mo>
#   <mfrac>
#     <msup>
#       <mn>2</mn>
#       <mrow data-mjx-texclass="ORD">
#         <mn>0</mn>
#       </mrow>
#     </msup>
#     <mrow>
#       <mn>0</mn>
#       <mo>!</mo>
#     </mrow>
#   </mfrac>
#   <msup>
#     <mi>e</mi>
#     <mrow data-mjx-texclass="ORD">
#       <mo>&#x2212;</mo>
#       <mn>2</mn>
#     </mrow>
#   </msup>
#   <mo>&#x2248;</mo>
#   <mn>0.135</mn>
# </math>
# 
# 

# 
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>&#x3BB;</mi>
#   <mo>=</mo>
#   <mn>5000</mn>
#   <mo>&#x22C5;</mo>
#   <mn>0.0004</mn>
#   <mo>=</mo>
#   <mn>2</mn>
# </math>
# 
# 
# 

# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>m</mi>
#   <mo>=</mo>
#   <mn>0</mn>
# </math>

# In[4]:


lmbd = 5000*0.0004


# In[5]:


puas(lmbd, 0)


#  Какова вероятность, что перегорят ровно две?

# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>P</mi>
#   <mo>&#x2248;</mo>
#   <mfrac>
#     <msup>
#       <mi>&#x3BB;</mi>
#       <mi>m</mi>
#     </msup>
#     <mrow>
#       <mi>m</mi>
#       <mo>!</mo>
#     </mrow>
#   </mfrac>
#   <msup>
#     <mi>e</mi>
#     <mrow data-mjx-texclass="ORD">
#       <mo>&#x2212;</mo>
#       <mi>&#x3BB;</mi>
#     </mrow>
#   </msup>
#   <mo>&#x2248;</mo>
#   <mfrac>
#     <msup>
#       <mn>2</mn>
#       <mrow data-mjx-texclass="ORD">
#         <mn>2</mn>
#       </mrow>
#     </msup>
#     <mrow>
#       <mn>2</mn>
#       <mo>!</mo>
#     </mrow>
#   </mfrac>
#   <msup>
#     <mi>e</mi>
#     <mrow data-mjx-texclass="ORD">
#       <mo>&#x2212;</mo>
#       <mn>2</mn>
#     </mrow>
#   </msup>
#   <mo>&#x2248;</mo>
#   <mn>0.27</mn>
# </math>

# In[7]:


puas(lmbd, 2)


# 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>P</mi>
#   <mo>&#x2248;</mo>
#   <mn>0.063</mn>
# </math>

# In[8]:



bern(0.5, 144, 70)


# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые? 
# 

# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>P</mi>
#   <mo>=</mo>
#   <mo stretchy="false">(</mo>
#   <mfrac>
#     <mn>7</mn>
#     <mn>10</mn>
#   </mfrac>
#   <mo>&#x22C5;</mo>
#   <mfrac>
#     <mn>6</mn>
#     <mn>9</mn>
#   </mfrac>
#   <mo stretchy="false">)</mo>
#   <mo>&#x22C5;</mo>
#   <mo stretchy="false">(</mo>
#   <mfrac>
#     <mn>9</mn>
#     <mn>11</mn>
#   </mfrac>
#   <mo>&#x22C5;</mo>
#   <mfrac>
#     <mn>8</mn>
#     <mn>10</mn>
#   </mfrac>
#   <mo stretchy="false">)</mo>
#   <mo>&#x2248;</mo>
#   <mn>0.31</mn>
# </math>

# In[9]:


(7*6*9*8)/(10*9*11*10)


# Какова вероятность того, что ровно два мяча белые?
# 
# 6 возможных вариантов = (бб)(чч)+(бч)(бч)+(бч)(чб)+(чб)(бч)+(чб)(чб)+(чч)(бб)
# 
# 

# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>P</mi>
#   <mo>&#x2248;</mo>
#   <mn>0.20</mn>
# </math>

# In[10]:


(7/10)*(6/9)*(2/11)*(1/10) + (7/10)*(3/9)*(9/11)*(2/10) + (7/10)*(3/9)*(2/11)*(9/10) + (3/10)*(7/9)*(9/11)*(2/10) + (3/10)*(7/9)*(2/11)*(9/10) + (3/10)*(2/9)*(9/11)*(8/10)


# Какова вероятность того, что хотя бы один мяч белый?
# 
# 1 - вероятность что все черные

# <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
#   <mi>P</mi>
#   <mo>&#x2248;</mo>
#   <mn>0.999</mn>
# </math>

# In[11]:


1-(3/10*2/9*2/11*1/10)


# In[ ]:




