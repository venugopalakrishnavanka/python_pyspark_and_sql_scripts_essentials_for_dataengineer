import pickle

def save_data(data_list, filename="pickle_file.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data_list, f)
    print("Data saved successfully.")

def load_data(filename="pickle_file.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":
    items = ["Apple", "Banana", "Cherry"]
    save_data(items)
    restored_items = load_data()
    print("Restored items:", restored_items)