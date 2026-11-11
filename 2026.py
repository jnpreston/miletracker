import datetime

# ==========================================
# ENTER YOUR PROGRESS HERE
# ==========================================
TARGET_MILES = 2026.0
CURRENT_MILES = 1661.2  # Update this number as you ride!
# ==========================================

# Date configurations
GOAL_DATE = datetime.date(2026, 12, 31)
TODAY = datetime.date.today()

# Calculations
miles_remaining = max(0.0, TARGET_MILES - CURRENT_MILES)
days_remaining = (GOAL_DATE - TODAY).days + 1  # Includes today

print("=" * 45)
print(f"🚴 ROAD TO {int(TARGET_MILES)} MILES TRACKER 🚴")
print("=" * 45)
print(f"Today's Date:      {TODAY.strftime('%B %d, %Y')}")
print(f"Current Progress:  {CURRENT_MILES:,.1f} miles")
print(f"Miles Remaining:   {miles_remaining:,.1f} miles")
print(f"Days Left:         {days_remaining} days")
print("-" * 45)

if miles_remaining > 0:
   daily_average = miles_remaining / days_remaining
   weekly_average = daily_average * 7
   percent_done = (CURRENT_MILES / TARGET_MILES) * 100

   print(f"Progress:          {percent_done:.1f}% complete")
   print(f"➡️ Needed Daily:   {daily_average:.2f} miles / day")
   print(f"➡️ Needed Weekly:  {weekly_average:.2f} miles / week")
else:
   print("🎉 CONGRATULATIONS! You have smashed your 2026 goal! 🎉")

print("=" * 45)
