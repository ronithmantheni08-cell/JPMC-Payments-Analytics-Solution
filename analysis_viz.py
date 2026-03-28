import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Absolute Path
file_path = '/Users/ronithmantheni/Documents/data/jpmc_payments_data.csv'

# 2. Start the 'Tent' (The if block)
if os.path.exists(file_path):
    # --- EVERYTHING BELOW IS INDENTED 4 SPACES ---
    df = pd.read_csv(file_path)
    print("Success! Data loaded.")

    # Prepare Data
    funnel_data = df['Last_Step_Reached'].value_counts().sort_index()
    labels = {1: '1. Started', 2: '2. Details', 3: '3. Security', 4: '4. Success'}
    
    plot_df = pd.DataFrame({
        'Step': [labels[i] for i in funnel_data.index],
        'Count': funnel_data.values
    })

    # Plotting (Stay indented!)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_df, x='Step', y='Count', palette='viridis')
    plt.title('JPMC Payments Digital Funnel Analysis')
    
    # Saving and Showing (Stay indented!)
    save_path = '/Users/ronithmantheni/Documents/data/funnel_chart.png'
    plt.savefig(save_path)
    print(f"Chart saved at {save_path}")
    plt.show()
    # --- END OF INDENTATION ---

else:
    print(f"File not found at: {file_path}")