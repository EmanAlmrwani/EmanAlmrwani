"""Sales analysis demo; place synthetic_orders.csv under data/ before running."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
orders=pd.read_csv(root/"data"/"synthetic_orders.csv",parse_dates=["order_date"])
assert orders["order_id"].is_unique
assert orders.notna().all().all()
completed=orders.loc[orders.order_status.eq("Completed")].copy()
completed["revenue_sar"]=(completed.quantity*completed.unit_price_sar*(1-completed.discount_rate)).round(2)
completed["month"]=completed.order_date.dt.to_period("M").astype(str)
print("Completed orders:",len(completed))
print("Total synthetic revenue (SAR):",round(completed.revenue_sar.sum(),2))
print("Unique customers:",completed.customer_id.nunique())
print("Average order value:",round(completed.revenue_sar.mean(),2))
for field in ["month","category","region"]:
    grouped=completed.groupby(field,as_index=False).revenue_sar.sum()
    print("\\n",field,"\\n",grouped.to_string(index=False))
    ax=grouped.plot(x=field,y="revenue_sar",kind="bar",legend=False,title=f"Revenue by {field} (synthetic data)")
    ax.set_ylabel("Revenue (SAR)")
    plt.tight_layout()
    plt.show()
