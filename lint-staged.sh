for file_path in $(git diff --cached --name-only); do
  [[ "$file_path" =~ ^.*\.py$ ]] && black --check $file_path
done
exit 0