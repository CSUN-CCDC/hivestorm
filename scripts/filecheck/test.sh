#!/bin/bash

# Define multimedia file types
multimedia_types=("JPEG" "PNG" "GIF" "MP4" "MP3" "WAV")

# Function to check if a file is multimedia
is_multimedia() {
    file_type=$(file "$1" | cut -d' ' -f2)
    for type in "${multimedia_types[@]}"; do
        if [[ "$file_type" == *"$type"* ]]; then
            return 0  # Return success (multimedia file)
        fi
    done
    return 1  # Return failure (not a multimedia file)
}

# Find multimedia files in the home directory
find_multimedia_files() {
    local home_dir="$1"
    while IFS= read -r -d '' file; do
        if is_multimedia "$file"; then
            echo "$file"
        fi
    done < <(find "$home_dir" -type f -print0)
}

# Main execution
home_dir="/home/beep/pictures"
echo "Searching for multimedia files in $home_dir..."
multimedia_files=$(find_multimedia_files "$home_dir")

# Print results
if [ -n "$multimedia_files" ]; then
    echo -e "Multimedia files found:\n$multimedia_files"
else
    echo "No multimedia files found in $home_dir."
fi

