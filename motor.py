import math

def analizar_muro(H, B, t, gamma_m, gamma_s, phi, hz):
    # Unidades: tonf, m
    phi_rad = math.radians(phi)
    
    # 1. Coeficiente de Rankine (Ka)
    Ka = (1 - math.sin(phi_rad)) / (1 + math.sin(phi_rad))

    # 2. Empuje Activo (Pa) - Se aplica a H/3
    Pa = 0.5 * Ka * gamma_s * (H ** 2)

    # 3. Pesos y Centros de Gravedad (cg) desde x=0
    # W1: Rectángulo frontal (Mampostería)
    W1 = t * H * gamma_m
    x1 = t / 2
    
    # W2: Triángulo trasero (Mampostería)
    ancho_tri = B - t
    W2 = (0.5 * ancho_tri * H) * gamma_m
    x2 = t + (ancho_tri / 3)
    
    # W3: Suelo sobre el trasdós inclinado (Zona 3)
    W3 = (0.5 * ancho_tri * H) * gamma_s
    x3 = t + (2 * ancho_tri / 3)

    W_total = W1 + W2 + W3

    # 4. Momentos (Punto de giro en el dedo/punta x=0)
    M_est = (W1 * x1) + (W2 * x2) + (W3 * x3)
    M_vol = Pa * (H / 3)

    # 5. Factores de Seguridad
    fs_vol = M_est / M_vol if M_vol > 0 else 99.0
    # En deslizamiento usamos la fricción base (tan(phi))
    fs_des = (W_total *math.tan((2/3)*phi_rad)) / Pa
    #Considerando Pasivo
    Kp = (math.tan(math.radians(45)+phi_rad/2))**2
    Pp = 0.5*Kp*gamma_s*hz**2
    fs_despasivo = ((W_total *math.tan((2/3)*phi_rad)) + Pp) / Pa

    # 6. Excentricidad y Presiones
    x_res = (M_est - M_vol) / W_total
    e = abs((B / 2) - x_res)
    
    # Fórmulas de Navier-Schule para presiones
    if e <= B / 6:
        q_max = (W_total / B) * (1 + 6 * e / B)
        q_min = (W_total / B) * (1 - 6 * e / B)
    else:
        q_max = (2 * W_total) / (3 * x_res)
        q_min = 0.0

    return {
        "Pa": Pa, "W_total": W_total, "FS_vol": fs_vol,
        "FS_des": fs_des, "FS_despasivo": fs_despasivo, "q_max": q_max, "e": e
    }
