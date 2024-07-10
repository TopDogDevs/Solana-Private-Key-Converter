import json
import base58

def decode_base58_to_private_key(base58_key):
    """Decodes a Base58-encoded private key to a list of integers."""
    private_key_bytes = base58.b58decode(base58_key)
    private_key_list = list(private_key_bytes)
    return private_key_list

def save_private_key_to_json(private_key_list, file_path):
    """Saves a private key list to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(private_key_list, f, separators=(',', ':'))  # Remove whitespace

def read_private_key_from_json(file_path):
    """Reads a private key from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def encode_private_key_to_base58(private_key_bytes):
    """Encodes a private key to Base58."""
    private_key_base58 = base58.b58encode(bytes(private_key_bytes)).decode('utf-8')
    return private_key_base58

def main():
    """Provides options to convert between Base58 and JSON private key formats."""
    while True:
        print("\nChoose an option:")
        print("1. Convert Base58 to JSON")
        print("2. Convert JSON to Base58")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            base58_key = input("Enter your Base58 encoded private key: ")
            try:
                private_key_list = decode_base58_to_private_key(base58_key)
                print("Decoded Private Key (JSON Style):", json.dumps(private_key_list, separators=(',', ':')))  # Remove whitespace
                save_json = input("Save to JSON? (yes/no): ").strip().lower()
                if save_json == 'yes':
                    json_file_path = input("Enter the path to save the JSON file: ")
                    save_private_key_to_json(private_key_list, json_file_path)
                    print(f"Private key saved to {json_file_path}")
                else:
                    print("Private key was not saved.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == '2':
            file_path = input("Enter the path to your keyfile.json: ")
            try:
                private_key_bytes = read_private_key_from_json(file_path)
                private_key_base58 = encode_private_key_to_base58(private_key_bytes)
                print("Base58 Encoded Private Key:", private_key_base58)
            except Exception as e:
                print("An error occurred:", e)

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()