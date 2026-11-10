import pandas as pd
import matplotlib.pyplot as plt

# Read connected flow input in SAS Data and AI Studio
cars = SAS.sd2df(_input1)

cars["Price_Category"] = pd.cut(
    cars["MSRP"],
    bins=[0, 25000, 40000, float("inf")],
    labels=["Budget", "Mid-range", "Premium"]
)

cars["Power_to_Price"] = (
    cars["Horsepower"] / cars["MSRP"] * 10000
)

# Write to connected flow output
SAS.df2sd(cars, _output1)

fig, ax = plt.subplots(figsize=(10, 6))

for origin, group in cars.groupby("Origin"):
    ax.scatter(
        group["Horsepower"],
        group["MSRP"],
        label=origin,
        alpha=0.7,
        s=50
    )

ax.set_title("Horsepower vs MSRP by Vehicle Origin")
ax.set_xlabel("Horsepower")
ax.set_ylabel("MSRP ($)")
ax.legend(title="Origin")
ax.grid(alpha=0.2)

fig.tight_layout()

SAS.pyplot(plt)
plt.close(fig)