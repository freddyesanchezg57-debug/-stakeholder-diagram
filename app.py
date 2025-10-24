from flask import Flask, request, send_file, jsonify
import matplotlib
matplotlib.use('Agg')
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
        
        fig, ax = plt.subplots(figsize=(18, 14))
        ax.set_aspect('equal')
        ax.axis('off')
        
        radius = 3.5
        center_x = 8
        center_y = 7
        separation = 3.2
        
        circle1_center = (center_x - separation*0.866, center_y + separation*0.5)
        circle2_center = (center_x + separation*0.866, center_y + separation*0.5)
        circle3_center = (center_x, center_y - separation)
        
        color_poder = '#ffcccc'
        color_legitimidad = '#ccccff'
        color_urgencia = '#ccffcc'
        
        circle1 = Circle(circle1_center, radius, fill=True, facecolor=color_poder, edgecolor='darkred', linewidth=2.5, alpha=0.5, zorder=1)
        circle2 = Circle(circle2_center, radius, fill=True, facecolor=color_legitimidad, edgecolor='darkblue', linewidth=2.5, alpha=0.5, zorder=1)
        circle3 = Circle(circle3_center, radius, fill=True, facecolor=color_urgencia, edgecolor='darkgreen', linewidth=2.5, alpha=0.5, zorder=1)
        
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        
        ax.text(circle1_center[0] - 3.2, circle1_center[1] + 2.2, 'Poder', fontsize=16, fontweight='bold', ha='center')
        ax.text(circle2_center[0] + 3.2, circle2_center[1] + 2.2, 'Legitimidad', fontsize=16, fontweight='bold', ha='center')
        ax.text(circle3_center[0], circle3_center[1] - 4.2, 'Urgencia', fontsize=16, fontweight='bold', ha='center')
        
        def format_names(names, num, max_names=5):
