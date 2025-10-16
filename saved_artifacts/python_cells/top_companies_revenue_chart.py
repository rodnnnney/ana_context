"""
Flash Cab Market Dominance Visualization
Generated from Chicago Taxi Trip Data Analysis

This script creates a horizontal bar chart showing the top 10 taxi companies
by total revenue, highlighting Flash Cab's market dominance.

Author: Ana
Date: 2025-10-16
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_top_companies_chart(df, output_file='top_companies_revenue.png'):
    """
    Create a horizontal bar chart of top taxi companies by revenue.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns: company, trip_total, unique_key
    output_file : str
        Output filename for the chart
        
    Returns:
    --------
    None (saves chart to file)
    """
    # Set style
    sns.set_style("whitegrid")
    
    # Aggregate data by company
    top_companies = df.groupby('company').agg({
        'trip_total': 'sum',
        'unique_key': 'count'
    }).round(2)
    top_companies.columns = ['Total Revenue', 'Trip Count']
    top_companies = top_companies.sort_values('Total Revenue', ascending=True).tail(10)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Shorten company names for readability
    company_names = [name[:35] + '...' if len(name) > 35 else name 
                     for name in top_companies.index]
    
    # Create color gradient
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(top_companies)))
    bars = ax.barh(range(len(top_companies)), top_companies['Total Revenue'], color=colors)
    
    # Set labels and title
    ax.set_yticks(range(len(top_companies)))
    ax.set_yticklabels(company_names, fontsize=10)
    ax.set_xlabel('Total Revenue ($)', fontsize=12, fontweight='bold')
    ax.set_title('Top 10 Taxi Companies by Revenue\nFlash Cab Dominates the Market', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, top_companies['Total Revenue'])):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f'${value:,.0f}',
                ha='left', va='center', fontweight='bold', fontsize=9, 
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ Chart saved to {output_file}")
    return top_companies


# Example usage:
# Assuming you have a DataFrame 'df' with taxi trip data
# top_companies_data = create_top_companies_chart(df)
# print(top_companies_data)
