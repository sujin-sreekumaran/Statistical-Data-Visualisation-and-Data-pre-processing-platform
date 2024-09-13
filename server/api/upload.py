import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' to avoid GUI issues

from flask import Blueprint, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from scipy.stats import skew, kurtosis

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    # Determine whether it's CSV or Excel
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        return 'Invalid file format', 400

    try:
        # Create visualizations in a single column layout
        fig, axes = plt.subplots(4, 1, figsize=(16, 24))  # Increased width to 16 for better fit
        
        # Visualization 1: Curve Plot
        numeric_df = df.select_dtypes(include=['number'])
        if not numeric_df.empty and numeric_df.shape[1] > 0:
            axes[0].plot(numeric_df.index, numeric_df[numeric_df.columns[0]], label=numeric_df.columns[0])
            axes[0].set_title('Curve Plot')
            axes[0].legend()
        else:
            axes[0].text(0.5, 0.5, 'No numeric data for Curve Plot', ha='center', va='center', fontsize=12)
            axes[0].set_title('Curve Plot')

        # Visualization 2: Boxplot
        if not numeric_df.empty and numeric_df.shape[1] > 0:
            sns.boxplot(data=numeric_df, ax=axes[1])
            axes[1].set_title('Boxplot')
        else:
            axes[1].text(0.5, 0.5, 'No numeric data for Boxplot', ha='center', va='center', fontsize=12)
            axes[1].set_title('Boxplot')

        # Visualization 3: Moments
        if not numeric_df.empty and numeric_df.shape[1] > 0:
            moments_df = pd.DataFrame({
                'Mean': numeric_df.mean(),
                'Variance': numeric_df.var(),
                'Skewness': numeric_df.apply(skew),
                'Kurtosis': numeric_df.apply(kurtosis)
            })
            moments_df.plot(kind='bar', ax=axes[2])
            axes[2].set_title('Moments of Numeric Data')
            axes[2].set_ylabel('Value')
        else:
            axes[2].text(0.5, 0.5, 'No numeric data for Moments Plot', ha='center', va='center', fontsize=12)
            axes[2].set_title('Moments of Numeric Data')

        # Visualization 4: Heatmap
        if not numeric_df.empty:
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=axes[3])
            axes[3].set_title('Correlation Heatmap')
        else:
            axes[3].text(0.5, 0.5, 'No numeric data for Heatmap', ha='center', va='center', fontsize=12)
            axes[3].set_title('Correlation Heatmap')

        plt.tight_layout()

        # Save the figure to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight', dpi=300)  # Increase resolution for better quality
        img.seek(0)
       
        # Return the image as a response
        return send_file(img, mimetype='image/png')
    
    except Exception as e:
        return str(e), 500
