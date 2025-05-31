# Based on different features, we'll assign traits to each customer cluster representing the type of customers in each of them
def generate_persona_labels(cluster_summary_df):
    personas = {}

    for cluster_id, row in cluster_summary_df.iterrows():
        traits = []

        # Income level
        if row['Income'] > 80000:
            traits.append("High-Income")
        elif row['Income'] < 30000:
            traits.append("Low-Income")
        else:
            traits.append("Middle-Income")

        # Total Spend
        if row['Total_Spend'] > 1000:
            traits.append("Heavy Spender")
        elif row['Total_Spend'] < 100:
            traits.append("Low Spender")
        else:
            traits.append("Moderate Spender")

        # Recency
        if row['Recency'] > 60:
            traits.append("Recently Inactive")
        elif row['Recency'] < 30:
            traits.append("Recently Active")

        # Campaign responsiveness
        if row['Total_Campaigns_Accepted'] >= 2:
            traits.append("Highly Responsive to Campaigns")
        elif row['Total_Campaigns_Accepted'] == 0:
            traits.append("Not Responsive to Campaigns")

        # Complaint status
        if row['Complain'] > 0:
            traits.append("Complainers")
        else:
            traits.append("No Complaints")

        # Web activity
        if row['NumWebPurchases'] >= 5 or row['NumWebVisitsMonth'] >= 6:
            traits.append("Digital Shoppers")
        elif row['NumWebPurchases'] <= 2:
            traits.append("Low Online Activity")

        # Store purchases
        if row['NumStorePurchases'] >= 8:
            traits.append("In-Store Loyalists")

        # Age
        if row['Age'] < 35:
            traits.append("Young Adults")
        elif row['Age'] >= 60:
            traits.append("Seniors")
        else:
            traits.append("Middle-Aged")

        # Family
        if row['Family_Size'] >= 3:
            traits.append("Large Families")
        else:
            traits.append("Small Households")

        # Label
        personas[cluster_id] = ", ".join(traits)

    return personas