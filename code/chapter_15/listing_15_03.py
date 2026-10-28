# Listing 15.3: Sinusoidal positional encodings
def positional_encoding(n_positions, d_model):
    pos = np.arange(n_positions)[:, None]
    i = np.arange(d_model)[None, :]
    angles = pos / np.power(10000, (2 * (i // 2)) / d_model)
    pe = np.zeros((n_positions, d_model))
    pe[:, 0::2] = np.sin(angles[:, 0::2])            # even dimensions
    pe[:, 1::2] = np.cos(angles[:, 1::2])            # odd dimensions
    return pe

pe = positional_encoding(50, 64)
print(pe.shape)
print("Similarity of position 10 to positions 9, 11, 30:",
      [round(cos(pe[10], pe[j]), 2) for j in (9, 11, 30)])
