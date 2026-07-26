import jax.numpy as jnp
from jax import random
from jax import grad

l=random.PRNGKey(0)


nums=random.randint(l,(10,),minval=0,maxval=100)

print(nums)

def f(x):
    return jnp.sin(x)+x**2

l=jnp.linspace(10,100,10)

y=f(l)
y=jnp.round(y).astype(int)
print(y)

df=grad(f,allow_int=True)
print("the value of :",df(2.0))
