def modify_content(text):
    """
    Modify the content of the file before writing.
    For this example, we'll convert text to uppercase.
    """
    return text.upper()


def file_read_write():
    try:
        # Ask user for input file
        input_file = input("Enter the filename to read: ")

        # Read file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify content
        modified_content = modify_content(content)

        # Write to new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: Permission denied. Cannot read/write the file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    file_read_write()
