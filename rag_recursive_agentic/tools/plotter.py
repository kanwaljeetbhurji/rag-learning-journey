# tools/plotter.py
import matplotlib
matplotlib.use('Agg')  # Add this line at the top before importing pyplot
import matplotlib.pyplot as plt
import os

def plot_bar_chart(data, x_field, y_field, title, xlabel, ylabel, output_dir="static/charts"):
    """
    Generate and save a bar chart from structured data.

    Args:
        data (list of dict): Data records (from JSON).
        x_field (str): Field name for x-axis.
        y_field (str): Field name for y-axis.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        output_dir (str): Directory to save chart.

    Returns:
        str: Path to saved chart image.
    """
    if not data:
        return None

    # Ensure output dir exists
    os.makedirs(output_dir, exist_ok=True)

    x_vals = [record[x_field] for record in data]
    y_vals = [record.get(y_field, 0) for record in data]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(x_vals, y_vals, color="seagreen")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=20, ha='right')

    # Label values on top
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.1f}', ha='center', va='bottom')

    filename = f"{title.lower().replace(' ', '_')}.png"
    output_path = os.path.join(output_dir, filename)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path
