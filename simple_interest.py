# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("🧮 Simple Interest Calculator")
p = float(input("Enter Principal Amount (₹): "))
r = float(input("Enter Interest Rate (%): "))
t = float(input("Enter Time (years): "))

si = calculate_simple_interest(p, r, t)
print(f"📊 Simple Interest = ₹{si:.2f}")
