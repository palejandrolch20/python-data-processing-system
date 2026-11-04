import pandas as pd

class DataAnalyzer:

    def calculate_metrics(self, df : pd.DataFrame) :


        total_production= df["production"].sum()
        total_defects = df["defects"].sum()
        good_production = total_production - total_defects
        average_efficiency = df["efficiency"].mean()
        quality_percentage = round((good_production / total_production) * 100,2)
        metrics = {
            "total_production": total_production,
            "total_defects": total_defects,
            "good_production": good_production,
            "average_efficiency": average_efficiency,
            "quality_percentage" : quality_percentage        
            }

        return metrics