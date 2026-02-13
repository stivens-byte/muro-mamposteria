import matplotlib.pyplot as plt

def dibujar_muro(H, B, t, Pa, W):
    fig, ax = plt.subplots(figsize=(6, 5))
    
    # Muro (Mampostería)
    ax.fill([0, B, t, 0, 0], [0, 0, H, H, 0], color="#9e9e9e", edgecolor="black", label="Mampostería")
    
    # Suelo sobre el trasdós
    ax.fill([t, B, B], [H, 0, H], color="#d2b48c", alpha=0.5, label="Suelo (Relleno)")
    
    # Flecha Empuje
    ax.arrow(B + 0.5, H/3, -0.4, 0, head_width=0.15, color="red")
    ax.text(B + 0.6, H/3, f"Pa={Pa:.1f} tonf", color="red", fontweight="bold")
    
    ax.set_aspect("equal")
    ax.set_title("Geometría del Muro (tonf/m)")
    ax.grid(True, linestyle=":", alpha=0.6)
    return fig
