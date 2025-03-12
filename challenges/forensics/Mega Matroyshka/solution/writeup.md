## Solution
Use a script to extract all 100 layers using binwalk.

```bash
#!/bin/bash
# Recursive extraction script for Mega Matroyshka challenge.
# It extracts the current file with binwalk, then moves the next doll.jpeg
# to the working directory (cleaning up extraction folders) before proceeding.

# Start with the challenge file
current_file="mega_matroyshka.jpeg"
layer=1

while [ $layer -le 100 ]; do
    echo "[*] Extracting layer $layer from $current_file"

    # Run binwalk on the current file.
    # Note: binwalk will create an extraction folder named: _<filename>.extracted
    binwalk -e "$current_file" >/dev/null 2>&1

    # Calculate the extraction folder path.
    base_name=$(basename "$current_file")
    extract_dir="$(dirname "$current_file")/_${base_name}.extracted"

    if [ ! -d "$extract_dir" ]; then
        echo "[-] Extraction folder not found for layer $layer at $extract_dir"
        exit 1
    fi

    # Check for the flag (flag.txt) anywhere inside the extraction folder.
    flag_file=$(find "$extract_dir" -type f -name "flag.txt" 2>/dev/null | head -n 1)
    if [ -n "$flag_file" ]; then
        echo "[+] Flag found:"
        cat "$flag_file"
        # Clean up before exit.
        rm -rf "$extract_dir"
        exit 0
    fi

    # Find the next doll.jpeg within the extraction folder.
    next_file=$(find "$extract_dir" -type f -name "doll.jpeg" | head -n 1)
    if [ -z "$next_file" ]; then
        echo "[-] doll.jpeg not found in layer $layer."
        exit 1
    fi

    # Move the next doll.jpeg out to the working directory as the new current_file.
    new_file="layer${layer}_doll.jpeg"
    mv "$next_file" "$new_file"
    echo "[*] Moved next layer to $new_file"

    # Clean up the extraction folder to reduce clutter.
    rm -rf "$extract_dir"

    # Set up for the next iteration.
    current_file="$new_file"
    layer=$((layer + 1))
done

echo "[-] Reached 100 layers without finding the flag."
exit 1
