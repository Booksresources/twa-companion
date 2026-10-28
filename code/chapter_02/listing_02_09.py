# Listing 2.9: Monthly volume and average rating
exec(open("l7.py").read().split("print(df[")[0])
monthly = (df.set_index("date")
             .resample("MS")["rating"]
             .agg(["count", "mean"]))
print(monthly)
