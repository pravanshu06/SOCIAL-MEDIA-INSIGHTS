from utils.data_loader import load_data
from utils.analyzer import analyze_data
from utils.visualizer import visualize
from config import DATA_PATH, OUTPUT_PATH
import json

def main():
    data = load_data(DATA_PATH)
    insights = analyze_data(data)
    visualize(data)

    # Save results
    with open(OUTPUT_PATH, "w") as f:
        json.dump(insights, f, indent=4)

if __name__ == "__main__":
    main()
