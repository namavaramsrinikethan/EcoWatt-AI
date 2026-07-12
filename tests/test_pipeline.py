from src.pipeline import run_pipeline

results = run_pipeline(
    dataset_path="datasets/household_power_consumption.txt",
    model_path="models/prophet_model.pkl",
    tariff_rate=8.5
)

print("\nPipeline Executed Successfully!\n")

print("Health Report:")
print(results["health"])

print("\nBill Summary:")
print(results["bill"])

print("\nRecommendations:")
for card in results["recommendations"]:
    print(f"- {card['title']}")