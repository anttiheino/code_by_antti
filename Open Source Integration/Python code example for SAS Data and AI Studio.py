import matplotlib.pyplot as plt

# Read the SAS table into a pandas DataFrame
carsdf = SAS.sd2df("sashelp.cars")

# Filter to Honda vehicles
vehicle_make = "Honda"
mycars = carsdf[carsdf["Make"] == vehicle_make].copy()

# Calculate average MSRP
avg_msrp = round(mycars["MSRP"].mean())
print(f"Average MSRP for {vehicle_make}: ${avg_msrp:,.0f}")

# Write the filtered DataFrame back to SAS
SAS.df2sd(mycars, "work.filtered_cars")

# Create the histogram
fig, ax = plt.subplots(figsize=(10, 6))

counts, bins, patches = ax.hist(
    mycars["MPG_Highway"].dropna(),
    bins=8,
    edgecolor="white",
    linewidth=1
)

# Apply a yellow-to-blue gradient
cmap = plt.colormaps["viridis"]
for i, patch in enumerate(patches):
    position = i / max(len(patches) - 1, 1)
    patch.set_facecolor(cmap(position))

ax.set_title(
    f"Distribution of Highway MPG for {vehicle_make} Cars",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Highway MPG")
ax.set_ylabel("Number of Cars")
ax.grid(axis="y", alpha=0.2)

fig.tight_layout()
# Render the plot in the SAS Studio Results panel
SAS.pyplot(plt)
# Close the figure after SAS has rendered it
plt.close(fig)
# Print the first rows to the output
print(mycars.head())