import jax.numpy as jnp
from jax import random

k=random.PRNGKey(0)
l=random.randint(k,(3,4),1,100)

y=(jnp.sum(l,axis=1)>200).astype(int)
print(l,y)

