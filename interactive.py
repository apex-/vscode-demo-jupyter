# %%
import plotly.express as px

df = px.data.gapminder().query("continent != 'Asia'") # remove Asia for visibility
fig = px.line(df, x="year", y="lifeExp", color="continent",
              line_group="country", hover_name="country")
fig.show()


# %%
# Calculate Prime Numbers
import itertools

def iter_primes():
     numbers = itertools.count(2)
     while True:
         prime = next(numbers)
         yield prime
         numbers = filter(prime.__rmod__, numbers)

for p in iter_primes():
    if p > 1000:
        break
    print (p)

# %%
