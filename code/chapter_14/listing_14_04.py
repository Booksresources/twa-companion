# Listing 14.4: Detecting bursts in hourly post volume
hourly = original.set_index("time").resample("h")["id"].count()
# previous 24 hours
baseline = hourly.rolling(24, min_periods=12).median().shift(1)
spread = hourly.rolling(24, min_periods=12).std().shift(1)
z = (hourly - baseline) / spread
bursts = hourly[z > 3]
print("Burst hours (more than 3 standard deviations above the recent median):")
print(bursts.to_string())
