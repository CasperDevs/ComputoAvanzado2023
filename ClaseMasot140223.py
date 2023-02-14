from random import random
#parte del ordenamiento primer paso
def sphere (values):
    return sum(x**2 for x in values)

def NelderMead(function ,li ,ls , n, it, alpha=1, rho=0.5, gamma=1, sigma=0.5):
    pop =[(li+random()*(ls-li) for _ in range(n+1))]
    for item in pop:
        item[-1] = sphere(item [:-1])
    print("\n".join(str(val)for val in pop))
    print("*"*20)
    for _ in range(it):
      pop.sort(key= lambda x:x[-1])
      print("\n".join(str(val)for val in pop))

      m = pop[0][:]
      for item in pop[1:-1]:
        m = [(i+j)/n for i,j in zip(m, item)]
      print(m)
      
