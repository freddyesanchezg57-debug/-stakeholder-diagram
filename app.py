from flask import Flask, request, send_file, jsonify
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle
import io

app = Flask(__name__)

@app.route('/stakeholder-venn', methods=['POST'])
def generate_stakeholder_venn():
    try:
        data = request.json
        categorias = data['categorias']
        
        # Crear figura
        fig, ax = plt.subplots(figsize=(18, 14))
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Parámetros de los círculos
        radius = 3.5
        center_x = 8
        center_y = 7
        separation = 3.2
        
        # Centros de los 3 círculos
        circle1_center = (center_x - separation*0.866, center_y + separation*0.5)
        circle2_center = (center_x + separation*0.866, center_y + separation*0.5)
        circle3_center = (center_x, center_y - separation)
        
        # Colores
        color_poder = '#ffcccc'
        color_legitimidad = '#ccccff'
        color_urgencia = '#ccffcc'
        
        # Dibujar círculos
        circle1 = Circle(circle1_center, radius, fill=True, facecolor=color_poder,
                        edgecolor='darkred', linewidth=2.5, alpha=0.5, zorder=1)
        circle2 = Circle(circle2_center,
