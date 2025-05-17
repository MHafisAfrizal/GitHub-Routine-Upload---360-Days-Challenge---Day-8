# pricing_data.py

import json

# Data paket pricing
pricing_plans = [
    {
        "name": "Basic",
        "price": 10,
        "currency": "USD",
        "features": [
            "1 Website",
            "Email Support",
            "Basic Analytics"
        ]
    },
    {
        "name": "Pro",
        "price": 25,
        "currency": "USD",
        "features": [
            "5 Websites",
            "Priority Support",
            "Advanced Analytics",
            "SEO Tools"
        ]
    },
    {
        "name": "Ultimate",
        "price": 50,
        "currency": "USD",
        "features": [
            "Unlimited Websites",
            "24/7 Support",
            "Full Analytics",
            "SEO Tools",
            "Marketing Reports"
        ]
    }
]

# Simpan sebagai JSON
with open("pricing.json", "w") as file:
    json.dump(pricing_plans, file, indent=4)

print("✅ Data paket pricing berhasil disimpan ke pricing.json!")
